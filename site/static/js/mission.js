import { initAtmosphere, initParticles, initLattice, initNetwork, setMotion } from './mission/visuals.js';
import { initMaterials, initMeasurement } from './mission/materials.js';
import { initArchitecture, initConcurrency } from './mission/foundry.js';
import { initFleet } from './mission/fleet.js';
import { initEvidence, initPartners, initFuture, initTotals, initAppendix, initHeadlines, initGallery } from './mission/evidence.js';

const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
const toggle = document.querySelector('#motion-toggle');
let paused = reduceMotion.matches;
try { paused ||= localStorage.getItem('orbital-motion-paused') === 'true'; } catch {}
function applyMotion() {
  document.documentElement.classList.toggle('motion-paused', paused);
  toggle.setAttribute('aria-pressed', String(paused));
  toggle.setAttribute('aria-label', paused ? 'Resume visual effects' : 'Pause visual effects');
  toggle.title = paused ? 'Resume visual effects' : 'Pause visual effects';
  toggle.firstElementChild.textContent = paused ? '▷' : 'Ⅱ';
  setMotion(!paused);
}
toggle.addEventListener('click', () => {
  paused = !paused;
  try { localStorage.setItem('orbital-motion-paused', String(paused)); } catch {}
  applyMotion();
});
reduceMotion.addEventListener('change', e => { paused = e.matches; applyMotion(); });
applyMotion();

// A single observer animates entrances without hiding narrative on script failure.
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => { if(entry.isIntersecting) { entry.target.classList.add('is-visible'); observer.unobserve(entry.target); } });
}, {threshold: .08});
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
document.documentElement.classList.add('motion-ready');
let scrollPending = false;
function updateScroll() {
  const range = document.documentElement.scrollHeight - innerHeight;
  const progress = range > 0 ? scrollY / range : 0;
  document.querySelector('.scroll-progress').style.width = `${Math.min(100, progress * 100)}%`;
  if(!paused) {
    document.querySelector('.vapor-blue').style.transform = `translate(${Math.sin(progress * 8) * 60}px, ${-progress * 420}px)`;
    document.querySelector('.vapor-amber').style.transform = `translate(${Math.cos(progress * 7) * 50}px, ${-progress * 550}px)`;
  }
  scrollPending = false;
}
addEventListener('scroll', () => { if(!scrollPending) { scrollPending = true; requestAnimationFrame(updateScroll); } }, {passive:true});
updateScroll();
initAtmosphere();
document.querySelectorAll('[data-particles]').forEach(initParticles);
initLattice(document.querySelector('#lattice-canvas'));
initNetwork(document.querySelector('#network-canvas'));

const safe = async (selector, task) => {
  const target = document.querySelector(selector);
  if(!target) return;
  try { await task(); } catch(error) {
    console.error(error);
    const message = document.createElement('p'); message.className = 'load-error';
    message.append('This interactive view could not load. ');
    const link = document.createElement('a'); link.href='research.html'; link.textContent='Open the research desk';
    message.append(link); target.replaceChildren(message);
  }
};
safe('#material-detail', initMaterials);
safe('#viscosity-chart', initMeasurement);
safe('#architecture-diagram', initArchitecture);
safe('#concurrency-output', initConcurrency);
safe('#fleet-bars', initFleet);
initEvidence();
initPartners().catch(console.error);
initFuture().catch(console.error);
initTotals().catch(console.error);
initAppendix().catch(console.error);
initHeadlines().catch(console.error);
initGallery().catch(console.error);

document.querySelectorAll('.share-matrix td').forEach(cell => {
  const level = cell.textContent.trim(); cell.dataset.level = level;
  const label = {S:'Shared service',B:'Budget or schedule required',I:'Dedicated or isolated'}[level];
  const dot = document.createElement('span');dot.textContent=level;dot.title=label;dot.setAttribute('aria-label',label);cell.replaceChildren(dot);
});
