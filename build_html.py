import json
with open('questions_final.json','r',encoding='utf-8') as f:
    Q=json.load(f)
for i,q in enumerate(Q): q['id']=i+1
data=json.dumps(Q,ensure_ascii=False,separators=(',',':'))

css='*{margin:0;padding:0;box-sizing:border-box}body{font-family:Microsoft YaHei,sans-serif;background:#f5f0e8;color:#2c2416}.c{max-width:800px;margin:0 auto;padding:16px}h1{text-align:center;color:#8b1a1a;padding:16px 0;font-size:1.4em}.btn{display:block;width:100%;padding:14px;margin:8px 0;border:none;border-radius:8px;font-size:1em;cursor:pointer;text-align:center;background:#8b1a1a;color:#fff}.btn2{background:#fff;color:#8b1a1a;border:2px solid #8b1a1a}.btn3{background:#fff;color:#8b6914;border:2px solid #8b6914}.card{background:#fff;border-radius:10px;padding:20px;margin:12px 0;box-shadow:0 2px 6px rgba(0,0,0,.05);line-height:1.6}.opt{display:block;width:100%;padding:12px 16px;margin:6px 0;text-align:left;border:2px solid #e0d8c8;border-radius:6px;background:#fdfaf5;font-size:.95em;cursor:pointer}.opt:hover{border-color:#8b6914}.opt.good{border-color:#27ae60;background:#eafaf1}.opt.bad{border-color:#e74c3c;background:#fdedec}.opt.done{pointer-events:none}.ana{margin-top:12px;padding:14px;background:#fef9ef;border-left:4px solid #8b6914;border-radius:4px;font-size:.9em;line-height:1.6;display:none}.ana.on{display:block}.next{display:none;margin-top:10px;padding:10px 24px;background:#8b1a1a;color:#fff;border:none;border-radius:6px;cursor:pointer}.next.on{display:inline-block}.badge{display:inline-block;background:#e74c3c;color:#fff;border-radius:10px;padding:1px 8px;font-size:.8em;margin-left:4px}.empty{text-align:center;padding:60px 20px;color:#999}.back{color:#8b1a1a;background:none;border:none;cursor:pointer;margin-bottom:8px;font-size:.9em}'

js='''var labels="ABCDEFGH";var state={view:"home",filter:"all",queue:[],idx:0};var app=document.getElementById("app");
function P(){try{return JSON.parse(localStorage.cq_p||'{"t":0,"c":0}')}catch(e){return{t:0,c:0}}}
function W(){try{return JSON.parse(localStorage.cq_w||'[]')}catch(e){return[]}}
function Sp(p){localStorage.cq_p=JSON.stringify(p)}function Sw(w){localStorage.cq_w=JSON.stringify(w)}
function home(){var p=P();var w=W();var r=p.t>0?Math.round(p.c/p.t*100):"-";
app.innerHTML='<h1>中国当代史题库</h1><div style="text-align:center;margin-bottom:16px;color:#666">已刷'+p.t+'题 正确率'+r+'% 错题'+w.length+'道 共'+Q.length+'题</div>'+
'<button class="btn" onclick="start(\'all\')">开始刷题（全部时期）</button>'+
'<button class="btn2 btn" onclick="start(\'1949-1952\')">1949-1952 建国初期</button>'+
'<button class="btn2 btn" onclick="start(\'1953-1957\')">1953-1957 过渡时期</button>'+
'<button class="btn2 btn" onclick="start(\'1958-1965\')">1958-1965 大跃进</button>'+
'<button class="btn2 btn" onclick="start(\'1966-1976\')">1966-1976 文革</button>'+
'<button class="btn2 btn" onclick="start(\'1977-1982\')">1977-1982 改革开放</button>'+
'<button class="btn3 btn" onclick="wrong()">错题本<span class=badge>'+w.length+'</span></button>'+
'<button class="btn3 btn" onclick="browse()">题库大览</button>';
}
function start(f){state.filter=f;state.view="quiz";var pool=Q;if(f!=="all")pool=Q.filter(function(q){return q.period===f});state.queue=pool.map(function(q){return q.id}).sort(function(){return Math.random()-0.5});state.idx=0;quiz();}
function quiz(){if(state.idx>=state.queue.length){app.innerHTML='<div class="card" style="text-align:center"><h2>完成</h2><button class="btn" onclick="start(state.filter)">再来一轮</button><button class="btn2 btn" onclick="home()">返回主页</button></div>';return}
var qid=state.queue[state.idx];var q=null;for(var i=0;i<Q.length;i++){if(Q[i].id===qid){q=Q[i];break}}if(!q){state.idx++;quiz();return}
var n=state.idx+1;var t=state.queue.length;app.innerHTML='<button class="back" onclick="home()">返回</button>'+'<div class="card"><small style="color:#999">'+n+'/'+t+' · '+q.period+'</small>'+'<p style="font-size:1.1em;margin:12px 0">'+q.question+'</p>'+q.options.map(function(o,i){return '<button class="opt" id="o'+i+'" onclick="answer('+qid+','+i+')">'+labels[i]+'. '+o+'</button>'}).join('')+'<div class="ana" id="ana"></div><button class="next" id="nxt" onclick="next()">下一题</button></div>';}
function answer(qid,ua){var q=null;for(var i=0;i<Q.length;i++){if(Q[i].id===qid){q=Q[i];break}}if(!q)return;var ok=ua===q.answer;var btns=document.querySelectorAll(".opt");for(var i=0;i<btns.length;i++)btns[i].classList.add("done");document.getElementById("o"+q.answer).classList.add("good");if(!ok){document.getElementById("o"+ua).classList.add("bad");var w=W();if(w.indexOf(qid)<0){w.unshift(qid);Sw(w)}}var p=P();p.t++;if(ok)p.c++;Sp(p);document.getElementById("ana").innerHTML="<b>"+(ok?"正确":"错误")+"</b> 答案: <b>"+labels[q.answer]+". "+q.options[q.answer]+"</b><br><br>"+(q.analysis||"");document.getElementById("ana").classList.add("on");document.getElementById("nxt").classList.add("on");}
function next(){state.idx++;quiz()}
function wrong(){var w=W();if(w.length===0){app.innerHTML='<button class="back" onclick="home()">返回</button><div class="empty">暂无错题</div>';return}var h='<button class="back" onclick="home()">返回</button><h2>错题本('+w.length+'题)</h2>';w.forEach(function(qid){var q=null;for(var i=0;i<Q.length;i++){if(Q[i].id===qid){q=Q[i];break}}if(!q)return;h+='<div class="card"><b>#'+q.id+'</b> '+q.question+'<br><span style="color:#1e7e34">答案: '+labels[q.answer]+'. '+q.options[q.answer]+'</span><div class="ana on" style="margin-top:8px">'+(q.analysis||"")+'</div></div>';});app.innerHTML=h;}
function browse(){var ps=["1949-1952","1953-1957","1958-1965","1966-1976","1977-1982"];var pn={"1949-1952":"建国初期","1953-1957":"过渡时期","1958-1965":"大跃进与调整","1966-1976":"文化大革命","1977-1982":"改革开放初期"};var h='<button class="back" onclick="home()">返回</button><h2>题库大览('+Q.length+'题)</h2>';ps.forEach(function(p){var qs=Q.filter(function(q){return q.period===p});if(qs.length===0)return;h+='<h3 style="color:#8b1a1a;margin:16px 0 8px">'+pn[p]+' . '+qs.length+'题</h3>';qs.forEach(function(q){h+='<div class="card" style="cursor:pointer" onclick="var el=this.querySelector(\'div\');el.style.display=el.style.display==\'block\'?\'none\':\'block\'"><b>#'+q.id+'</b> '+q.question+'<div style="display:none;margin-top:8px;padding-top:8px;border-top:1px solid #eee"><b style="color:#1e7e34">'+labels[q.answer]+'. '+q.options[q.answer]+'</b><br>'+(q.analysis||"")+'</div></div>'});});app.innerHTML=h;}'''

html='<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>中国当代史刷题</title><style>'+css+'</style></head><body><div class="c" id="app"></div><script>var Q='+data+';'+js+'home();</script></body></html>'

with open('index.html','w',encoding='utf-8') as f:
    f.write(html)
print(f'OK {len(html)} bytes, {len(Q)} questions')
