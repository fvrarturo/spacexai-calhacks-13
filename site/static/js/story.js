
import { storyData as D } from './content.js';
const $=(s,root=document)=>root.querySelector(s);
const $$=(s,root=document)=>[...root.querySelectorAll(s)];
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const sourceMap=Object.fromEntries(D.sources.map((s,i)=>[s[0],{id:s[0],title:s[1],type:s[2],url:s[3],n:i+1}]));
const cite=id=>{const s=sourceMap[id];return s?'<a class="cite" href="#source-'+s.id+'" title="'+esc(s.title)+'" aria-label="Source '+s.n+': '+esc(s.title)+'">['+String(s.n).padStart(2,'0')+']</a>':''};
function populateCites(root=document){$$('[data-cite]',root).forEach(el=>{el.innerHTML=el.dataset.cite.split(',').map(cite).join('')})}
function art(type,color){
 let shapes='';
 if(type==='protein'){
  [[40,45],[68,35],[93,48],[32,75],[61,64],[89,78],[53,94],[82,105]].forEach(([x,y],i)=>{shapes+='<path d="M'+x+','+(y-13)+' l12,7 v14 l-12,7 -12,-7 v-14z" fill="'+color+'" fill-opacity="'+(.23+i*.07)+'" stroke="'+color+'" stroke-width="1"/>'});
 }else if(type==='crystal'){
  shapes='<path d="M64 10 110 49 98 108 49 128 18 72 30 25Z" fill="'+color+'" fill-opacity=".18" stroke="'+color+'" stroke-width="2"/><path d="M64 10 70 64 110 49M70 64 98 108M70 64 49 128M70 64 18 72M70 64 30 25" fill="none" stroke="'+color+'" stroke-width="1.5"/>';
 }else if(type==='thermal'){
  shapes='<rect x="20" y="20" width="90" height="100" rx="12" fill="'+color+'" fill-opacity=".15" stroke="'+color+'"/><path d="m22 75 18-12 19 16 14-30 20 17 15-12M40 63 45 22M59 79 51 118M73 49 85 22M93 66 105 114" fill="none" stroke="'+color+'" stroke-width="2"/><path d="M6 39v50m-5-7 5 7 5-7M124 98V47m-5 7 5-7 5 7" fill="none" stroke="#6c858d"/>';
 }else if(type==='membrane'){
  shapes='<path d="M12 45 84 16 118 44 47 77Z" fill="'+color+'" fill-opacity=".2" stroke="'+color+'"/><path d="M12 45v40l35 31 71-31V44M47 77v39" fill="none" stroke="'+color+'" stroke-width="2"/>';
  [[39,44],[60,36],[79,28],[53,56],[74,47],[93,40]].forEach(([x,y])=>shapes+='<ellipse cx="'+x+'" cy="'+y+'" rx="6" ry="3" fill="'+color+'"/>');
 }else if(type==='bijel'){
  shapes='<path d="M5 35C40 0 36 65 72 47S100 13 130 44M0 93C35 58 45 119 77 88S109 66 135 99M28 25C4 60 73 53 46 91S55 131 94 114" fill="none" stroke="'+color+'" stroke-width="10" stroke-linecap="round"/><path d="M0 61C28 32 45 91 76 66S105 38 135 68M12 116C32 88 49 138 79 113S115 89 135 122" fill="none" stroke="#94b9aa" stroke-width="8" stroke-linecap="round"/>';
 }else{
  for(let row=0;row<5;row++)for(let col=0;col<5;col++){let x=15+col*23+(row%2?10:0),y=24+row*22;shapes+='<circle cx="'+x+'" cy="'+y+'" r="9" fill="'+color+'" fill-opacity="'+(.25+row*.1)+'" stroke="'+color+'" stroke-width="1"/>'}
 }
 return '<svg viewBox="0 0 140 140" role="img" aria-label="Conceptual material structure illustration">'+shapes+'</svg>';
}
const tabs=$('#programTabs'), panels=$('#programPanels');
D.programs.forEach((p,i)=>{
 tabs.insertAdjacentHTML('beforeend','<button class="program-tab'+(!i?' active':'')+'" role="tab" id="tab-'+p.id+'" aria-controls="panel-'+p.id+'" aria-selected="'+(!i)+'" tabindex="'+(!i?'0':'-1')+'" style="--accent:'+p.color+'" data-program="'+p.id+'"><span class="tab-n">0'+(i+1)+'</span><span>'+esc(p.name)+'<small>'+esc(p.short)+'</small></span></button>');
 panels.insertAdjacentHTML('beforeend','<article class="program-panel" id="panel-'+p.id+'" role="tabpanel" aria-labelledby="tab-'+p.id+'"'+(i?' hidden':'')+'><div class="program-panel-top"><div><div class="program-org">'+esc(p.org)+'</div><h3>'+esc(p.headline)+'</h3><span class="grade">'+esc(p.grade)+'</span></div><div class="program-art">'+art(p.icon,p.color)+'</div></div><div class="program-body"><div class="plain-definition"><span class="micro">IN PLAIN ENGLISH</span><p>'+esc(p.plain)+'</p></div><p>'+esc(p.body)+'</p><p>'+esc(p.evidence)+'</p><div class="program-two-col"><div><h4>Earth application</h4><p>'+esc(p.application)+'</p></div><div><h4>Our proposed bridge</h4><p>'+esc(p.bridge)+'</p></div></div><div class="evidence-gate"><strong>The qualification gate</strong>'+esc(p.gate)+'</div><div class="program-controls">'+p.controls.map(t=>'<span>'+esc(t)+'</span>').join('')+'</div><div class="program-sources">Primary evidence '+p.sources.map(cite).join('')+'</div><details class="program-disclosure"><summary>Organization context</summary><p>'+esc(p.people)+'</p></details></div></article>');
});
function selectProgram(id,focus=false){
 $$('.program-tab').forEach(b=>{const active=b.dataset.program===id;b.classList.toggle('active',active);b.setAttribute('aria-selected',active);b.tabIndex=active?0:-1;if(active&&focus)b.focus()});
 $$('.program-panel').forEach(p=>p.hidden=p.id!=='panel-'+id);
}
tabs.addEventListener('click',e=>{const b=e.target.closest('[data-program]');if(b)selectProgram(b.dataset.program)});
tabs.addEventListener('keydown',e=>{
 if(!['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','Home','End'].includes(e.key))return;
 const i=D.programs.findIndex(p=>$('#tab-'+p.id).classList.contains('active'));
 let n=e.key==='Home'?0:e.key==='End'?D.programs.length-1:(i+(e.key==='ArrowDown'||e.key==='ArrowRight'?1:-1)+D.programs.length)%D.programs.length;
 e.preventDefault();selectProgram(D.programs[n].id,true);
});
const stageNames=['Prepare','Condition','Form','Observe','Preserve','Qualify'];
D.programs.forEach((p,i)=>$('#processMatrix').insertAdjacentHTML('beforeend','<tr><th scope="row">'+esc(p.name)+'</th>'+p.stages.map((s,j)=>'<td><button class="matrix-cell'+(!i&&!j?' active':'')+'" data-row="'+i+'" data-stage="'+j+'" aria-label="'+esc(p.name+', '+stageNames[j]+': '+s)+'" aria-pressed="'+(!i&&!j)+'"></button></td>').join('')+'</tr>'));
$('#processMatrix').addEventListener('click',e=>{const b=e.target.closest('.matrix-cell');if(!b)return;const p=D.programs[+b.dataset.row],j=+b.dataset.stage;$$('.matrix-cell').forEach(c=>{c.classList.toggle('active',c===b);c.setAttribute('aria-pressed',c===b)});$('#matrixInspector').innerHTML='<span class="micro">'+esc(p.name+' / '+stageNames[j])+'</span><p>'+esc(p.stages[j])+'</p>'});
function selectModule(i){
 const m=D.modules[i];$$('[data-module]').forEach(b=>{const on=+b.dataset.module===i;b.classList.toggle('active',on);b.setAttribute('aria-selected',on);b.id='module-tab-'+b.dataset.module});
 const detail=$('#moduleDetail');detail.setAttribute('role','tabpanel');detail.setAttribute('aria-labelledby','module-tab-'+i);
 detail.innerHTML='<span class="micro">'+esc(m.subtitle)+'</span><h3>'+esc(m.title)+'</h3><p>'+esc(m.body)+'</p><div class="module-tags">'+m.tags.map(t=>'<span>'+esc(t)+'</span>').join('')+'</div><p class="module-boundary">'+esc(m.boundary)+'</p>';
 $$('[data-layer]').forEach(g=>g.style.opacity=+g.dataset.layer===i?'1':'.42');
}
$$('[data-module]').forEach(b=>{b.setAttribute('aria-controls','moduleDetail');b.addEventListener('click',()=>selectModule(+b.dataset.module));b.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();const n=(+b.dataset.module+(e.key==='ArrowRight'?1:2))%3;selectModule(n);$('[data-module="'+n+'"]').focus()}})});
selectModule(0);
const scenarios={
 growth:[['Observation','A calibrated measurement indicates the growth pattern has moved outside its target band.'],['Decision','Check confidence, sensor validity and the permitted correction envelope.'],['Action','A validated controller changes the allowed process setting; the scheduler checks the new thermal load.'],['Record','Store the measurement, rule, command and outcome against this batch.']],
 target:[['Observation','The selected structural endpoint has been reached with adequate measurement confidence.'],['Decision','Check whether the target persists and all finish conditions are satisfied.'],['Action','Execute the material-specific preservation step and release shared resources.'],['Record','Record why processing ended; final functional acceptance still happens through qualification.']],
 fault:[['Observation','A sensor reading is missing, implausible or inconsistent with another measurement.'],['Decision','Treat the process state as uncertain. Do not infer physical safety from a language-model answer.'],['Action','Follow the predefined hold or safe-state procedure and notify the operator.'],['Record','Flag the batch for review and retain the complete fault history.']]
};
function selectScenario(key){$$('[data-scenario]').forEach(b=>{const on=b.dataset.scenario===key;b.classList.toggle('active',on);b.setAttribute('aria-pressed',on)});$('#scenarioDetail').innerHTML=scenarios[key].map(([a,b])=>'<div class="scenario-detail-line"><span>'+a+'</span><p>'+b+'</p></div>').join('')}
$$('[data-scenario]').forEach(b=>b.addEventListener('click',()=>selectScenario(b.dataset.scenario)));selectScenario('growth');
function costs(){const n=+$('#batchCount').value,q=+$('#yieldRate').value/100,dedicated=120/q,shared=(100/n+20)/q,saving=(1-shared/dedicated)*100;$('#batchOutput').value=n;$('#yieldOutput').value=Math.round(q*100)+'%';$('#dedicatedCost').textContent=dedicated.toFixed(1)+' u';$('#sharedCost').textContent=shared.toFixed(1)+' u';$('#dedicatedBar').style.width='100%';$('#sharedBar').style.width=(shared/dedicated*100)+'%';$('#savingPct').textContent=Math.round(saving)+'%';}
$('#batchCount').addEventListener('input',costs);$('#yieldRate').addEventListener('input',costs);costs();
let selectedDataset='dsi',datasetFilter='All';
function renderDatasets(){const arr=D.datasets.filter(d=>datasetFilter==='All'||d.family===datasetFilter);if(!arr.some(d=>d.id===selectedDataset))selectedDataset=arr[0]?.id;$('#datasetCount').textContent=arr.length+' INVESTIGATION'+(arr.length===1?'':'S');$('#datasetList').innerHTML=arr.map(d=>'<button class="dataset-row'+(d.id===selectedDataset?' active':'')+'" data-dataset="'+d.id+'" aria-pressed="'+(d.id===selectedDataset)+'"><span><strong>'+esc(d.name)+'</strong><small>'+esc(d.accession+' / '+d.family.toUpperCase())+'</small></span><span class="data-size">'+d.size+'<small>reported archive size</small></span></button>').join('');renderDatasetDetail();}
function renderDatasetDetail(){const d=D.datasets.find(x=>x.id===selectedDataset);if(!d)return;$('#datasetDetail').innerHTML='<span class="micro">'+esc(d.status)+'</span><h3>'+esc(d.name)+'</h3><p>'+esc(d.what)+'</p><dl><dt>Potential measurement</dt><dd>'+esc(d.measure)+'</dd><dt>Decision it could inform</dt><dd>'+esc(d.decision)+'</dd><dt>Inference boundary</dt><dd>'+esc(d.limit)+'</dd></dl><div class="access-state"><strong>Access check:</strong> '+esc(d.access)+'</div><a class="source-direct" href="'+sourceMap[d.source].url+'" target="_blank" rel="noopener noreferrer">Open NASA investigation ↗</a>';}
$('#datasetList').addEventListener('click',e=>{const b=e.target.closest('[data-dataset]');if(b){selectedDataset=b.dataset.dataset;renderDatasets()}});
$$('[data-filter]').forEach(b=>b.addEventListener('click',()=>{datasetFilter=b.dataset.filter;$$('[data-filter]').forEach(c=>{c.classList.toggle('active',c===b);c.setAttribute('aria-pressed',c===b)});renderDatasets()}));renderDatasets();
$('#sourceList').innerHTML=D.sources.map((s,i)=>'<article class="source-item" id="source-'+s[0]+'" data-search="'+esc((s[1]+' '+s[2]+' '+s[3]).toLowerCase())+'"><span class="source-index">'+String(i+1).padStart(2,'0')+'</span><div><a href="'+esc(s[3])+'" target="_blank" rel="noopener noreferrer">'+esc(s[1])+' ↗</a><small>'+esc(s[2])+'</small></div></article>').join('');
$('#sourceSearch').addEventListener('input',e=>{let n=0;const q=e.target.value.toLowerCase().trim();$$('.source-item').forEach(a=>{a.hidden=!a.dataset.search.includes(q);if(!a.hidden)n++});$('#sourceEmpty').hidden=n>0});
populateCites();
const sections=$$('section.story');let presenting=false,chapter=0;
function showChapter(n){chapter=Math.max(0,Math.min(sections.length-1,n));sections.forEach((s,i)=>s.classList.toggle('current',i===chapter));$('#presentationChapter').textContent=String(chapter+1).padStart(2,'0')+' / '+String(sections.length).padStart(2,'0');$('#presentationTitle').textContent=sections[chapter].dataset.title;$('#prevChapter').disabled=chapter===0;$('#nextChapter').disabled=chapter===sections.length-1;window.scrollTo({top:0,behavior:'instant'});}
function togglePresent(on){if(on&&!presenting){const probe=Math.min(innerHeight*.35,250);const current=sections.findIndex(s=>{const r=s.getBoundingClientRect();return r.top<=probe&&r.bottom>probe});if(current>=0)chapter=current}presenting=on;document.body.classList.toggle('presentation',on);$('#presentationControls').hidden=!on;$('#presentToggle').setAttribute('aria-pressed',on);$('#presentToggle').innerHTML=on?'Reading mode ↙':'Present <span aria-hidden="true">↗</span>';if(on){showChapter(chapter)}else{sections.forEach(s=>s.classList.remove('current'));sections[chapter].scrollIntoView({behavior:'instant',block:'start'})}}
$('#presentToggle').addEventListener('click',()=>togglePresent(!presenting));$('#exitPresentation').addEventListener('click',()=>togglePresent(false));$('#prevChapter').addEventListener('click',()=>showChapter(chapter-1));$('#nextChapter').addEventListener('click',()=>showChapter(chapter+1));
document.addEventListener('keydown',e=>{if(e.target.matches('input,textarea,select,[contenteditable=true]'))return;if(e.key.toLowerCase()==='p'){e.preventDefault();togglePresent(!presenting)}else if(presenting&&e.key==='Escape'){togglePresent(false)}else if(presenting&&['ArrowRight','PageDown'].includes(e.key)&&!e.target.closest('[role=tablist]')){e.preventDefault();showChapter(chapter+1)}else if(presenting&&['ArrowLeft','PageUp'].includes(e.key)&&!e.target.closest('[role=tablist]')){e.preventDefault();showChapter(chapter-1)}});
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(!a)return;const target=$(a.getAttribute('href'));if(!target)return;if(target.classList.contains('source-item')){$('#sourceSearch').value='';$$('.source-item').forEach(x=>x.hidden=false);$('#sourceEmpty').hidden=true}if(presenting){e.preventDefault();const section=target.closest('section.story');if(section){showChapter(sections.indexOf(section));requestAnimationFrame(()=>target.scrollIntoView({behavior:'instant',block:'start'}));history.replaceState(null,'',a.getAttribute('href'))}}});
const observer=new IntersectionObserver(entries=>{if(presenting)return;for(const e of entries)if(e.isIntersecting)chapter=sections.indexOf(e.target)},{rootMargin:'-15% 0px -65% 0px',threshold:0});sections.forEach(s=>observer.observe(s));
function progress(){if(presenting)return;const max=document.documentElement.scrollHeight-innerHeight;$('#readProgress').style.width=(max>0?scrollY/max*100:0)+'%'}window.addEventListener('scroll',progress,{passive:true});window.addEventListener('resize',progress);progress();
$('#copyPitch').addEventListener('click',async()=>{const text=$$('#pitchText p').map(p=>p.textContent).join('\n\n');let ok=false;try{if(navigator.clipboard){await navigator.clipboard.writeText(text);ok=true}}catch{}if(!ok){const t=document.createElement('textarea');t.value=text;t.style.cssText='position:fixed;left:-9999px';document.body.appendChild(t);t.select();try{ok=document.execCommand('copy')}catch{}t.remove()}$('#copyStatus').textContent=ok?'Pitch copied.':'Select the pitch text to copy it.';});
$('#printButton').addEventListener('click',()=>window.print());
window.addEventListener('beforeprint',()=>{document.body.classList.add('printing')});
window.addEventListener('afterprint',()=>document.body.classList.remove('printing'));
if(location.hash){requestAnimationFrame(()=>{const t=$(location.hash);if(t)t.scrollIntoView()})}