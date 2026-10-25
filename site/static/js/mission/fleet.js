import { readJSON } from '../lib.js';

export async function initFleet() {
  const data = await readJSON('results/sensitivity.json');
  const select = document.querySelector('#scenario-select');
  select.innerHTML = data.rows.map((r,i)=>`<option value="${i}">${r.config.jobs} jobs · ${r.config.setup_hours}h setup · ${r.config.cadence}h return · ${r.config.failure_rate*100}% failure</option>`).join('');
  // Start with a busy scenario so the page does not cherry-pick a coordination win.
  select.value = String(Math.max(0, data.rows.findIndex(r=>r.config.jobs===72 && r.config.setup_hours===2 && r.config.cadence===24 && r.config.failure_rate===.1)));
  const names = {fifo:'First in, first out',earliest_due:'Earliest due date',dedicated:'Dedicated capsules',coordinated:'Coordinated v0'};
  const pct = n => (n*100).toFixed(1);
  function render() {
    const row=data.rows[+select.value];
    document.querySelector('#scenario-facts').innerHTML = `<div><strong>${row.config.jobs}</strong><span>submitted jobs</span></div><div><strong>${row.config.setup_hours}<small>h</small></strong><span>changeover</span></div><div><strong>${row.config.cadence}<small>h</small></strong><span>return cadence</span></div><div><strong>${row.config.failure_rate*100}<small>%</small></strong><span>failure probability</span></div>`;
    document.querySelector('#fleet-bars').innerHTML = Object.entries(names).map(([key,label])=>{
      const r=row.policies[key];
      return `<div class="data-bar ${key==='coordinated'?'flight':''}"><div class="bar-label"><span>${label}</span><strong>${pct(r.mean)}<small>%</small></strong></div><div class="bar-track"><span class="bar-fill" style="width:${r.mean*100}%"></span><span class="bar-whisker" style="left:${r.low*100}%;width:${(r.high-r.low)*100}%"></span></div><span class="bar-interval">95% interval ${pct(r.low)}–${pct(r.high)}%</span></div>`;
    }).join('')+'<div class="chart-axis"><span>0</span><span>25</span><span>50</span><span>75</span><span>100%</span></div>';
    const delta=row.paired_on_time_delta.dedicated;
    const sign=delta.mean>=0?'+':'';
    const interpretation=delta.low>0?'Coordination beats dedicated operation in this modeled workload.':delta.high<0?'Dedicated operation beats coordination in this modeled workload.':'This comparison does not resolve a clear advantage over dedicated operation.';
    document.querySelector('#fleet-takeaway').innerHTML=`<div><span class="micro">COORDINATED − DEDICATED</span><strong>${sign}${pct(delta.mean)} <small>pp</small></strong></div><p>${interpretation}<span>Paired 95% interval: ${pct(delta.low)} to ${pct(delta.high)} percentage points. A simulation result, not a measured fleet benefit.</span></p>`;
  }
  select.addEventListener('change',render);render();
}
