import { readJSON, esc } from '../lib.js';
import { drawSpecimen } from './visuals.js';

export async function initMaterials() {
  const dossiers = await readJSON('content/material-dossiers.json');
  const target = document.querySelector('#material-detail');
  const buttons = [...document.querySelectorAll('[data-material]')];
  function select(id) {
    const m = dossiers.find(m => m.id === id) || dossiers[0];
    buttons.forEach(b => b.setAttribute('aria-pressed',String(b.dataset.material===m.id)));
    target.style.setProperty('--material-color',m.color);
    target.innerHTML = `<div class="specimen-panel"><div class="specimen-top"><span class="micro">SPECIMEN / ${m.number}</span><span class="micro">${esc(m.application)}</span></div><canvas class="specimen-canvas" role="img" aria-label="Conceptual structure illustration for ${esc(m.title)}"></canvas><div class="specimen-bottom"><span>STRUCTURE STUDY</span><span>ILLUSTRATIVE / NOT MICROSCOPY</span></div><div class="specimen-metrics"><div><small>WHAT WE MEASURE</small><span>${esc(m.metric)}</span></div><div><small>KEY CONSTRAINT</small><span>${esc(m.constraint)}</span></div></div></div><div class="material-narrative"><span class="tag">${esc(m.status)}</span><h3>${esc(m.title)}</h3><p class="material-subtitle">${esc(m.subtitle)}</p><p>${esc(m.opportunity)}</p><dl><div><dt>THE EVIDENCE</dt><dd>${esc(m.evidence)}</dd></div><div><dt>OUR NEXT TEST</dt><dd>${esc(m.test)}</dd></div><div><dt>INSIDE THE FOUNDRY</dt><dd>${esc(m.hardware)}</dd></div></dl><div class="material-sources"><a href="${esc(m.source)}">${esc(m.sourceLabel)} ↗</a>${m.secondSource?`<a href="${esc(m.secondSource)}">${esc(m.secondSourceLabel)} ↗</a>`:''}</div></div>`;
    drawSpecimen(target.querySelector('canvas'),m.visual,m.color);
  }
  buttons.forEach(button => button.addEventListener('click',()=>select(button.dataset.material)));
  select('protein');
}

export async function initMeasurement() {
  const result = await readJSON('results/materials.json');
  const input = document.querySelector('#concentration');
  function render() {
    const row = result.rows.find(r=>r.concentration_mg_ml===+input.value);
    document.querySelector('#effect-stat').innerHTML=`${row.relative_reduction_pct.toFixed(1)}<span>%</span>`;
    document.querySelector('#measurement-context').textContent=`At ${row.concentration_mg_ml} mg/ml, using the values in Table 1.`;
    const max = 8;
    document.querySelector('#viscosity-chart').innerHTML = [
      ['Earth control',row.earth,row.earth_reported_spread,'earth'],
      ['Flight suspension',row.flight,row.flight_reported_spread,'flight']
    ].map(([name,value,spread,kind])=>`<div class="data-bar ${kind}"><div class="bar-label"><span>${name}</span><strong>${value.toFixed(2)} <small>± ${spread.toFixed(2)} cP</small></strong></div><div class="bar-track"><span class="bar-fill" style="width:${value/max*100}%"></span><span class="bar-whisker" style="left:${(value-spread)/max*100}%;width:${spread*2/max*100}%"></span></div></div>`).join('')+'<div class="chart-axis"><span>0</span><span>2</span><span>4</span><span>6</span><span>8 cP</span></div>';
  }
  input.addEventListener('change',render);render();
}
