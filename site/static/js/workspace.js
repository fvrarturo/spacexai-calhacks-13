import { $, esc, readJSON, failure } from './lib.js';
import { renderMaterials } from './workspace/materials.js';
import { renderCompatibility } from './workspace/compatibility.js';
import { renderFleet, renderSensitivity } from './workspace/fleet.js';
import { renderPlan } from './workspace/plan.js';

const jobs=[
  ['#pillars',async()=>{
    const data=await readJSON('content/workspace.json');
    $('#pillars').innerHTML=data.pillars.map(p=>`<article class="pillar"><span class="num">${esc(p.number)}</span><h3>${esc(p.name)}</h3><p>${esc(p.claim)}</p><p class="artifact">${esc(p.artifact)}</p><a href="#${p.id}">${esc(p.status)} ↗</a></article>`).join('');
    renderPlan(data);
    $('#data-pipeline').innerHTML=data.dataPlan.map((p,i)=>`<article><b>0${i+1}</b><h3>${esc(p.step)}</h3><p>${esc(p.action)}</p><small>${esc(p.scale)}</small></article>`).join('');
  }],
  ['#materials-result',async()=>renderMaterials(await readJSON('results/materials.json'))],
  ['#compatibility-result',async()=>renderCompatibility(await readJSON('content/compatibility.json'))],
  ['#hardware-result',async()=>{
    const data=await readJSON('results/foundry.json'),panel=document.createElement('div');panel.className='hardware-evidence';
    panel.innerHTML=`<span class="badge published">PUBLISHED HARDWARE PRECEDENT</span><h3>Shared services already support different payloads.</h3><div class="metric-strip"><div><strong>${data.positions}</strong><span>EXPRESS payload positions</span></div><div><strong>${data.rack_power_w/1000} kW</strong><span>published rack power</span></div><div><strong>${data.position_power_w} W</strong><span>individual position limit</span></div></div><p>At the individual maximum, ten positions would request ${data.all_positions_max_w/1000} kW. The published ${data.rack_power_w/1000} kW budget allows at most <strong>${data.simultaneous_full_power_upper_bound} simultaneous 500 W loads</strong> in this simplified power-only calculation. The table also lists ${data.water_cooled_positions} water-cooled positions.</p><p>${esc(data.inference)} ${esc(data.boundary)}</p><div class="download-row"><a href="${esc(data.source)}" target="_blank" rel="noopener noreferrer">NASA resource table · printed p. 13 ↗</a><a href="${esc(data.specialized_precedent.source)}" target="_blank" rel="noopener noreferrer">MSRR interchangeable furnace precedent ↗</a><a href="results/foundry.json" download>Download inputs & calculation ↓</a></div></div>`;
    $('#hardware-result').replaceChildren(panel);
  }],
  ['#fleet-results',async()=>renderFleet(await readJSON('results/fleet.json'))],
  ['#sensitivity-results',async()=>renderSensitivity(await readJSON('results/sensitivity.json'))],
  ['#cluster-result',async()=>{
    const data=await readJSON('results/engaging.json');
    $('#cluster-result').innerHTML=`<div class="pilot-card cluster-proof"><span class="field-label">ENGAGING / COMPLETED REPRODUCTION</span><h3>${data.tasks_completed} of ${data.scenarios} scenarios completed successfully.</h3><p>${data.scenarios*data.seeds_per_scenario*data.policies_per_seed} policy simulations. ${data.all_outputs_byte_identical?'Every result file is byte-for-byte identical to the local run.':'See the verification record for comparison details.'} Array ${esc(data.array_job_id)} used at most ${data.concurrency_limit} one-CPU tasks concurrently.</p><div class="download-row"><a href="results/engaging.json" download>Job provenance & result hashes ↓</a></div></div>`;
  }],
  ['#pilot-result',async()=>{
    const data=await readJSON('results/dsi-qc.json');
    $('#pilot-result').innerHTML=`<div class="pilot-card"><span class="field-label">REAL NASA FILES / DESCRIPTIVE QC ONLY</span><h3>${data.count} images verified · ${(data.bytes/1e6).toFixed(1)} MB processed</h3><p>Checksums, dimensions, intensity and image-gradient diagnostics are recorded for a bounded DSI pilot. This is pipeline verification, not a materials-performance result.</p><p class="footnote">${esc(data.selection)}</p><div class="download-row"><a href="results/dsi-qc.json" download>Download per-image QC & provenance ↓</a><a href="https://registry.opendata.aws/nasa-psi/" target="_blank" rel="noopener noreferrer">NASA public-data registry ↗</a></div></div>`;
  }]
];
await Promise.all(jobs.map(async([target,run])=>{try {await run();} catch(error) {failure(target,error);}}));
const nav=document.querySelectorAll('.sidebar nav a');
const observer=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting)nav.forEach(link=>{const active=link.hash==='#'+entry.target.id;link.classList.toggle('active',active);if(active)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});},{rootMargin:'-20% 0px -65% 0px'});
document.querySelectorAll('main>section[id]').forEach(s=>observer.observe(s));
