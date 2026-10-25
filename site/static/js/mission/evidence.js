// Renders big-data result files (data/results/bigdata/*.json) into evidence panels,
// partner lists, future-data plans and the appendix. No external libraries.
import { readJSON, esc } from '../lib.js';

const COLORS = { orange: '#ff945c', cyan: '#8bcedb', violet: '#b7b2f2', green: '#b4dcb3', amber: '#ffb482', grey: '#6f7b88', red: '#ff6b6b', white: '#eff1ef' };
const PALETTE = ['orange', 'cyan', 'violet', 'green', 'amber', 'grey'];
const cache = new Map();

export function loadResult(id) {
  if (!cache.has(id)) cache.set(id, readJSON(`results/bigdata/${id}.json`));
  return cache.get(id);
}
let indexPromise, displayPromise;
export function loadDisplay() {
  displayPromise ||= readJSON('content/evidence-display.json').catch(() => ({}));
  return displayPromise;
}
const firstSentences = (text, max = 220) => {
  if (!text || text.length <= max) return text;
  const cut = text.slice(0, max); const stop = cut.lastIndexOf('. ');
  return (stop > 60 ? cut.slice(0, stop + 1) : cut.trimEnd() + '…');
};
export function loadIndex() {
  indexPromise ||= readJSON('results/bigdata/index.json').catch(() => ({ analyses: [] }));
  return indexPromise;
}

export function formatBytes(bytes) {
  if (!Number.isFinite(bytes) || bytes <= 0) return '—';
  const units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB'];
  let i = 0; let v = bytes;
  while (v >= 1000 && i < units.length - 1) { v /= 1000; i++; }
  return `${v >= 100 ? v.toFixed(0) : v >= 10 ? v.toFixed(1) : v.toFixed(2)} ${units[i]}`;
}
export function formatCount(n) {
  if (!Number.isFinite(n)) return '—';
  const abs = Math.abs(n);
  if (abs >= 1e9) return `${(n / 1e9).toFixed(abs >= 1e10 ? 0 : 1)}B`;
  if (abs >= 1e6) return `${(n / 1e6).toFixed(abs >= 1e7 ? 0 : 1)}M`;
  if (abs >= 1e4) return `${(n / 1e3).toFixed(0)}k`;
  return n.toLocaleString('en-US');
}
function fmtTick(v, scale) {
  if (scale === 'log') {
    const e = Math.round(Math.log10(v));
    if (Math.abs(e) >= 4) return `1e${e}`;
  }
  const abs = Math.abs(v);
  if (abs === 0) return '0';
  if (abs >= 1e6) return formatCount(v);
  if (abs >= 1e4) return `${(v / 1e3).toFixed(0)}k`;
  if (abs >= 100) return v.toFixed(0);
  if (abs >= 1) return Number.isInteger(v) ? String(v) : v.toFixed(1);
  if (abs >= 0.01) return v.toFixed(2);
  return v.toExponential(0);
}

function niceTicks(min, max, count = 5) {
  if (!Number.isFinite(min) || !Number.isFinite(max)) return [0, 1];
  if (min === max) { const d = Math.abs(min) || 1; min -= d / 2; max += d / 2; }
  const span = max - min;
  const step0 = span / count;
  const mag = 10 ** Math.floor(Math.log10(step0));
  const err = step0 / mag;
  const step = (err >= 7.5 ? 10 : err >= 3.5 ? 5 : err >= 1.5 ? 2 : 1) * mag;
  const ticks = [];
  const start = Math.floor(min / step + 1e-9) * step, end = Math.ceil(max / step - 1e-9) * step;
  for (let t = start; t <= end + step * 1e-9; t += step) ticks.push(Math.abs(t) < step * 1e-6 ? 0 : +t.toPrecision(12));
  return ticks;
}
function logTicks(min, max) {
  const ticks = [];
  for (let e = Math.floor(Math.log10(min)); e <= Math.ceil(Math.log10(max)); e++) ticks.push(10 ** e);
  return ticks;
}
function makeScale(domain, range, type) {
  let [d0, d1] = domain;
  const [r0, r1] = range;
  if (type === 'log') {
    d0 = Math.max(d0, 1e-12); d1 = Math.max(d1, d0 * 10);
    const l0 = Math.log10(d0), l1 = Math.log10(d1);
    return v => r0 + (Math.log10(Math.max(v, d0)) - l0) / (l1 - l0) * (r1 - r0);
  }
  if (d1 === d0) d1 = d0 + 1;
  return v => r0 + (v - d0) / (d1 - d0) * (r1 - r0);
}
const colorOf = (series, i) => COLORS[series.color] || COLORS[PALETTE[i % PALETTE.length]];

// Normalise the many shapes a result file may use into {x, y, x1?} rows.
function pointsOf(series) {
  return (series.points || []).filter(p => Array.isArray(p) && p.length >= 2).map(p => (
    p.length >= 3 && typeof p[0] === 'number' && typeof p[1] === 'number' && typeof p[2] === 'number'
      ? { x: p[0], x1: p[1], y: p[2] } : { x: p[0], y: Number(p[1]), label: p[2] }
  )).filter(p => Number.isFinite(p.y));
}

export function renderChart(chart) {
  const W = 680, H = 380, M = { l: 70, r: 22, t: 18, b: 58 };
  const kind = chart.kind || 'line';
  const series = (chart.series || []).map((s, i) => ({ ...s, color: colorOf(s, i), pts: pointsOf(s) })).filter(s => s.pts.length);
  if (!series.length) return '<p class="caption">No data in this chart.</p>';
  const xScaleType = chart.x?.scale || 'linear';
  const yScaleType = chart.y?.scale || 'linear';
  const categorical = series.some(s => s.pts.some(p => typeof p.x === 'string')) || ['bar', 'hbar', 'stacked'].includes(kind) && series.every(s => s.pts.every(p => typeof p.x === 'string' || Number.isInteger(p.x)));
  const innerW = W - M.l - M.r, innerH = H - M.t - M.b;
  let body = '', xAxis = '', yAxis = '', grid = '';
  const title = (s, p) => `${esc(s.name || '')}${s.name ? ' · ' : ''}${esc(p.label ?? p.x)}: ${(chart.x?.unit === 'bytes' || chart.y?.unit === 'bytes') ? formatBytes(p.y) : esc(fmtTick(p.y, 'linear')) + (chart.y?.unit ? ' ' + esc(chart.y.unit) : '')}`;

  if (kind === 'hbar') {
    const valueAxis = series.every(s => s.pts.every(p => typeof p.x === 'string')) ? (chart.y || chart.x) : chart.x;
    const xScaleType = valueAxis?.scale === 'log' ? 'log' : 'linear';
    const tickText = t => valueAxis?.unit === 'bytes' ? formatBytes(t) : fmtTick(t, xScaleType);
    const cats = [...new Set(series.flatMap(s => s.pts.map(p => String(p.x))))];
    const rowH = innerH / cats.length;
    const maxV = Math.max(...series.flatMap(s => s.pts.map(p => p.y)), 0);
    const ticks = xScaleType === 'log' ? logTicks(Math.min(...series.flatMap(s => s.pts.map(p => p.y)).filter(v => v > 0)), maxV) : niceTicks(0, maxV);
    const longest = Math.max(...cats.map(c => Math.min(c.length, 34)));
    const labelW = Math.min(230, Math.max(90, longest * 6.4));
    const x = makeScale([xScaleType === 'log' ? ticks[0] : 0, ticks[ticks.length - 1]], [M.l - 40 + labelW, W - M.r], xScaleType);
    ticks.forEach(t => { grid += `<line class="grid" x1="${x(t)}" x2="${x(t)}" y1="${M.t}" y2="${H - M.b}"/>`; xAxis += `<text class="tick" x="${x(t)}" y="${H - M.b + 18}" text-anchor="middle">${tickText(t)}</text>`; });
    const bandH = rowH * 0.7 / series.length;
    cats.forEach((c, ci) => {
      yAxis += `<text class="tick cat" x="${M.l - 48 + labelW}" y="${M.t + rowH * ci + rowH / 2 + 4}" text-anchor="end">${esc(c.length > 34 ? c.slice(0, 33) + '…' : c)}<title>${esc(c)}</title></text>`;
      series.forEach((s, si) => {
        const p = s.pts.find(q => String(q.x) === c); if (!p) return;
        const y0 = M.t + rowH * ci + rowH * 0.15 + bandH * si;
        const x0 = x(xScaleType === 'log' ? ticks[0] : 0);
        body += `<rect class="mark" x="${x0}" y="${y0}" width="${Math.max(1, x(p.y) - x0)}" height="${bandH}" fill="${s.color}"><title>${title(s, p)}</title></rect>`;
      });
    });
  } else if (categorical && (kind === 'bar' || kind === 'stacked')) {
    const cats = [...new Set(series.flatMap(s => s.pts.map(p => String(p.x))))];
    if (cats.every(c => !isNaN(+c))) cats.sort((a, b) => +a - +b);
    const band = innerW / cats.length;
    const stack = kind === 'stacked';
    const totals = cats.map(c => series.reduce((sum, s) => sum + (s.pts.find(p => String(p.x) === c)?.y || 0), 0));
    const maxV = stack ? Math.max(...totals) : Math.max(...series.flatMap(s => s.pts.map(p => p.y)));
    const minV = Math.min(0, ...series.flatMap(s => s.pts.map(p => p.y)));
    const ticks = yScaleType === 'log' ? logTicks(Math.max(1e-9, Math.min(...series.flatMap(s => s.pts.map(p => p.y)).filter(v => v > 0))), maxV) : niceTicks(minV, maxV);
    const y = makeScale([yScaleType === 'log' ? ticks[0] : ticks[0], ticks[ticks.length - 1]], [H - M.b, M.t], yScaleType);
    ticks.forEach(t => { grid += `<line class="grid" x1="${M.l}" x2="${W - M.r}" y1="${y(t)}" y2="${y(t)}"/>`; yAxis += `<text class="tick" x="${M.l - 10}" y="${y(t) + 4}" text-anchor="end">${fmtTick(t, yScaleType)}</text>`; });
    const every = Math.ceil(cats.length / 12);
    cats.forEach((c, ci) => {
      const cx = M.l + band * ci;
      const maxLen = cats.length <= 4 ? 34 : cats.length <= 8 ? 20 : 16;
      if (ci % every === 0) xAxis += `<text class="tick" x="${cx + band / 2}" y="${H - M.b + 18}" text-anchor="${cats.length > 8 && isNaN(+c) ? 'end' : 'middle'}" ${cats.length > 8 && isNaN(+c) ? `transform="rotate(-30 ${cx + band / 2} ${H - M.b + 18})"` : ''}>${esc(c.length > maxLen ? c.slice(0, maxLen - 1) + '…' : c)}<title>${esc(c)}</title></text>`;
      let acc = 0;
      series.forEach((s, si) => {
        const p = s.pts.find(q => String(q.x) === c); if (!p) return;
        if (stack) {
          const y0 = y(acc), y1 = y(acc + p.y); acc += p.y;
          body += `<rect class="mark" x="${cx + band * 0.12}" y="${y1}" width="${band * 0.76}" height="${Math.max(0.5, y0 - y1)}" fill="${s.color}"><title>${title(s, p)}</title></rect>`;
        } else {
          const bw = band * 0.76 / series.length;
          const base = y(Math.max(ticks[0], 0));
          const top = y(p.y);
          body += `<rect class="mark" x="${cx + band * 0.12 + bw * si}" y="${Math.min(base, top)}" width="${Math.max(1, bw - 1)}" height="${Math.max(0.5, Math.abs(base - top))}" fill="${s.color}"><title>${title(s, p)}</title></rect>`;
        }
      });
    });
  } else {
    const xs = series.flatMap(s => s.pts.flatMap(p => p.x1 !== undefined ? [p.x, p.x1] : [p.x])).map(Number).filter(Number.isFinite);
    const ys = series.flatMap(s => s.pts.map(p => p.y));
    let xMin = Math.min(...xs), xMax = Math.max(...xs);
    if (kind === 'hist') {
      // Infer bin width from point spacing when only bin starts or centres are given.
      const sorted = [...new Set(series[0].pts.map(p => +p.x))].sort((a, b) => a - b);
      const diffs = sorted.slice(1).map((v, i) => v - sorted[i]).filter(d => d > 0);
      const w = diffs.length ? Math.min(...diffs) : 1;
      series.forEach(s => s.pts.forEach(p => { if (p.x1 === undefined) { p.x1 = p.x + w; } }));
      xMax = Math.max(xMax, ...series.flatMap(s => s.pts.map(p => p.x1)));
    }
    let yMin = Math.min(...ys), yMax = Math.max(...ys);
    if (kind === 'hist' || kind === 'bar') yMin = Math.min(0, yMin);
    const refs = (chart.reference || []).concat(chart.annotations?.some(a => /y\s*=\s*x/i.test(a.text || '')) ? ['identity'] : []);
    if (refs.includes('identity')) { const lo = Math.min(xMin, yMin), hi = Math.max(xMax, yMax); xMin = yMin = lo; xMax = yMax = hi; }
    (chart.hlines || []).forEach(h => { yMin = Math.min(yMin, h.y); yMax = Math.max(yMax, h.y); });
    const xt = xScaleType === 'log' ? logTicks(Math.max(1e-30, xMin), xMax) : niceTicks(xMin, xMax, 6);
    const yt = yScaleType === 'log' ? logTicks(Math.max(1e-30, Math.min(...ys.filter(v => v > 0), ...(chart.hlines || []).map(h => h.y).filter(v => v > 0))), yMax) : niceTicks(yMin, yMax, 5);
    const x = makeScale([xScaleType === 'log' ? xt[0] : Math.min(xt[0], xMin), xt[xt.length - 1]], [M.l, W - M.r], xScaleType);
    const y = makeScale([yt[0], yt[yt.length - 1]], [H - M.b, M.t], yScaleType);
    yt.forEach(t => { grid += `<line class="grid" x1="${M.l}" x2="${W - M.r}" y1="${y(t)}" y2="${y(t)}"/>`; yAxis += `<text class="tick" x="${M.l - 10}" y="${y(t) + 4}" text-anchor="end">${fmtTick(t, yScaleType)}</text>`; });
    const isYear = xs.every(v => Number.isInteger(v) && v > 1900 && v < 2100);
    xt.forEach(t => { xAxis += `<text class="tick" x="${x(t)}" y="${H - M.b + 18}" text-anchor="middle">${isYear ? String(Math.round(t)) : fmtTick(t, xScaleType)}</text>`; });
    if (refs.includes('identity')) body += `<line class="ref" x1="${x(xt[0])}" y1="${y(yt[0])}" x2="${x(Math.min(xt[xt.length - 1], yt[yt.length - 1]))}" y2="${y(Math.min(xt[xt.length - 1], yt[yt.length - 1]))}"/><text class="ref-label" x="${x(xt[xt.length - 1]) - 6}" y="${y(Math.min(xt[xt.length - 1], yt[yt.length - 1])) + 14}" text-anchor="end">y = x</text>`;
    (chart.hlines || []).forEach(h => { body += `<line class="ref" x1="${M.l}" x2="${W - M.r}" y1="${y(h.y)}" y2="${y(h.y)}"/><text class="ref-label" x="${W - M.r - 4}" y="${y(h.y) - 6}" text-anchor="end">${esc(h.text || '')}</text>`; });
    (chart.vlines || []).forEach(v => { body += `<line class="ref" y1="${M.t}" y2="${H - M.b}" x1="${x(v.x)}" x2="${x(v.x)}"/><text class="ref-label" x="${x(v.x) + 5}" y="${M.t + 12}">${esc(v.text || '')}</text>`; });
    series.forEach(s => {
      if (kind === 'hist' || kind === 'bar') {
        s.pts.forEach(p => { const x0 = x(p.x), x1 = x(p.x1 ?? p.x + 1), base = y(Math.max(yt[0], 0)); body += `<rect class="mark" x="${x0 + 0.5}" y="${y(p.y)}" width="${Math.max(1, x1 - x0 - 1)}" height="${Math.max(0, base - y(p.y))}" fill="${s.color}" fill-opacity="${series.length > 1 ? 0.62 : 0.9}"><title>${title(s, { ...p, label: `${fmtTick(p.x, xScaleType)}–${fmtTick(p.x1, xScaleType)}` })}</title></rect>`; });
      } else if (kind === 'scatter') {
        s.pts.forEach(p => { body += `<circle class="mark dot" cx="${x(+p.x)}" cy="${y(p.y)}" r="${s.pts.length > 200 ? 2.4 : 3.6}" fill="${s.color}" fill-opacity=".72"><title>${title(s, p)}</title></circle>`; });
      } else {
        const sorted = [...s.pts].sort((a, b) => +a.x - +b.x);
        const d = sorted.map((p, i) => `${i ? 'L' : 'M'}${x(+p.x).toFixed(1)},${y(p.y).toFixed(1)}`).join('');
        if (s.band) {
          const lo = (s.band.low || []).map(p => ({ x: +p[0], y: +p[1] })).sort((a, b) => a.x - b.x);
          const hi = (s.band.high || []).map(p => ({ x: +p[0], y: +p[1] })).sort((a, b) => b.x - a.x);
          if (lo.length && hi.length) body += `<path class="band" d="${[...lo, ...hi].map((p, i) => `${i ? 'L' : 'M'}${x(p.x).toFixed(1)},${y(p.y).toFixed(1)}`).join('')}Z" fill="${s.color}"/>`;
        }
        body += `<path class="mark line" d="${d}" stroke="${s.color}" pathLength="1"/>`;
        if (sorted.length <= 40) sorted.forEach(p => { body += `<circle class="mark dot" cx="${x(+p.x)}" cy="${y(p.y)}" r="3" fill="${s.color}"><title>${title(s, p)}</title></circle>`; });
      }
    });
    (chart.annotations || []).filter(a => Number.isFinite(+a.x) && Number.isFinite(+a.y) && !/y\s*=\s*x/i.test(a.text || '')).forEach(a => {
      const ax = x(+a.x), right = ax > M.l + innerW * 0.7;
      body += `<g class="annotation"><circle cx="${ax}" cy="${y(+a.y)}" r="5"/><text x="${right ? ax - 9 : ax + 9}" y="${y(+a.y) - 8}" text-anchor="${right ? 'end' : 'start'}">${esc(a.text || '')}</text></g>`;
    });
  }
  const lab = a => a?.label ? `${esc(a.label)}${a.unit ? ` (${esc(a.unit)})` : ''}` : '';
  const hbarValueAxis = kind === 'hbar' ? (series.every(s => s.pts.every(p => typeof p.x === 'string')) ? (chart.y || chart.x) : chart.x) : null;
  const xl = kind === 'hbar' ? lab(hbarValueAxis) : lab(chart.x);
  const yl = kind === 'hbar' ? '' : lab(chart.y);
  const legend = series.length > 1 || series[0].name ? `<div class="chart-legend">${series.map(s => `<span><i style="background:${s.color}"></i>${esc(s.name || '')}</span>`).join('')}</div>` : '';
  return `<figure class="evidence-chart"><figcaption><span class="micro">${esc(chart.subtitle || '')}</span><strong>${esc(chart.title || '')}</strong></figcaption>${legend}<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(chart.title || 'Chart')}" preserveAspectRatio="xMidYMid meet">${grid}<line class="axis" x1="${M.l}" x2="${W - M.r}" y1="${H - M.b}" y2="${H - M.b}"/><line class="axis" x1="${M.l}" x2="${M.l}" y1="${M.t}" y2="${H - M.b}"/>${body}${xAxis}${yAxis}<text class="axis-label" x="${(M.l + W - M.r) / 2}" y="${H - 10}" text-anchor="middle">${xl}</text><text class="axis-label" transform="rotate(-90)" x="${-(M.t + H - M.b) / 2}" y="16" text-anchor="middle">${yl}</text></svg>${chart.caption ? `<p class="caption">${esc(chart.caption)}</p>` : ''}</figure>`;
}

function datasetChips(result) {
  const ds = result.datasets || [];
  const isListed = d => d.scope === 'inventoried' || (!d.scope && /listobjects|inventory/i.test(`${d.name} ${d.notes || ''}`));
  const processed = ds.filter(d => !isListed(d));
  const bytes = processed.reduce((s, d) => s + (+d.bytes || 0), 0);
  const records = processed.reduce((s, d) => s + (+d.records || 0), 0);
  const listed = ds.filter(isListed).reduce((s, d) => s + (+d.bytes || 0), 0);
  const c = result.compute || {};
  const chips = [
    bytes ? `<span><b>${formatBytes(bytes)}</b> processed</span>` : '',
    listed ? `<span><b>${formatBytes(listed)}</b> archive catalogued</span>` : '',
    records ? `<span><b>${formatCount(records)}</b> records</span>` : '',
    c.where ? `<span><b>${esc(String(c.where).split(/\s*[(;,]/)[0])}</b>${c.job_ids?.length ? ` · ${c.job_ids.length} Slurm job${c.job_ids.length > 1 ? 's' : ''}` : ''}</span>` : '',
    +c.cpu_hours >= 0.05 ? `<span><b>${(+c.cpu_hours).toFixed(c.cpu_hours < 10 ? 1 : 0)}</b> CPU-hours</span>` : ''
  ].filter(Boolean).join('');
  return `<div class="evidence-chips">${chips}</div><p class="evidence-sources">${ds.slice(0, 4).map(d => d.url ? `<a href="${esc(d.url)}">${esc(d.name)} ↗</a>` : esc(d.name)).join(' · ')}</p>`;
}

export function renderPanel(result, opts = {}) {
  const display = opts.display?.[result.id] || {};
  const wanted = opts.charts ? opts.charts.split(',').map(s => s.trim()) : display.charts || null;
  let charts = (result.charts || []).filter(c => !wanted || wanted.includes(c.id));
  if (wanted) charts.sort((a, b) => wanted.indexOf(a.id) - wanted.indexOf(b.id));
  charts = charts.slice(0, opts.maxCharts || 4).map(c => {
    if (opts.full) return c;
    const d = display[c.id] || {};
    return { ...c, series: d.series ? d.series.map(i => c.series[i]).filter(Boolean) : c.series, caption: d.caption || firstSentences(c.caption), title: d.title || c.title, reference: d.reference || c.reference };
  });
  const findings = (!opts.full && display.findings ? display.findings.map(i => (result.findings || [])[i]).filter(Boolean) : (result.findings || [])).slice(0, opts.findings ?? 3);
  const h = result.headline || {};
  return `<article class="evidence-panel ${opts.variant === 'compact' ? 'compact' : ''}" id="evidence-${esc(result.id)}">
    <header class="evidence-head"><div><span class="tag cyan">${esc((result.evidence_level || 'our computation').toUpperCase())}</span><h3>${esc(result.title)}</h3><p class="evidence-question">${esc(result.question || '')}</p></div>
    <div class="evidence-headline"><strong>${esc(h.value ?? '')}${String(h.unit ?? '').length <= 6 ? `<span>${esc(h.unit ?? '')}</span>` : ''}</strong>${String(h.unit ?? '').length > 6 ? `<em class="unit-long">${esc(h.unit)}</em>` : ''}<p>${esc(h.text || '')}</p></div></header>
    <div class="evidence-charts n${charts.length}">${charts.map(renderChart).join('')}</div>
    ${findings.length ? `<ul class="evidence-findings">${findings.map(f => `<li>${esc(f)}</li>`).join('')}</ul>` : ''}
    <footer class="evidence-foot">${datasetChips(result)}<a class="inline-link" href="appendix.html#${esc(result.id)}">Method, data & limits <b>↗</b></a></footer>
  </article>`;
}

function pending(id) {
  return `<article class="evidence-panel pending"><span class="tag">ANALYSIS IN PROGRESS</span><p>Result <code>${esc(id)}</code> has not been generated yet. Run the analysis and rebuild.</p></article>`;
}

export async function initEvidence() {
  const nodes = [...document.querySelectorAll('[data-evidence]')];
  await Promise.all(nodes.map(async node => {
    const id = node.dataset.evidence;
    try {
      const [result, display] = await Promise.all([loadResult(id), loadDisplay()]);
      node.innerHTML = renderPanel(result, { charts: node.dataset.charts, variant: node.dataset.variant, maxCharts: +node.dataset.max || undefined, display });
      animate(node);
    } catch (e) { node.innerHTML = pending(id); }
  }));
}

function animate(node) {
  const io = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) { entry.target.classList.add('drawn'); io.unobserve(entry.target); }
  }), { threshold: 0.15 });
  node.querySelectorAll('.evidence-chart').forEach(c => io.observe(c));
}

// Aggregate partners and future-data plans from every analysis on a tab, merged with curated content.
const norm = s => String(s || '').toLowerCase().replace(/&/g, ' and ').replace(/[^a-z0-9]+/g, ' ').trim();
function matchesCurated(curated, dataName) {
  const dn = ` ${norm(dataName)} `;
  const keys = (curated.aliases || []).map(norm);
  const toks = norm(curated.name).split(' ').filter(t => t.length > 2 && !['the', 'and'].includes(t));
  if (keys.some(k => dn.includes(` ${k} `) || dn.includes(` ${k}`))) return true;
  return toks.length >= 2 ? dn.includes(` ${toks[0]} `) && dn.includes(` ${toks[1]} `) : toks.length === 1 && dn.includes(` ${toks[0]} `);
}
export async function initPartners() {
  const nodes = [...document.querySelectorAll('[data-partners]')];
  if (!nodes.length) return;
  const [index, curated] = await Promise.all([loadIndex(), readJSON('content/partners.json').catch(() => ({}))]);
  for (const node of nodes) {
    const tab = node.dataset.partners;
    const results = await Promise.all(index.analyses.filter(a => a.tab === tab || (a.tabs || []).includes(tab)).map(a => loadResult(a.id).catch(() => null)));
    const fromData = new Map();
    results.filter(Boolean).forEach(r => (r.partners || []).forEach(p => {
      const key = norm(p.name);
      if (!fromData.has(key)) fromData.set(key, { ...p, sources: [r.title] }); else fromData.get(key).sources.push(r.title);
    }));
    const used = new Set();
    const cards = (curated[tab] || []).map(c => {
      const hits = [...fromData.entries()].filter(([, p]) => matchesCurated(c, p.name));
      hits.forEach(([k]) => used.add(k));
      return { ...c, data: hits.length ? hits[0][1] : null };
    });
    const extras = [...fromData.entries()].filter(([k]) => !used.has(k)).map(([, p]) => p);
    node.innerHTML = cards.map(p => `<article class="partner-card"><div class="partner-top"><span class="micro">${esc(p.role || '')}</span>${p.data ? '<span class="tag cyan">IN OUR DATA</span>' : ''}</div><h4>${esc(p.name)}</h4><p>${esc(p.why || '')}</p>${p.ask ? `<p class="partner-ask"><b>Our ask</b> ${esc(p.ask)}</p>` : ''}${p.data?.evidence ? `<p class="partner-evidence"><b>Evidence</b> ${esc(p.data.evidence)}</p>` : ''}</article>`).join('')
      + (extras.length ? `<div class="partner-extras"><span class="micro">ALSO NAMED BY OUR DATA · ${extras.length}</span><div>${extras.map(p => `<span class="partner-chip" title="${esc((p.why || '') + (p.evidence ? ' — ' + p.evidence : ''))}">${esc(p.name.length > 60 ? p.name.slice(0, 58) + '…' : p.name)}</span>`).join('')}</div></div>` : '');
  }
}

export async function initFuture() {
  const nodes = [...document.querySelectorAll('[data-future]')];
  if (!nodes.length) return;
  const index = await loadIndex();
  for (const node of nodes) {
    const tab = node.dataset.future;
    const results = (await Promise.all(index.analyses.filter(a => a.tab === tab || (a.tabs || []).includes(tab)).map(a => loadResult(a.id).catch(() => null)))).filter(Boolean);
    const items = results.flatMap(r => (r.future_big_data || []).slice(0, 3).map(text => ({ text, id: r.id, title: r.title })));
    if (!items.length) continue;
    node.innerHTML = items.map((it, i) => `<li><span class="micro">${String(i + 1).padStart(2, '0')} / FROM ${esc(it.title.toUpperCase())}</span><p>${esc(it.text)}</p></li>`).join('');
  }
}

// Totals shown in data bands: bytes, records, CPU-hours and jobs across all analyses.
export async function initTotals() {
  const nodes = [...document.querySelectorAll('[data-bigdata-total]')];
  if (!nodes.length) return;
  const index = await loadIndex();
  const t = index.totals || {};
  nodes.forEach(n => {
    const k = n.dataset.bigdataTotal;
    const v = t[k];
    n.textContent = k === 'bytes' ? formatBytes(v) : k === 'cpu_hours' ? (v ? (+v).toFixed(v < 10 ? 1 : 0) : '—') : formatCount(v);
  });
}

// Appendix: full method cards for every analysis.
export async function initAppendix() {
  const target = document.querySelector('#appendix-analyses');
  if (!target) return;
  const index = await loadIndex();
  const stack = document.querySelector('#dataset-stack');
  if (stack && index.datasets?.length) {
    const rows = index.datasets.filter(d => d.scope !== 'inventoried' && d.bytes > 0).slice(0, 12);
    const short = n => n.replace(/\s*\(.*?\)\s*/g, ' ').replace(/,.*$/, '').trim().slice(0, 34);
    stack.innerHTML = renderChart({ kind: 'hbar', title: 'What went in', subtitle: 'BYTES PROCESSED PER PUBLIC DATASET · LOG SCALE', x: { label: 'Size', unit: 'bytes', scale: 'log' }, series: [{ name: '', color: 'orange', points: rows.map(d => [short(d.name), d.bytes]) }], caption: 'The largest datasets each analysis downloaded or streamed and parsed. The 30.3 TB NASA PSI archive was catalogued object by object and is not counted here.' });
    stack.querySelector('.evidence-chart')?.classList.add('drawn');
  }
  const results = (await Promise.all(index.analyses.map(a => loadResult(a.id).then(r => ({ ...r, _doc: a.doc, _review: a.review })).catch(() => null)))).filter(Boolean);
  const order = { materials: 0, foundry: 1, network: 2 };
  results.sort((a, b) => (order[a.tab] ?? 9) - (order[b.tab] ?? 9));
  const tabName = { materials: '01 Materials', foundry: '02 Foundry', network: '03 Network' };
  target.innerHTML = results.map(r => {
    const c = r.compute || {};
    return `<section class="appendix-card" id="${esc(r.id)}"><header><span class="micro">${esc(tabName[r.tab] || r.tab)}${r.material ? ' · ' + esc(r.material) : ''} · ${esc(r.evidence_level || '')}</span><h3>${esc(r.title)}</h3><p>${esc(r.question || '')}</p></header>
      <div class="appendix-grid">
        <div><h4>Data</h4><table class="appendix-table"><thead><tr><th>Dataset</th><th>Records</th><th>Size</th><th>Accessed</th></tr></thead><tbody>${(r.datasets || []).map(d => `<tr><td>${d.url ? `<a href="${esc(d.url)}">${esc(d.name)} ↗</a>` : esc(d.name)}${d.license ? `<small>${esc(d.license)}</small>` : ''}${d.notes ? `<small>${esc(d.notes)}</small>` : ''}</td><td>${formatCount(+d.records)}</td><td>${formatBytes(+d.bytes)}${d.scope === 'inventoried' ? '<small>listed, not downloaded</small>' : ''}</td><td>${esc(d.accessed || '')}</td></tr>`).join('')}</tbody></table>
        <h4>Compute</h4><p class="appendix-compute">${esc(c.where || '—')} · ${(c.partitions || []).map(esc).join(', ') || '—'} · ${c.cpu_hours ? (+c.cpu_hours).toFixed(1) + ' CPU-h' : '—'} · ${c.wall_minutes ? Math.round(c.wall_minutes) + ' min wall' : ''}${c.peak_storage_gb ? ' · ' + (+c.peak_storage_gb).toFixed(0) + ' GB peak storage' : ''}${c.job_ids?.length ? `<br><span class="micro">Slurm jobs: ${c.job_ids.map(esc).join(', ')}</span>` : ''}</p></div>
        <div><h4>Method</h4><ol>${(r.method || []).map(m => `<li>${esc(m)}</li>`).join('')}</ol>
        <h4>What it does not show</h4><ul>${(r.limitations || []).map(m => `<li>${esc(m)}</li>`).join('')}</ul></div>
      </div>
      ${(r.charts || []).length ? `<details class="appendix-charts" open><summary>All ${r.charts.length} charts, full captions <span>+</span></summary><div class="evidence-charts n2">${r.charts.map(renderChart).join('')}</div></details>` : ''}
      ${(r.findings || []).length ? `<h4 class="appendix-sub">Findings</h4><ul class="appendix-findings">${r.findings.map(f => `<li>${esc(f)}</li>`).join('')}</ul>` : ''}
      ${r._review ? `<div class="grok-review"><span class="micro">INDEPENDENT REVIEW · ${esc(r._review.model || 'Grok')} · ${esc((r._review.reviewed_at || '').slice(0, 10))}</span><p><b>${esc((r._review.verdict || '').replace(/_/g, ' '))}</b> ${esc(r._review.judge_summary || '')}</p>${(r._review.overclaim_flags || []).length ? `<ul>${r._review.overclaim_flags.map(f => `<li>${esc(f)}</li>`).join('')}</ul>` : ''}</div>` : ''}
      <details><summary>Reproduce & code <span>+</span></summary><pre>${(r.reproduce || []).map(esc).join('\n')}</pre><p>${(r.code || []).map(p => `<a href="https://github.com/fvrarturo/spacexai-calhacks-13/blob/main/${esc(p)}">${esc(p)} ↗</a>`).join(' · ')}</p>${r._doc ? `<p><a href="${esc(r._doc)}">Full methods note ↗</a></p>` : ''}</details>
    </section>`;
  }).join('');
  // Reference page: show every chart immediately, no draw-on-scroll.
  target.querySelectorAll('.evidence-chart').forEach(c => c.classList.add('drawn'));
}

// Home-page headline cards: one number per tab, read from the result files.
export async function initHeadlines() {
  const nodes = [...document.querySelectorAll('[data-headline]')];
  await Promise.all(nodes.map(async node => {
    try {
      const r = await loadResult(node.dataset.headline);
      const h = r.headline || {};
      const longUnit = String(h.unit ?? '').length > 6;
      node.querySelector('strong').innerHTML = `${esc(h.value ?? '')}${longUnit ? '' : `<span>${esc(h.unit ?? '')}</span>`}`;
      if (longUnit) node.querySelector('strong').insertAdjacentHTML('afterend', `<em class="unit-long">${esc(h.unit)}</em>`);
      node.querySelector('p').textContent = h.text || r.title;
    } catch { node.querySelector('p').textContent = 'Analysis in progress.'; }
  }));
}

// Gallery of real NASA PSI frames with our measured spacing (thumbnails made by the psi analysis).
export async function initGallery() {
  const nodes = [...document.querySelectorAll('[data-gallery]')];
  await Promise.all(nodes.map(async node => {
    try {
      const base = `results/bigdata/${node.dataset.gallery}/`;
      const thumbs = await readJSON(base + 'thumbs.json');
      const pick = (node.dataset.files || '').split(',').map(s => s.trim()).filter(Boolean);
      const list = pick.length ? pick.map(f => thumbs.find(t => t.file === f)).filter(Boolean) : thumbs;
      node.innerHTML = list.map(t => {
        const rejected = /rejected/.test(t.file);
        return `<figure class="gallery-item ${rejected ? 'rejected' : ''}"><img src="${base}${esc(t.file)}" alt="${esc(t.label)} — ISS DECLIC-DSI frame with its radial power spectrum" loading="lazy" width="520" height="260"><figcaption><span class="micro">${esc(t.label.replace(/\s+/g, ' ').replace('um/s', 'µm/s'))}</span><strong>${rejected ? 'Rejected by the pattern gate' : `${Math.round(t.lambda_um)} µm cell spacing`}</strong></figcaption></figure>`;
      }).join('');
    } catch (e) { node.remove(); }
  }));
}
