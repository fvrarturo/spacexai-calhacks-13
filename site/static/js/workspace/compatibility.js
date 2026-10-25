import { $, esc } from '../lib.js';
export function evaluatePair(a,b,{power,heat,imagers,stagger}) {
  const imaging=stagger?Math.max(a.imagers,b.imagers):a.imagers+b.imagers;
  const disturbance=(a.vibration==='active'&&b.vibration==='quiet')||(b.vibration==='active'&&a.vibration==='quiet');
  const checks=[
    {label:`Power: ${a.power_w+b.power_w} / ${power} W`,pass:a.power_w+b.power_w<=power},
    {label:`Heat: ${a.heat_w+b.heat_w} / ${heat} W`,pass:a.heat_w+b.heat_w<=heat},
    {label:`Imagers: ${imaging} / ${imagers}${stagger?' · staggered':''}`,pass:imaging<=imagers},
    {label:disturbance?'Mixing / quiet-growth conflict':'No modeled mixing / quiet-growth conflict',pass:!disturbance}
  ];
  return {checks,pass:checks.every(c=>c.pass)};
}
export function renderCompatibility(data) {
  $('#shared-layers').innerHTML=data.layers.map(l=>`<article class="layer"><span class="state">${esc(l.state)}</span><h3>${esc(l.name)}</h3><p>${esc(l.detail)}</p></article>`).join('');
  const options=data.processes.map(p=>`<option value="${p.id}">${esc(p.name)}</option>`).join('');
  $('#process-a').innerHTML=options;$('#process-b').innerHTML=options;$('#process-b').value='mof';
  $('#compatibility-limit').textContent=data.limits;
  const map=document.createElement('div');map.id='compatibility-map';map.className='table-scroll';
  $('#compatibility-limit').before(map);
  const render=()=>{
    const a=data.processes.find(p=>p.id===$('#process-a').value),b=data.processes.find(p=>p.id===$('#process-b').value);
    const power=+$('#power-budget').value,heat=+$('#heat-budget').value,stagger=$('#stagger-imaging').checked;
    $('#power-output').textContent=power+' W';$('#heat-output').textContent=heat+' W';
    const result=evaluatePair(a,b,{power,heat,imagers:data.capacity.imagers,stagger});
    map.innerHTML=`<table class="pair-map"><caption>All process pairs under the current budgets. Select a cell to inspect the pair. Every candidate still requires isolated cartridges and validation.</caption><thead><tr><th scope="col">Process stage</th>${data.processes.map(p=>`<th scope="col">${esc(p.name.split(' ')[0])}</th>`).join('')}</tr></thead><tbody>${data.processes.map(left=>`<tr><th scope="row">${esc(left.name)}</th>${data.processes.map(right=>{const pair=evaluatePair(left,right,{power,heat,imagers:data.capacity.imagers,stagger});return `<td><button class="pair-cell ${pair.pass?'candidate':'sequence'}" data-left="${left.id}" data-right="${right.id}" aria-label="${esc(left.name)} and ${esc(right.name)}: ${pair.pass?'candidate':'sequence stages'}">${pair.pass?'C':'S'}</button></td>`;}).join('')}</tr>`).join('')}</tbody></table><p class="footnote">C = candidate under illustrative constraints. S = sequence or add independently qualified resources. Diagonal = two cartridges running the same stage.</p>`;
    $('#compatibility-result').innerHTML=`<div class="compatibility-verdict ${result.pass?'':'hold'}"><h4>${result.pass?'Candidate for concurrent operation':'Separate the operating windows'}</h4><p>${result.pass?'Passes this illustrative screen. Validate real stage loads, isolation, timing and fault behavior before claiming compatibility.':'At least one modeled constraint fails. Sequence the stages or provide independently qualified resources and disturbance isolation.'}</p><ul class="constraint-list">${result.checks.map(c=>`<li class="${c.pass?'':'fail'}">${c.pass?'✓':'!'} ${esc(c.label)}</li>`).join('')}</ul></div><p class="footnote"><strong>Dedicated internals:</strong> ${esc(a.module)}; ${esc(b.module)}.${stagger?' Staggering assumes each observation fits a separate window; cadence and missed-transient risks still need validation.':''}</p>`;
  };
  map.addEventListener('click',event=>{const button=event.target.closest('[data-left]');if(!button)return;$('#process-a').value=button.dataset.left;$('#process-b').value=button.dataset.right;render();$('#process-a').focus();});
  ['#process-a','#process-b','#power-budget','#heat-budget','#stagger-imaging'].forEach(id=>$(id).addEventListener('input',render));render();
}
