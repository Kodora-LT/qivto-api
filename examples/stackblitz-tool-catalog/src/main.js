import './style.css';
const list=document.querySelector('ul'),status=document.querySelector('[data-status]'),search=document.querySelector('input');let tools=[];
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function render(){const q=search.value.toLowerCase().trim(),shown=tools.filter(t=>(t.name+' '+t.description).toLowerCase().includes(q));list.innerHTML=shown.map(t=>`<li><a href="https://qivto.com/en/tools/${encodeURIComponent(t.slug)}" target="_blank" rel="noopener"><strong>${escape(t.name)}</strong><span>${escape(t.description)}</span></a></li>`).join('');status.textContent=`${shown.length} tools`}
fetch('https://qivto.com/api/v1/tools?lang=en').then(r=>r.json()).then(data=>{tools=data.tools||[];render()}).catch(()=>status.textContent='Could not load the catalog.');search.addEventListener('input',render);
