// All visuals are illustrative. One throttled animation loop, visibility gating,
// bounded pixel density and a shared motion switch keep the experience lightweight.
let running = true, raf = 0, last = 0, clock = 0;
const scenes = new Set();
const TAU = Math.PI * 2;
const colors = {orange:'#ff945c',cyan:'#8bcedb',blue:'#486c8b'};
function frame(now) {
  raf = 0;
  if(!running || document.hidden) return;
  if(now-last>=32) {
    clock += Math.min((now-last)/1000,.05); last=now;
    for(const scene of scenes) {
      if(!scene.canvas.isConnected){scene.resize.disconnect();scene.visibility.disconnect();scenes.delete(scene);continue;}
      if(scene.visible) scene.draw(clock);
    }
  }
  if(scenes.size) raf = requestAnimationFrame(frame);
}
function start(){if(running&&!document.hidden&&!raf){last=performance.now();raf=requestAnimationFrame(frame);}}
export function setMotion(enabled){running=enabled;if(!enabled){cancelAnimationFrame(raf);raf=0;}else start();}
document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(raf);raf=0;}else start();});
function canvasScene(canvas, render) {
  if(!canvas) return;
  const ctx=canvas.getContext('2d'); if(!ctx) return;
  let width=0,height=0;
  const scene={canvas,visible:true,draw(t){if(width&&height){ctx.clearRect(0,0,width,height);render(ctx,width,height,t);}}};
  scene.resize=new ResizeObserver(()=>{
    const box=canvas.getBoundingClientRect();width=box.width;height=box.height;
    const ratio=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(width*ratio);canvas.height=Math.round(height*ratio);ctx.setTransform(ratio,0,0,ratio,0,0);scene.draw(clock);
  });scene.resize.observe(canvas);
  scene.visibility=new IntersectionObserver(([entry])=>{scene.visible=entry.isIntersecting; if(scene.visible)scene.draw(clock);});scene.visibility.observe(canvas);
  scenes.add(scene);start();
  return ()=>scene.draw(clock);
}
function seeded(n){const x=Math.sin(n*127.1+43.7)*43758.5453;return x-Math.floor(x);}
function line(ctx,x1,y1,x2,y2,color,width=1){ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.strokeStyle=color;ctx.lineWidth=width;ctx.stroke();}
function dot(ctx,x,y,r,color){ctx.beginPath();ctx.arc(x,y,r,0,TAU);ctx.fillStyle=color;ctx.fill();}
function project(x,y,z,angle,cx,cy,scale){const a=x*Math.cos(angle)+z*Math.sin(angle),b=z*Math.cos(angle)-x*Math.sin(angle);const yy=y*Math.cos(.38)-b*Math.sin(.38),zz=y*Math.sin(.38)+b*Math.cos(.38);const perspective=4/(4+zz);return {x:cx+a*scale*perspective,y:cy+yy*scale*perspective,z:zz,s:perspective};}

export function initAtmosphere(){
  canvasScene(document.querySelector('#ambient-field'),(ctx,w,h,t)=>{
    for(let i=0;i<72;i++){const x=seeded(i)*w,y=(seeded(i+100)*h-t*(2+seeded(i+200)*7))%h;dot(ctx,x,(y+h)%h,.5+seeded(i+300),`rgba(138,183,201,${.1+seeded(i+400)*.32})`);}
    // Faint upward wisps respond to scrolling; they are visual atmosphere only.
    const travel=scrollY*.075;
    for(let i=0;i<4;i++){
      const x=i%2?w-30:20,y=h-((t*11+travel+i*h*.26)% (h+200));
      const glow=ctx.createRadialGradient(x,y,0,x,y,140);glow.addColorStop(0,i%2?'rgba(211,130,72,.018)':'rgba(102,173,196,.025)');glow.addColorStop(1,'transparent');ctx.fillStyle=glow;ctx.fillRect(x-140,y-140,280,280);
    }
  });
}
export function initParticles(canvas){
  const earth=canvas.dataset.particles==='earth';
  canvasScene(canvas,(ctx,w,h,t)=>{
    const margin=12;ctx.strokeStyle='#374753';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(margin,20);ctx.lineTo(margin,h-10);ctx.lineTo(w-margin,h-10);ctx.lineTo(w-margin,20);ctx.stroke();
    for(let i=0;i<42;i++){
      let x=margin+14+seeded(i)*Math.max(1,w-2*margin-28),y;
      if(earth){y=30+((seeded(i+50)*(h-45)+t*(8+seeded(i+80)*6))%(h-45));x+=Math.sin(t*.6+i)*5;}
      else{y=25+seeded(i+50)*(h-55)+Math.sin(t*.4+i)*8;x+=Math.sin(t*.3+i*2)*8;}
      const size=2+seeded(i+120)*3;ctx.shadowBlur=8;ctx.shadowColor=earth?colors.orange:colors.cyan;dot(ctx,x,y,size,earth?'#dca47c':'#8bcedb');ctx.shadowBlur=0;
    }
    if(earth){for(let i=0;i<28;i++)dot(ctx,margin+6+seeded(i+600)*(w-2*margin-12),h-12-seeded(i+700)*15,2+seeded(i+800)*3,'#c9926f99');}
    ctx.font='8px monospace';ctx.fillStyle='#708695';ctx.fillText(earth?'SETTLING + CIRCULATION':'SUSPENDED ASSEMBLY',margin+8,12);
  });
}
function lattice(ctx,w,h,t,type='photonic',color=colors.cyan){
  const angle=t*.09+.4,cx=w*.5,cy=h*.49,scale=Math.min(w,h)*.26;
  const points=[];const size=type==='mof'?3:4;
  for(let x=0;x<size;x++)for(let y=0;y<size;y++)for(let z=0;z<size;z++){
    const divisor=(size-1)/2;
    const point=project((x-divisor)/divisor,(y-divisor)/divisor,(z-divisor)/divisor,angle,cx,cy,scale);
    points.push({...point,ix:x,iy:y,iz:z,id:`${x}-${y}-${z}`});
  }
  const lookup=new Map(points.map(p=>[p.id,p]));
  for(const p of points)for(const d of [[1,0,0],[0,1,0],[0,0,1]]){
    const q=lookup.get(`${p.ix+d[0]}-${p.iy+d[1]}-${p.iz+d[2]}`);
    if(q)line(ctx,p.x,p.y,q.x,q.y,type==='mof'?color+'90':'#6994a153',type==='mof'?2:1);
  }
  points.sort((a,b)=>b.z-a.z).forEach(p=>{
    const orange=(p.ix+p.iy+p.iz)%3===0;
    const r=(type==='mof'?4:6)*p.s;
    const glow=ctx.createRadialGradient(p.x-r*.3,p.y-r*.4,0,p.x,p.y,r);
    glow.addColorStop(0,orange?'#ffe2bd':'#d9f4f4');glow.addColorStop(.35,orange?colors.orange:color);glow.addColorStop(1,orange?'#6c3921':'#1f3c4e');
    ctx.globalAlpha=.55+(.5-p.z*.16)*.4;dot(ctx,p.x,p.y,r,glow);ctx.globalAlpha=1;
  });
  // A delicate crosshair and orbit of the instrument, not a data axis.
  ctx.strokeStyle='#516a7b44';ctx.lineWidth=.7;ctx.beginPath();ctx.ellipse(cx,cy,scale*1.7,scale*.57,-.25,0,TAU);ctx.stroke();
}
export function initLattice(canvas){canvasScene(canvas,(ctx,w,h,t)=>lattice(ctx,w,h,t,'photonic','#9dcbd6'));}
export function drawSpecimen(canvas,type,color){
  canvasScene(canvas,(ctx,w,h,t)=>{
    if(type==='mof'||type==='photonic'){lattice(ctx,w,h,t,type,color);return;}
    const cx=w/2,cy=h/2,scale=Math.min(w,h)*.27;
    if(type==='cooling'){
      for(let j=0;j<19;j++){
        const x=cx+(j-9)*12,y=cy+Math.sin(j*.8+t*.12)*16;
        ctx.beginPath();ctx.moveTo(x,y-85);ctx.lineTo(x+7,y-110);ctx.lineTo(x+11,y+70);ctx.lineTo(x+2,y+90);ctx.closePath();
        const g=ctx.createLinearGradient(x,0,x+11,0);g.addColorStop(0,'#513c31');g.addColorStop(.5,color);g.addColorStop(1,'#675341');ctx.fillStyle=g;ctx.fill();ctx.strokeStyle='#f9ce9d80';ctx.stroke();
      }
      const glow=ctx.createLinearGradient(0,cy-100,0,cy+100);glow.addColorStop(0,'#8bcedb00');glow.addColorStop(.5,'#8bcedb30');glow.addColorStop(1,'#ff945c00');ctx.fillStyle=glow;ctx.fillRect(cx-130,cy-130,260,260);return;
    }
    const seeds=type==='protein'?7:3;
    for(let n=0;n<seeds;n++){
      const offsets=type==='protein'?[Math.sin(n*2.3)*scale*.85,Math.cos(n*2.3)*scale*.7]:[(n-1)*scale*.75,Math.sin(n*3)*scale*.3];
      const a=t*.065+n*.7,s=scale*(type==='protein'?.28:.42),x=cx+offsets[0],y=cy+offsets[1];
      const vertices=[[-.65,-.7,-.4],[.65,-.7,-.4],[.65,.7,-.4],[-.65,.7,-.4],[-.65,-.7,.4],[.65,-.7,.4],[.65,.7,.4],[-.65,.7,.4]].map(([xx,yy,zz])=>project(xx,yy,zz,a,x,y,s));
      const faces=[[0,1,2,3],[4,5,6,7],[0,1,5,4],[1,2,6,5],[2,3,7,6],[3,0,4,7]].sort((a,b)=>b.reduce((s,i)=>s+vertices[i].z,0)-a.reduce((s,i)=>s+vertices[i].z,0));
      faces.forEach((face,i)=>{ctx.beginPath();face.forEach((index,j)=>{const p=vertices[index];if(j)ctx.lineTo(p.x,p.y);else ctx.moveTo(p.x,p.y);});ctx.closePath();ctx.fillStyle=color+['25','40','15','66','30','55'][i];ctx.fill();ctx.strokeStyle=color+'b0';ctx.lineWidth=.8;ctx.stroke();});
    }
    for(let i=0;i<20;i++){const x=cx+(seeded(i)-.5)*scale*3,y=cy+(seeded(i+30)-.5)*scale*2.8;dot(ctx,x,y,1,color+'66');}
  });
}

export function initNetwork(canvas){
  if(!canvas)return;let count=1;
  const descriptions={1:'One foundry proves a process and its return path. Concept illustration; no operating fleet is claimed.',3:'Three specialized foundries separate solution growth, thermal processing and particle assembly. Concept illustration, not a validated fleet design.',8:'A future network matches qualified capacity to demand and return windows. Additional capacity is an ambition, not a computed performance forecast.'};
  const redraw=canvasScene(canvas,(ctx,w,h,t)=>{
    const mobile=w<641;
    const r=mobile?Math.min(w*.34,145):Math.min(w*.21,290),cx=mobile?w*.5:w*.76,cy=mobile?h*.74:h*.53;
    for(let i=0;i<100;i++){dot(ctx,seeded(i+300)*w,seeded(i+400)*h,seeded(i+600)*1.1,'#8ca4bd66');}
    // The atmospheric limb and dark globe are drawn procedurally.
    const halo=ctx.createRadialGradient(cx,cy,r*.8,cx,cy,r*1.22);halo.addColorStop(0,'#18394f00');halo.addColorStop(.65,'#4c91b952');halo.addColorStop(1,'#18394f00');dot(ctx,cx,cy,r*1.22,halo);
    const earth=ctx.createRadialGradient(cx-r*.4,cy-r*.4,0,cx+r*.2,cy+r*.1,r*1.2);earth.addColorStop(0,'#183e52');earth.addColorStop(.55,'#0b2232');earth.addColorStop(1,'#03080e');dot(ctx,cx,cy,r,earth);
    ctx.save();ctx.beginPath();ctx.arc(cx,cy,r,0,TAU);ctx.clip();
    // Latitude/longitude mesh communicates a world-spanning system, not geography data.
    ctx.lineWidth=.6;ctx.strokeStyle='#59869938';
    for(let k=-3;k<=3;k++){ctx.beginPath();ctx.ellipse(cx,cy,r*Math.cos(k*.22),r*Math.abs(Math.sin(k*.22))+.1,0,0,TAU);ctx.stroke();}
    for(let k=-3;k<=3;k++){ctx.beginPath();ctx.ellipse(cx,cy,r*Math.abs(Math.sin(k*.23))+.1,r,0,0,TAU);ctx.stroke();}
    for(let i=0;i<800;i++){
      const lat=(seeded(i+900)-.5)*Math.PI,lon=seeded(i+1300)*TAU;
      const shape=Math.sin(lon*3+lat*2)+Math.cos(lat*7-lon*2)+Math.sin(lon*5+lat*4)*.5;
      if(shape<.5)continue;
      const zz=Math.cos(lat)*Math.cos(lon+t*.025);
      if(zz<0)continue;
      const x=cx+Math.cos(lat)*Math.sin(lon+t*.025)*r,y=cy+Math.sin(lat)*r;
      dot(ctx,x,y,.6+seeded(i+1700),`rgba(119,166,166,${.08+zz*.24})`);
    }
    const shade=ctx.createLinearGradient(cx-r,cy-r,cx+r,cy+r);shade.addColorStop(0,'#00000000');shade.addColorStop(.6,'#00000030');shade.addColorStop(1,'#000000c0');ctx.fillStyle=shade;ctx.fillRect(cx-r,cy-r,r*2,r*2);ctx.restore();
    ctx.strokeStyle='#76b9d27a';ctx.lineWidth=1;ctx.beginPath();ctx.arc(cx,cy,r,0,TAU);ctx.stroke();
    const nodes=[];
    for(let k=0;k<3;k++){
      const tilt=-.3+k*.42;ctx.save();ctx.translate(cx,cy);ctx.rotate(tilt);ctx.beginPath();ctx.ellipse(0,0,r*(1.38+k*.12),r*(.6+k*.1),0,0,TAU);ctx.strokeStyle=k===0?'#d79c6977':'#6d8d9b55';ctx.lineWidth=.7;ctx.setLineDash(k===2?[3,7]:[]);ctx.stroke();ctx.restore();
    }
    for(let i=0;i<count;i++){
      const group=i%3,tilt=-.3+group*.42,a=t*(.08+group*.013)+i*TAU/count-.8;
      const xx=Math.cos(a)*r*(1.38+group*.12),yy=Math.sin(a)*r*(.6+group*.1);
      nodes.push({x:cx+xx*Math.cos(tilt)-yy*Math.sin(tilt),y:cy+xx*Math.sin(tilt)+yy*Math.cos(tilt),group});
    }
    if(count>1)nodes.forEach((p,i)=>{const q=nodes[(i+1)%nodes.length];line(ctx,p.x,p.y,q.x,q.y,'#76abc52e',.7);});
    nodes.forEach((p,i)=>{
      const color=[colors.orange,colors.cyan,'#bccba1'][p.group];
      ctx.shadowColor=color;ctx.shadowBlur=10;dot(ctx,p.x,p.y,3,color);ctx.shadowBlur=0;
      ctx.fillStyle='#0b1720';ctx.strokeStyle=color;ctx.lineWidth=.8;ctx.fillRect(p.x-8,p.y-5,16,10);ctx.strokeRect(p.x-8,p.y-5,16,10);
      ctx.fillStyle='#294453';ctx.fillRect(p.x-20,p.y-3,10,6);ctx.fillRect(p.x+10,p.y-3,10,6);line(ctx,p.x-20,p.y,p.x+20,p.y,color,.5);
      ctx.font=`${mobile?7:8}px monospace`;ctx.fillStyle=color;ctx.fillText(`OF—${String(i+1).padStart(2,'0')}`,p.x+25,p.y+3);
    });
    if(!mobile){ctx.font='8px monospace';ctx.fillStyle='#87a1b6';ctx.fillText('EARTH / RESEARCH · FINISHING · QUALIFICATION',cx-r*.7,cy+r+75);}
  });
  document.querySelectorAll('[data-scale]').forEach(button=>button.addEventListener('click',()=>{
    count=+button.dataset.scale;document.querySelectorAll('[data-scale]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
    document.querySelector('#network-description').textContent=descriptions[count];redraw?.();
  }));
}
