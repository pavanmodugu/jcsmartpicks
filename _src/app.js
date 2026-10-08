/* JC Smart Picks – progressive enhancement (inlined by build.py). Content is static HTML; this only adds filtering, wishlist, share, theme. */
(function(){
var d=document,h=d.documentElement,w=window;h.classList.add("js");
function $(s,r){return (r||d).querySelector(s)}function $$(s,r){return Array.prototype.slice.call((r||d).querySelectorAll(s))}
var store={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
var reduce=w.matchMedia&&w.matchMedia('(prefers-reduced-motion: reduce)').matches;
var cards=$$('.card'),secs=$$('.cat'),q=$('#q'),clr=$('#clr'),chips=$$('.chip'),cnt=$('#count'),empty=$('#empty'),toastEl=$('#toast'),picks=$('#picks');
var cat='all',tt;
function toast(m){toastEl.textContent=m;toastEl.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){toastEl.classList.remove('on')},2400)}
/* wishlist */
var saved;try{saved=JSON.parse(store.get('jcsp-saved')||'[]')}catch(e){saved=[]}
function isSaved(id){return saved.indexOf(id)>-1}
function syncSaved(){var n=saved.length;$$('.savedn').forEach(function(e){e.textContent=n;e.hidden=!n});
 $$('.fav').forEach(function(b){b.setAttribute('aria-pressed',isSaved(b.dataset.id)?'true':'false')})}
$$('.fav').forEach(function(b){b.addEventListener('click',function(ev){ev.preventDefault();ev.stopPropagation();var id=b.dataset.id,i=saved.indexOf(id);
 if(i>-1){saved.splice(i,1);toast('Removed from My picks')}else{saved.push(id);toast('♥ Saved to My picks')}
 store.set('jcsp-saved',JSON.stringify(saved));b.classList.remove('pop');void b.offsetWidth;b.classList.add('pop');syncSaved();if(cat==='saved')apply()})});
/* filtering */
function matchCat(c){if(cat==='all')return true;if(cat==='saved')return isSaved(c.dataset.id);
 if(cat.indexOf('occ-')===0)return (' '+c.dataset.occ+' ').indexOf(' '+cat.slice(4)+' ')>-1;return c.dataset.cat===cat}
function apply(push){var t=(q.value||'').trim().toLowerCase(),terms=t?t.split(/\s+/):[],n=0;
 cards.forEach(function(c){var s=c.dataset.s,ok=matchCat(c)&&terms.every(function(x){return s.indexOf(x)>-1||(x.length>3&&x.slice(-1)==='s'&&s.indexOf(x.slice(0,-1))>-1)});c.hidden=!ok;if(ok){n++;c.classList.add('in')}});
 secs.forEach(function(s){s.hidden=!s.querySelector('.card:not([hidden])')});
 empty.hidden=n>0;$('#emptyq').textContent=t?'“'+q.value.trim()+'”':(cat==='saved'?'your saved list':'this filter');
 var lbl=cat==='all'?'':' in '+(($$('.chip[data-f="'+cat+'"]')[0]||{}).textContent||'').replace(/\s*\d+$/,'');
 cnt.textContent=(n===cards.length&&!t)?'Showing all '+n+' handpicked finds':n+' pick'+(n===1?'':'s')+lbl+(t?' for “'+q.value.trim()+'”':'');
 clr.hidden=!t;
 chips.forEach(function(ch){ch.setAttribute('aria-pressed',ch.dataset.f===cat?'true':'false')});
 if(push!==false&&history.replaceState){var u=new URLSearchParams();if(cat!=='all')u.set('f',cat);if(t)u.set('q',t);var qs=u.toString();history.replaceState(null,'',location.pathname+(qs?'?'+qs:'')+location.hash)}}
function setCat(f,scroll){cat=f;apply();if(scroll)picks.scrollIntoView({behavior:reduce?'auto':'smooth'})}
chips.forEach(function(ch){ch.addEventListener('click',function(){setCat(ch.dataset.f);var a=ch.getBoundingClientRect();if(picks.getBoundingClientRect().top<0)picks.scrollIntoView({behavior:reduce?'auto':'smooth'})})});
$$('[data-go]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();q.value='';setCat(a.dataset.go,true)})});
var deb;q.addEventListener('input',function(){clearTimeout(deb);deb=setTimeout(apply,90)});
q.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();q.blur();picks.scrollIntoView({behavior:reduce?'auto':'smooth'})}});
clr.addEventListener('click',function(){q.value='';apply();q.focus()});
$('#reset').addEventListener('click',function(){q.value='';setCat('all')});
d.addEventListener('keydown',function(e){if(e.key==='/'&&d.activeElement!==q&&!/input|textarea/i.test(d.activeElement.tagName)){e.preventDefault();q.focus()}});
/* initial state from URL */
var P=new URLSearchParams(location.search);if(P.get('q'))q.value=P.get('q');var f0=P.get('f');if(f0&&(f0==='saved'||f0.indexOf('occ-')===0||$$('.chip[data-f="'+f0+'"]').length))cat=f0;
/* share */
var url=location.origin+location.pathname;
$$('[data-share]').forEach(function(b){b.addEventListener('click',function(){var data={title:'JC Smart Picks – Handpicked Amazon.in Finds',text:'Handpicked Amazon.in finds for Diwali & the Great Indian Festival 🪔🛒',url:url};
 if(navigator.share){navigator.share(data).catch(function(){})}else if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(url).then(function(){toast('Link copied – paste it in WhatsApp 👍')},function(){toast(url)})}else{toast(url)}})});
/* theme */
var tb=$('#theme');function setTheme(t){h.dataset.theme=t;tb.textContent=t==='dark'?'☀️':'🌙';tb.setAttribute('aria-label',t==='dark'?'Switch to light mode':'Switch to dark mode');var m=$('meta[name=theme-color]');if(m)m.content=t==='dark'?'#0d1630':'#13254f'}
setTheme(h.dataset.theme||'light');tb.addEventListener('click',function(){var t=h.dataset.theme==='dark'?'light':'dark';setTheme(t);store.set('jcsp-theme',t)});
/* header shadow + back to top */
var hdr=$('.hdr'),top=$('#totop'),ticking=false;
function onScroll(){var y=w.scrollY||0;hdr.classList.toggle('sc',y>8);top.classList.toggle('on',y>700);ticking=false}
w.addEventListener('scroll',function(){if(!ticking){ticking=true;w.requestAnimationFrame(onScroll)}},{passive:true});
top.addEventListener('click',function(){w.scrollTo({top:0,behavior:reduce?'auto':'smooth'})});
/* scroll reveal */
if('IntersectionObserver' in w&&!reduce){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -6% 0px'});$$('.rv').forEach(function(el){io.observe(el)})}
else{$$('.rv').forEach(function(el){el.classList.add('in')})}
syncSaved();apply(false);onScroll();
})();
