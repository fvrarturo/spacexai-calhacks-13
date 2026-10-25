import { $, esc } from '../lib.js';
export function renderPlan(data) {
  const allTasks=data.phases.flatMap(p=>p.tasks),byId=Object.fromEntries(allTasks.map(t=>[t.id,t]));
  let filter='all';
  const render=()=>{
    let count=0;
    $('#roadmap-content').innerHTML=data.phases.map(phase=>{
      const tasks=phase.tasks.filter(t=>filter==='all'||(t.status===filter && (filter!=='next'||t.depends.every(id=>byId[id].status==='done'))));count+=tasks.length;
      if(!tasks.length)return '';
      return `<article class="phase"><div class="phase-heading"><h3>${esc(phase.label)}</h3><p>Exit criterion: ${esc(phase.exit)}</p></div>${tasks.map(t=>`<div class="task"><span class="task-status ${t.status}">${esc(t.status.replace('-',' '))}</span><div><h4>${esc(t.title)}</h4><p>${esc(t.deliverable)}</p>${t.depends.length?`<small>Depends on: ${t.depends.map(id=>esc(byId[id].title)).join('; ')}</small>`:''}</div><span class="task-owner">${esc(t.owner)}</span></div>`).join('')}</article>`;
    }).join('') || '<p>No tasks match this filter.</p>';
    $('#task-count').textContent=`${count} of ${allTasks.length} tasks`;
  };
  document.querySelectorAll('[data-task-filter]').forEach(button=>button.addEventListener('click',()=>{
    filter=button.dataset.taskFilter;
    document.querySelectorAll('[data-task-filter]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});render();
  }));render();
  const notes=$('#team-notes'),key='orbital-foundry:research-notes:v1';
  try { notes.value=localStorage.getItem(key)||''; } catch { $('#notes-status').textContent='Browser storage unavailable; export notes to keep them.'; }
  notes.addEventListener('input',()=>{try {localStorage.setItem(key,notes.value);$('#notes-status').textContent='Saved in this browser.';} catch {$('#notes-status').textContent='Could not save locally. Export your notes.';}});
  $('#export-notes').addEventListener('click',()=>{
    const blob=new Blob([`# Orbital Foundry — working notes\n\n${notes.value}\n`],{type:'text/markdown'});
    const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='orbital-foundry-notes.md';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  });
}
