"""Watch source files and serve a freshly built static site; no npm install required."""
import argparse
import functools
import http.server
import threading
import time
from build import ROOT, OUT, build

def snapshot():
    return {str(p): p.stat().st_mtime_ns for folder in ['site', 'data/results', 'docs'] for p in (ROOT / folder).rglob('*') if p.is_file()}

def watch():
    previous = snapshot()
    while True:
        time.sleep(0.75)
        current = snapshot()
        if current != previous:
            try:
                build()
                previous = current
            except Exception as error:
                print(f'Build failed; fix the source and save again: {error}', flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=4173)
    args = parser.parse_args()
    build()
    threading.Thread(target=watch, daemon=True).start()
    class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
        # Always serve the freshest build: browsers otherwise cache ES modules heuristically.
        def end_headers(self):
            self.send_header('Cache-Control', 'no-store, must-revalidate')
            super().end_headers()
    handler = functools.partial(NoCacheHandler, directory=str(OUT))
    server = http.server.ThreadingHTTPServer(('127.0.0.1', args.port), handler)
    print(f'Local: http://127.0.0.1:{args.port}', flush=True)
    server.serve_forever()
