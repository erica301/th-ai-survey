logo = open('logo.svg').read().strip()
# strip xml decl if present
logo = logo.replace('<?xml version="1.0" encoding="UTF-8"?>','').strip()

HTML = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Transform Health · AI check-in</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Space+Grotesk:wght@700&display=swap" rel="stylesheet">
<style>
:root{
  --blue:#3480DC; --deep:#24588A; --cyan:#00AAFF; --orange:#E45A30; --yellow:#FADF56;
  --ink:#333333; --muted:#6B7280; --line:#E4E4E4; --panel:#F7F9FC; --white:#fff;
}
*{box-sizing:border-box}
body{margin:0;background:var(--panel);color:var(--ink);
  font-family:Montserrat,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  font-weight:400;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:720px;margin:0 auto;padding:0 20px 100px}
header{background:var(--white);border-bottom:1px solid var(--line);padding:26px 0 24px;margin-bottom:26px}
header .wrap{padding-bottom:0}
.brandbar{display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.logo{max-width:190px;height:auto;display:block}
.logo svg{width:190px;height:auto;display:block}
.divider{width:1px;height:38px;background:var(--line);flex:none}
.la{font-family:'Space Grotesk',Montserrat,sans-serif;line-height:1.15}
.la .mark{font-size:19px;font-weight:700;color:#1C1410;letter-spacing:-.01em}
.la .mark .sl{color:#9C2058}
.la .tag{font-size:9.5px;font-weight:600;letter-spacing:.16em;color:#2A9D8F;text-transform:uppercase;margin-top:3px}
.pre{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:16px}
.pre h3{font-size:12px;font-weight:700;letter-spacing:.12em;color:var(--blue);margin:0 0 7px;text-transform:uppercase}
.pre p{margin:0 0 16px;font-size:15px;color:var(--ink)}
.pre p:last-child{margin-bottom:0}
h1{font-size:30px;line-height:1.2;font-weight:700;color:var(--deep);margin:22px 0 10px;letter-spacing:-.01em}
.lede{font-size:16px;color:var(--muted);margin:0 0 6px;max-width:56ch}
.meta{font-size:13px;color:var(--blue);font-weight:600;margin-top:14px}
.anon{background:#EAF2FC;border-left:3px solid var(--blue);padding:14px 16px;border-radius:0 8px 8px 0;
  font-size:14px;color:var(--deep);margin-top:18px}
.anon b{font-weight:700}
section{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:24px 22px;margin-bottom:16px}
.num{font-size:11px;font-weight:700;letter-spacing:.14em;color:var(--blue)}
h2{font-size:20px;font-weight:600;color:var(--deep);margin:6px 0 4px;line-height:1.3}
.hint{font-size:14px;color:var(--muted);margin:0 0 18px}
.row{margin:0 0 20px}
.row:last-child{margin-bottom:0}
.lab{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:7px}
.lab span:first-child{font-size:15px;font-weight:500}
.val{font-size:12px;font-weight:700;color:var(--white);background:var(--blue);
  border-radius:20px;padding:2px 9px;min-width:38px;text-align:center;flex:none}
input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:8px;border-radius:20px;
  background:var(--line);outline:none;margin:0}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:22px;height:22px;border-radius:50%;
  background:var(--white);border:3px solid var(--blue);cursor:pointer;box-shadow:0 1px 4px rgba(0,0,0,.2)}
input[type=range]::-moz-range-thumb{width:22px;height:22px;border-radius:50%;background:var(--white);
  border:3px solid var(--blue);cursor:pointer}
.ends{display:flex;justify-content:space-between;font-size:12px;color:var(--muted);margin-top:5px}
.ends.three span:nth-child(2){text-align:center}
.chips{display:flex;flex-wrap:wrap;gap:9px}
.chip{border:1.5px solid var(--line);background:var(--white);border-radius:22px;padding:9px 15px;
  font-family:inherit;font-size:14px;font-weight:500;color:var(--ink);cursor:pointer;transition:.15s}
.chip:hover{border-color:var(--blue)}
.chip.on{background:var(--blue);border-color:var(--blue);color:var(--white)}
label.q{display:block;font-size:15px;font-weight:500;margin:0 0 7px}
textarea,input[type=text]{width:100%;font-family:inherit;font-size:15px;color:var(--ink);
  border:1.5px solid var(--line);border-radius:10px;padding:11px 13px;background:var(--white);resize:vertical}
textarea:focus,input[type=text]:focus{outline:none;border-color:var(--blue)}
textarea{min-height:74px}
.dial .val{background:var(--deep)}
.warn .val{background:var(--orange)}
.warn input[type=range]::-webkit-slider-thumb{border-color:var(--orange)}
.warn input[type=range]::-moz-range-thumb{border-color:var(--orange)}
.hp{position:absolute;left:-9999px}
.submit{width:100%;background:var(--blue);color:var(--white);border:none;border-radius:12px;
  padding:17px;font-family:inherit;font-size:17px;font-weight:600;cursor:pointer;transition:.15s}
.submit:hover{background:var(--deep)}
.submit:disabled{opacity:.55;cursor:default}
.foot{font-size:13px;color:var(--muted);text-align:center;margin-top:16px}
.done{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:44px 26px;text-align:center}
.done h2{font-size:24px;margin-bottom:8px}
.done p{color:var(--muted);margin:0;font-size:15px}
.err{color:var(--orange);font-size:14px;text-align:center;margin-top:12px;font-weight:500}
@media(max-width:520px){h1{font-size:25px}section{padding:20px 17px}}
</style>
</head>
<body>
<header><div class="wrap"><div class="brandbar">
  <div class="logo">__LOGO__</div>
  <div class="divider"></div>
  <div class="la"><div class="mark"><span class="sl">/</span>erica-layer</div><div class="tag">AI on Purpose</div></div>
</div></div></header>
<div class="wrap">

<div id="form">
  <h1>Before we start</h1>
  <p class="lede">Please answer a few questions before the first session so that it can be tailored to where the team actually is.</p>
  <p class="meta">About 7 minutes · drag the bars, tap the chips</p>

  <div class="pre" style="margin-top:22px">
    <h3>Who this is from</h3>
    <p>Erica has 20 years of experience in global digital health nonprofit strategy and currently works with social impact organisations to build the human and AI operating systems they run on. She previously served as CEO of D-tree International and COO of health.enabled.</p>
    <h3>What is happening</h3>
    <p>Erica will be facilitating two sessions in September on how Transform Health wants to work with AI. The output is a shared set of values and norms for how the team works with AI, which then shapes how the six week AI capacity course is built so that it meets the team's needs.</p>
    <h3>Why this survey</h3>
    <p>Starting with an intake survey helps Erica to understand the current situation and tailor the two workshops to where the team actually is.</p>
  </div>
  <div class="anon"><b>This survey is anonymous.</b> We will not collect your name, email, or anything that identifies you. Answers go directly to Erica. Individual responses will not be shared with Transform Health, only summarised responses across the team. Please answer as honestly as possible.</div>

  <section>
    <div class="num">01</div><h2>Where does your time actually go?</h2>
    <p class="hint">Roughly how much of a normal week does each of these take?</p>
    <div id="time"></div>
  </section>

  <section>
    <div class="num">02</div><h2>If you had help, what would you delegate?</h2>
    <p class="hint">For each one, where would you want to land?</p>
    <div id="assist"></div>
  </section>

  <section>
    <div class="num">03</div><h2>How are you using AI right now?</h2>
    <div id="ainow"></div>
    <label class="q" style="margin-top:24px">And in which ways?</label>
    <p class="hint" style="margin-bottom:12px">Tap any that apply.</p>
    <div class="chips" id="ways"></div>
    <label class="q" style="margin-top:24px">Which tools, if any, do you use today?</label>
    <p class="hint" style="margin-bottom:12px">Including anything you use personally or informally. Nobody is being audited.</p>
    <div class="chips" id="tools"></div>
  </section>

  <section>
    <div class="num">04</div><h2>How are you feeling about it?</h2>
    <p class="hint">Tap any that fit.</p>
    <div class="chips" id="feelings"></div>
  </section>

  <section>
    <div class="num">05</div><h2>Excited and skeptical are not opposites</h2>
    <p class="hint">You can be both. Most people are.</p>
    <div id="dials" class="dial"></div>
  </section>

  <section class="warn">
    <div class="num">06</div><h2>What are you actually worried about?</h2>
    <p class="hint">Drag each one to how much it worries you.</p>
    <div id="concerns"></div>
    <label class="q" style="margin-top:18px">Your single biggest worry, if you had to name one</label>
    <textarea id="biggest_worry" placeholder="Optional"></textarea>
  </section>

  <section>
    <div class="num">07</div><h2>What do you want AI to help you with?</h2>
    <p class="hint">Drag each one to how much you want it.</p>
    <div id="outcomes"></div>
  </section>





  <section>
    <div class="num">08</div><h2>Anything else?</h2>
    <p class="hint">Anything you want Erica to know before the sessions, or anything you are hoping gets covered.</p>
    <textarea id="anything_else" placeholder="Optional"></textarea>
  </section>

  <input type="text" class="hp" id="website" tabindex="-1" autocomplete="off">
  <button class="submit" id="go">Send my answers</button>
  <p class="foot">Anonymous. Individual responses are never shared with anyone at Transform Health.</p>
  <p class="err" id="err" style="display:none"></p>
</div>

<div class="done" id="done" style="display:none">
  <h2>Thank you</h2>
  <p>That is really useful. See you in September.</p>
</div>

</div>
<script>
const SB_URL="__SB_URL__", SB_KEY="__SB_KEY__";

const TIME=[["advocacy","Advocacy and policy engagement"],["coalitions","Supporting national coalitions and partners"],
["comms","Communications, campaigns and social media"],["fundraising","Fundraising and donor relations"],
["reporting","Donor and internal reporting"],["events","Events and convenings"],
["research","Research, evidence and landscape scanning"],["admin","Internal admin and coordination"],
["meetings","Meetings"]];
const ASSIST=[["meeting_notes","Meeting notes and follow-ups"],["tracking","Task and project tracking"],
["scheduling","Scheduling and calendar"],["briefs","Drafting policy briefs and position papers"],
["donor_reporting","Donor and grant reporting"],["research","Research and landscape scanning"],
["social","Social media and communications content"],["partner_comms","Partner and coalition correspondence"],
["budget","Budget tracking and financial admin"],["logistics","Event and travel logistics"]];
const WAYS=["As a thought partner","Running skills I have set up","Automations running in the background","A full operating system with agents"];
const TOOLS=["ChatGPT","Claude","Microsoft Copilot","Gemini","Perplexity","Something else","None of these"];
const FEELINGS=["Curious","Excited","Skeptical","Anxious","Overwhelmed","Behind","Hopeful","Uneasy","Indifferent","Relieved someone is finally doing this"];
const CONCERNS=[["quality","The quality of the work we produce"],["skills","Losing my own skills over time"],
["unnoticed","Getting something wrong without noticing"],["confidentiality","Confidentiality of our data and our partners' data"],
["political","Saying something politically or diplomatically wrong about a government or partner"],
["job","What it means for my role and job security"],["time","Finding the time to learn this on top of my workload"],
["performance","It being used to judge my performance"]];
const OUTCOMES=[["time_back","Getting time back from admin"],["team_view","Seeing what is happening across the team"],
["landscape","Keeping up with the digital health and AI landscape"],["drafting","Drafting faster without losing quality"],
["donor_rep","Better and less painful donor reporting"],["approvals","Less waiting on approvals and sign-off"],
["finding","Finding things I know we have somewhere"],["objectives","Tracking progress against our objectives"]];
const DIALS=[["excitement","How excited are you about what AI could do for your work?","Not really","Can't wait"],
["skepticism","How skeptical are you, honestly?","All in","Show me it's real"],
["confidence","How confident do you feel using AI well right now?","Just starting out","Very confident"]];

const S={};
function slider(host,key,label,lo,hi,mid,def){
  const d=document.createElement('div');d.className='row';
  d.innerHTML=`<div class="lab"><span>${label}</span><span class="val">${def}</span></div>
  <input type="range" min="0" max="100" value="${def}">
  <div class="ends${mid?' three':''}"><span>${lo}</span>${mid?`<span>${mid}</span>`:''}<span>${hi}</span></div>`;
  const r=d.querySelector('input'),v=d.querySelector('.val');
  S[key]=def;
  const paint=()=>{const p=r.value;v.textContent=p;S[key]=+p;
    r.style.background=`linear-gradient(90deg,var(--blue) ${p}%,var(--line) ${p}%)`;save();};
  r.addEventListener('input',paint);paint();
  host.appendChild(d);
}
TIME.forEach(([k,l])=>slider(document.getElementById('time'),'time.'+k,l,'none of it','most of it',null,20));
ASSIST.forEach(([k,l])=>slider(document.getElementById('assist'),'assist.'+k,l,'keep it myself','hand it over','do it together',20));
slider(document.getElementById('ainow'),'ai_now','How much do you use AI in your work today?','never','all the time',null,20);
DIALS.forEach(([k,l,lo,hi])=>slider(document.getElementById('dials'),k,l,lo,hi,null,20));
CONCERNS.forEach(([k,l])=>slider(document.getElementById('concerns'),'concerns.'+k,l,'not worried','very worried',null,20));
OUTCOMES.forEach(([k,l])=>slider(document.getElementById('outcomes'),'outcomes.'+k,l,'not important','really want this',null,20));

const wh=document.getElementById('ways');const ways=new Set();
WAYS.forEach(t=>{const b=document.createElement('button');b.className='chip';b.type='button';b.textContent=t;
  b.onclick=()=>{b.classList.toggle('on');ways.has(t)?ways.delete(t):ways.add(t);save();};wh.appendChild(b);});

const th=document.getElementById('tools');const tools=new Set();
TOOLS.forEach(t=>{const b=document.createElement('button');b.className='chip';b.type='button';b.textContent=t;
  b.onclick=()=>{b.classList.toggle('on');tools.has(t)?tools.delete(t):tools.add(t);save();};th.appendChild(b);});

const fh=document.getElementById('feelings');const picked=new Set();
FEELINGS.forEach(f=>{const b=document.createElement('button');b.className='chip';b.type='button';b.textContent=f;
  b.onclick=()=>{b.classList.toggle('on');picked.has(f)?picked.delete(f):picked.add(f);save();};fh.appendChild(b);});

const TEXTS=['biggest_worry','anything_else'];
TEXTS.forEach(id=>document.getElementById(id).addEventListener('input',save));

function collect(){
  const nest={};
  for(const[k,v]of Object.entries(S)){
    if(k.includes('.')){const[a,b]=k.split('.');(nest[a]=nest[a]||{})[b]=v;}else nest[k]=v;
  }
  TEXTS.forEach(id=>nest[id]=document.getElementById(id).value.trim());
  nest.feelings=[...picked];
  nest.ai_tools=[...tools];
  nest.ai_ways=[...ways];
  return nest;
}
function save(){try{localStorage.setItem('th_survey',JSON.stringify({s:S,f:[...picked],tl:[...tools],wy:[...ways],
  t:Object.fromEntries(TEXTS.map(i=>[i,document.getElementById(i).value]))}));}catch(e){}}
try{const raw=localStorage.getItem('th_survey');if(raw){const d=JSON.parse(raw);
  document.querySelectorAll('.row').forEach(()=>{});
  Object.entries(d.t||{}).forEach(([i,v])=>{const el=document.getElementById(i);if(el)el.value=v;});
  (d.f||[]).forEach(f=>{[...fh.children].forEach(b=>{if(b.textContent===f){b.classList.add('on');picked.add(f);}});});
  (d.tl||[]).forEach(f=>{[...th.children].forEach(b=>{if(b.textContent===f){b.classList.add('on');tools.add(f);}});});
  (d.wy||[]).forEach(f=>{[...wh.children].forEach(b=>{if(b.textContent===f){b.classList.add('on');ways.add(f);}});});
}}catch(e){}

document.getElementById('go').onclick=async()=>{
  if(document.getElementById('website').value)return;
  const btn=document.getElementById('go'),err=document.getElementById('err');
  btn.disabled=true;btn.textContent='Sending...';err.style.display='none';
  const p=collect();
  const body={excitement:p.excitement,skepticism:p.skepticism,confidence:p.confidence,
    payload:Object.assign({},p,{submitted_at:new Date().toISOString(),user_agent:navigator.userAgent})};
  try{
    const r=await fetch(SB_URL+'/rest/v1/th_ai_survey',{method:'POST',
      headers:{'Content-Type':'application/json','apikey':SB_KEY,'Authorization':'Bearer '+SB_KEY,'Prefer':'return=minimal'},
      body:JSON.stringify(body)});
    if(!r.ok)throw new Error(r.status+' '+await r.text());
    try{localStorage.removeItem('th_survey');}catch(e){}
    document.getElementById('form').style.display='none';
    document.getElementById('done').style.display='block';
    window.scrollTo({top:0,behavior:'smooth'});
  }catch(e){
    btn.disabled=false;btn.textContent='Send my answers';
    err.textContent='Something went wrong sending that. Please try again, or let Erica know.';
    err.style.display='block';
  }
};
</script>
</body></html>'''

HTML = HTML.replace('__LOGO__', logo)
HTML = HTML.replace('__SB_URL__', 'https://oymrwfajqywooqtnglxg.supabase.co')
HTML = HTML.replace('__SB_KEY__', 'sb_publishable_pBIeAhaQ3h0kSg22p-cHcQ_QPcYLTnS')
open('index.html','w').write(HTML)
print('written', len(HTML), 'bytes')
