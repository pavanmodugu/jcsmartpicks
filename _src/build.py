#!/usr/bin/env python3
"""Builds index.html, sitemap.xml, robots.txt for the JC Smart Picks link page.
Data: products.py   Styles: style.css   Script: app.js  (all inlined -> one fast request)."""
import json, html, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from products import SECTIONS
TAG = "jcsmartpick0e-21"
BASE = "https://pavanmodugu.github.io/jcsmartpicks/"
UPDATED_ISO = "2026-10-08"
UPDATED_HUMAN = "8 October 2026"
OUT = os.path.dirname(HERE)
VERIFY = '<meta name="google-site-verification" content="OB4e0H9pxlt7TmiGBKKGOR5DMOq12e8H9PZWltPUVYI" />'
IG = "https://www.instagram.com/jcsmartpicks"; YT = "https://www.youtube.com/@jcsmartpicks"
VIDEOS = [("https://youtube.com/shorts/WYM-mqx5p74","t1","🎁","Amma ki Diwali Gift Ideas – Top 3 Amazon.in Finds","YouTube Short · Telugu"),
          ("https://youtube.com/shorts/-Fv5NBJ2yGA","t2","🧽","Diwali Cleaning With Just Water? Magic Eraser Find","YouTube Short · Telugu"),
          (IG,"t3","📸","Follow @jcsmartpicks on Instagram","Reels · new finds every week")]
CHIP = {"featured":"▶ In our videos","sale":"🎉 Sale Picks","budget":"💰 Budget Best","premium":"💎 Premium Picks","diwali-decor":"🪔 Diwali Décor","pooja":"🙏 Pooja","gifts":"🎁 Gifts",
        "home-kitchen":"🏠 Home & Kitchen","gadgets":"🎧 Gadgets","beauty":"💄 Beauty","toys":"🧸 Toys"}
BADGE = {"featured":"▶ In our videos","sale":"🎉 Sale pick","budget":"💰 Budget best","premium":"💎 Premium","diwali-decor":"🪔 Diwali pick","pooja":"🪔 Diwali pick","gifts":"🎁 Gift idea",
         "home-kitchen":"🔥 Trending","gadgets":"🔥 Trending","beauty":"✨ Trending","toys":"🧸 Kids pick"}
KW = {"featured":"video featured diwali","sale":"great indian festival sale deal offer","budget":"budget affordable cheap value smart buy pocket friendly","premium":"premium luxury upgrade flagship high end","diwali-decor":"diwali deepavali decoration decor lights light festival",
      "pooja":"pooja puja diwali rangoli mandir festival","gifts":"gift gifts hamper present diwali bhai dooj amma sister",
      "home-kitchen":"home kitchen appliance cooking","gadgets":"gadget gadgets tech electronics mobile phone accessories",
      "beauty":"beauty skincare skin care makeup hair","toys":"toys kids children game"}
OCC = {  # "Shop by occasion" groups (ASIN lists)
 "amma": "B0H71SYY4J B09F8G2BDX B0DSZH4Y1H B0F54GKQ38 B0F8HJJVW1 B0C897PVVM B078S7CDLT B08FW1GJ4F B08M4T5FJG B0F3JH6RTG B0B63HWLGL B09B8XJDW5 B0B257ZYVB B09J2T124D B0FH569G3V B0H155N39C B0CND1VF2W B01CCGW4OE B0D3VDV73J B00A7PLVU6 B07VKM2HR5 B09L7QWYC3 B00JDACK3S".split(),
 "decor": None, "tech": None, "kids": "B0DHSBBV6R B0DN1RWNSQ B09VC3KD86".split(),
}
TECH_SALE = "B0DYDPBM8K B0FMDL81GS B0BJ72WZQ7 B09B8XJDW5 B0DCZ3WDTB B0F84FBWQM B0DSKNKCYX B0DGJHBX5Y B0BZP2H373 B0CT3SGHXL B0FNWNZZ1B B0DKTZ6592 B0F3JL33DW B09ZPL5VYM B08LHTJTBB".split()

def link(a): return f"https://www.amazon.in/dp/{a}?tag={TAG}"
e = lambda s: html.escape(s, quote=True)
def occ_for(sid, a):
    o=[]
    if a in OCC["amma"]: o.append("amma")
    if sid in ("diwali-decor","pooja") or a=="B0BBFCG66M": o.append("decor")
    if sid=="gadgets" or a in TECH_SALE: o.append("tech")
    if sid=="toys" or a in OCC["kids"]: o.append("kids")
    return " ".join(o)
def mini_css(s): s=re.sub(r"/\*.*?\*/","",s,flags=re.S); return re.sub(r"\s*\n\s*","",s).strip()
def mini_js(s): s=re.sub(r"^/\*.*?\*/\s*","",s,flags=re.S); return "\n".join(l.strip() for l in s.splitlines() if l.strip())
CSS = mini_css(open(os.path.join(HERE,"style.css"),encoding="utf-8").read())
JS = mini_js(open(os.path.join(HERE,"app.js"),encoding="utf-8").read())

# ---- JSON-LD
items=[]
for _,_,ps,*_ in SECTIONS:
    for a,_,n,_ in ps: items.append({"@type":"ListItem","position":len(items)+1,"name":n,"url":link(a)})
assert len({i["url"] for i in items})==len(items), "duplicate product"
ld = {"@context":"https://schema.org","@graph":[
  {"@type":"Organization","@id":BASE+"#org","name":"JC Smart Picks","url":BASE,
   "logo":{"@type":"ImageObject","url":BASE+"logo.png","width":512,"height":512},"sameAs":[IG,YT]},
  {"@type":"WebSite","@id":BASE+"#website","url":BASE,"name":"JC Smart Picks","alternateName":"JCSmartPicks","inLanguage":"en-IN","publisher":{"@id":BASE+"#org"}},
  {"@type":"WebPage","@id":BASE+"#webpage","url":BASE,"name":"JC Smart Picks – Handpicked Amazon.in Finds","isPartOf":{"@id":BASE+"#website"},
   "about":{"@id":BASE+"#org"},"inLanguage":"en-IN","primaryImageOfPage":BASE+"og-image.png","dateModified":UPDATED_ISO,"mainEntity":{"@id":BASE+"#picks"}},
  {"@type":"ItemList","@id":BASE+"#picks","name":"JC Smart Picks – handpicked Amazon.in finds","numberOfItems":len(items),"itemListElement":items},
]}

TITLE = "JC Smart Picks – Handpicked Amazon.in Finds | Trending Deals & Diwali Gifts"
DESC = "JC Smart Picks: handpicked Amazon.in finds – budget buys, premium upgrades, trending gadgets, Diwali lights, pooja items & gift ideas. Telugu Shorts."
KEYS = "JC Smart Picks, jcsmartpicks, Amazon finds India, Amazon.in finds, trending gadgets, viral Amazon products, Diwali gifts, Diwali decoration lights, pooja items, home and kitchen gadgets, Telugu Amazon finds, Great Indian Festival picks, budget Amazon finds, premium gadgets India"
I_IG='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg>'
I_YT='<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="4" fill="currentColor"/><path d="M10 9l5 3-5 3z" fill="#13254f"/></svg>'
I_SH='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/></svg>'
HEART='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20.5s-7.3-4.5-9.3-9C1.3 8.2 3.3 4.6 6.9 4.6c2 0 3.5 1.1 5.1 3 1.6-1.9 3.1-3 5.1-3 3.6 0 5.6 3.6 4.2 6.9-2 4.5-9.3 9-9.3 9z"/></svg>'
I_SEARCH='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>'
DIYA_SVG='''<svg viewBox="0 0 240 200" role="img" aria-label="Glowing Diwali diya illustration"><defs><radialGradient id="gl" cx="50%" cy="45%" r="50%"><stop offset="0" stop-color="#ffe08a" stop-opacity=".9"/><stop offset="1" stop-color="#ffb347" stop-opacity="0"/></radialGradient><linearGradient id="bw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffb347"/><stop offset="1" stop-color="#c2410c"/></linearGradient><linearGradient id="fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff7c2"/><stop offset=".6" stop-color="#ffcc33"/><stop offset="1" stop-color="#ff7a00"/></linearGradient></defs><circle cx="120" cy="80" r="78" fill="url(#gl)"/><g class="flame"><path d="M120 40c14 22 20 36 20 50a20 20 0 0 1-40 0c0-14 6-28 20-50z" fill="url(#fl)"/><path d="M120 70c6 9 8 15 8 21a8 8 0 0 1-16 0c0-6 2-12 8-21z" fill="#fff"/></g><rect x="117" y="104" width="6" height="14" rx="2" fill="#5b3a1a"/><path d="M28 118h184c-6 40-46 62-92 62s-86-22-92-62z" fill="url(#bw)"/><path d="M40 128c26 10 134 10 160 0" stroke="#ffe08a" stroke-width="5" fill="none" stroke-linecap="round"/><g fill="#ffe08a"><circle cx="70" cy="150" r="5"/><circle cx="96" cy="158" r="5"/><circle cx="120" cy="160" r="5"/><circle cx="144" cy="158" r="5"/><circle cx="170" cy="150" r="5"/></g><path d="M28 118c40-10 144-10 184 0" stroke="#7c2d12" stroke-width="4" fill="none"/></svg>'''
PARTICLES=[("6%","9s","0s","1.1","🪔"),("16%","11s","3s",".8","✨"),("27%","8s","1.5s","1","✨"),("38%","12s","5s","1.3","🪔"),("50%","10s","2s",".9","✨"),
           ("61%","9.5s","6s","1.2","🎆"),("72%","11.5s",".5s",".8","✨"),("83%","8.5s","4s","1.1","🪔"),("93%","10.5s","2.5s",".9","✨"),("44%","13s","7s",".7","🎁")]

total=len(items); ncat=len(SECTIONS)
h=[]
h.append('<!doctype html><html lang="en-IN"><head>\n'+VERIFY+'<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">')
h.append(f'<title>{e(TITLE)}</title><meta name="description" content="{e(DESC)}"><meta name="keywords" content="{e(KEYS)}">')
h.append(f'<meta name="robots" content="index,follow,max-image-preview:large"><meta name="author" content="JC Smart Picks"><meta name="theme-color" content="#13254f"><link rel="canonical" href="{BASE}">')
h.append(f'<link rel="icon" href="{BASE}favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"><link rel="icon" type="image/png" sizes="192x192" href="logo-192.png"><link rel="apple-touch-icon" href="apple-touch-icon.png">')
h.append(f'<meta property="og:type" content="website"><meta property="og:site_name" content="JC Smart Picks"><meta property="og:locale" content="en_IN"><meta property="og:title" content="{e(TITLE)}"><meta property="og:description" content="{e(DESC)}"><meta property="og:url" content="{BASE}"><meta property="og:image" content="{BASE}og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="JC Smart Picks – Handpicked Amazon.in finds">')
h.append(f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(TITLE)}"><meta name="twitter:description" content="{e(DESC)}"><meta name="twitter:image" content="{BASE}og-image.png"><meta name="twitter:image:alt" content="JC Smart Picks – Handpicked Amazon.in finds">')
h.append('<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False,separators=(",",":"))+'</script>')
h.append("<script>try{var t=localStorage.getItem('jcsp-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');document.documentElement.dataset.theme=t}catch(e){}</script>")
h.append(f'<style>{CSS}</style></head><body>')
h.append('<a class="skip" href="#picks">Skip to products</a>')
h.append('<div class="adbar"><b>#ad</b> · As an Amazon Associate I earn from qualifying purchases.</div>')
h.append(f'<header class="hdr"><div class="wrap"><a class="brand" href="#top" aria-label="JC Smart Picks home"><img src="avatar.jpg" width="36" height="36" alt=""><span>JC Smart <em>Picks</em></span></a>'
         f'<a class="ib" href="{IG}" target="_blank" rel="noopener me" aria-label="Instagram @jcsmartpicks">{I_IG}</a>'
         f'<a class="ib" href="{YT}" target="_blank" rel="noopener me" aria-label="YouTube @jcsmartpicks">{I_YT}</a>'
         f'<button class="ib" type="button" data-share aria-label="Share this page">{I_SH}</button>'
         f'<button class="ib" type="button" data-go="saved" aria-label="My picks (saved)">{HEART.replace("<svg ","<svg fill=\"currentColor\" ")}<span class="n savedn" hidden>0</span></button>'
         '<button class="ib" type="button" id="theme" aria-label="Switch to dark mode">🌙</button></div></header>')
# hero
h.append('<main id="top"><section class="hero"><div class="pts" aria-hidden="true">'+''.join(f'<span class="pt" style="--x:{x};--d:{dd};--w:{wd};--s:{s}">{c}</span>' for x,dd,wd,s,c in PARTICLES)+'</div><div class="wrap"><div>')
h.append('<span class="kick">🎉 Great Indian Festival · 🪔 Diwali 2026</span>')
h.append('<h1>JC Smart <em>Picks</em></h1><p class="lead">Trending Amazon.in finds, handpicked for you 🛒</p>')
h.append('<p class="intro">JC Smart Picks shares handpicked <strong>Amazon finds for India</strong>: <strong>Great Indian Festival</strong> sale picks, budget-friendly buys, premium upgrades, trending gadgets, home &amp; kitchen helpers, beauty, toys and <strong>Diwali gifts &amp; décor</strong>, explained in short Telugu videos on Instagram and YouTube. Tap any card to check today\'s price on Amazon.in.</p>')
h.append('<p class="te" lang="te">తెలుగులో షార్ట్ వీడియోలు, Instagram &amp; YouTube లో 👇</p>')
h.append('<div class="ctas"><a class="cta p" href="#picks">Explore today\'s picks ↓</a><a class="cta s" href="#videos">▶ Watch our Shorts</a></div>')
h.append(f'<div class="stats"><span><b>{total}</b>handpicked finds</span><span><b>{ncat}</b>categories</span><span><b>తెలుగు</b>Shorts &amp; Reels</span></div>')
h.append(f'</div><div class="art">{DIYA_SVG}</div></div></section>')
h.append('<div class="wrap">')
# occasions
h.append('<section class="sec" aria-labelledby="occ-h"><h2 id="occ-h">Shop by occasion</h2><p class="sub">Quick ideas for every budget this festive season</p><div class="occ">'
         '<a class="oc o1 rv" href="#gifts" data-go="occ-amma"><i aria-hidden="true">🎁</i>Gifts for Amma<small>Kitchen, pooja &amp; self-care</small></a>'
         '<a class="oc o2 rv" href="#diwali-decor" data-go="occ-decor"><i aria-hidden="true">🪔</i>Budget Diwali décor<small>Lights, diyas &amp; torans</small></a>'
         '<a class="oc o3 rv" href="#gadgets" data-go="occ-tech"><i aria-hidden="true">🎧</i>Tech gifts<small>Earbuds, watches &amp; more</small></a>'
         '<a class="oc o4 rv" href="#toys" data-go="occ-kids"><i aria-hidden="true">🧸</i>For kids<small>Toys &amp; fun learning</small></a>'
         '<a class="oc o5 rv" href="#budget" data-go="budget"><i aria-hidden="true">💰</i>Budget buys<small>Smart everyday picks</small></a>'
         '<a class="oc o6 rv" href="#premium" data-go="premium"><i aria-hidden="true">💎</i>Premium upgrades<small>Phones, audio &amp; home tech</small></a></div></section>')
# toolbar + products
h.append('<section class="sec" id="picks" aria-labelledby="picks-h"><h2 id="picks-h">Today\'s handpicked finds</h2><p class="sub">Search or tap a category. Every card opens the product on Amazon.in.</p>')
h.append(f'<div class="tools"><div class="srch" role="search">{I_SEARCH}<label for="q" class="skip">Search products</label><input id="q" type="search" placeholder="Search: diya, lights, earbuds, gift…" autocomplete="off" enterkeyhint="search" aria-describedby="count"><button class="clr" id="clr" type="button" aria-label="Clear search" hidden>✕</button></div>')
h.append('<div class="chips" role="toolbar" aria-label="Filter by category"><button class="chip" type="button" data-f="all" aria-pressed="true">✨ All</button>'
         + ''.join(f'<button class="chip" type="button" data-f="{sid}" aria-pressed="false">{CHIP[sid]}</button>' for sid,_,_,*_ in SECTIONS if sid!="featured")
         + '<button class="chip" type="button" data-f="featured" aria-pressed="false">▶ In our videos</button><button class="chip" type="button" data-f="saved" aria-pressed="false">♥ My picks <span class="savedn" hidden>0</span></button></div>'
         f'<p class="count" id="count" aria-live="polite">Showing all {total} handpicked finds</p></div>')
for sid,title,ps,*note in SECTIONS:
    h.append(f'<section class="cat" id="{sid}" aria-labelledby="h-{sid}"><h2 id="h-{sid}">{html.escape(title,quote=False)}</h2>')
    if note: h.append(f'<p class="note">{html.escape(note[0],quote=False)}</p>')
    h.append('<div class="grid">')
    for a,ic,n,dsc in ps:
        s=" ".join([n,dsc,title,KW[sid],CHIP[sid]]).lower()
        s=re.sub(r"[^\w\s\-+.&/]"," ",s,flags=re.U); s=re.sub(r"\s+"," ",s).strip()
        h.append(f'<article class="card rv" data-id="{a}" data-cat="{sid}" data-occ="{occ_for(sid,a)}" data-s="{e(s)}">'
                 f'<div class="tile g-{sid}"><span class="badge">{BADGE[sid]}</span>'
                 f'<button class="fav" type="button" data-id="{a}" aria-pressed="false" aria-label="Save {e(n)} to My picks">{HEART}</button>'
                 f'<span class="emo" aria-hidden="true">{ic}</span></div>'
                 f'<div class="body"><h3>{html.escape(n,quote=False)}</h3><p>{html.escape(dsc,quote=False)}</p>'
                 f'<a class="buy" href="{link(a)}" target="_blank" rel="sponsored noopener">Check price on Amazon.in →</a></div></article>')
    h.append('</div></section>')
h.append('<div class="empty" id="empty" hidden><div aria-hidden="true">🔍</div><strong>No picks match <span id="emptyq"></span></strong><p>Try “lights”, “gift”, “diya” or “earbuds”.</p><button class="btn" id="reset" type="button">Show all picks</button></div></section>')
# videos
h.append('<section class="sec" id="videos" aria-labelledby="vid-h"><h2 id="vid-h">▶ Watch our latest videos</h2><p class="sub">Short Telugu videos on the finds above</p><div class="vids">')
for u,t,ic,ti,sub in VIDEOS:
    h.append(f'<a class="vc rv" href="{u}" target="_blank" rel="noopener"><span class="th {t}" aria-hidden="true">{ic}</span><span><b>{e(ti)}</b><span>{e(sub)}</span><em>Watch now →</em></span></a>')
h.append('</div></section>')
WA="https://wa.me/?text="+ "Handpicked%20Amazon.in%20finds%20for%20Diwali%20%F0%9F%AA%94%20" + "https%3A%2F%2Fpavanmodugu.github.io%2Fjcsmartpicks%2F"
h.append(f'<section class="sharebox rv" aria-labelledby="sh-h"><h2 id="sh-h">Planning Diwali shopping with family? 🪔</h2><p>Send this page to your WhatsApp group.</p><div class="row"><a class="btn wa" href="{WA}" target="_blank" rel="noopener">💬 Share on WhatsApp</a><button class="btn" type="button" data-share>🔗 Share / copy link</button></div></section>')
h.append('</div></main>')
h.append(f'<footer><div class="wrap"><div class="soc"><a class="ib" href="{IG}" target="_blank" rel="noopener me" aria-label="Instagram @jcsmartpicks">{I_IG}</a><a class="ib" href="{YT}" target="_blank" rel="noopener me" aria-label="YouTube @jcsmartpicks">{I_YT}</a><button class="ib" type="button" data-share aria-label="Share this page">{I_SH}</button></div>'
         '<p><strong>#ad</strong> · As an Amazon Associate I earn from qualifying purchases.</p>'
         '<p>Prices and availability change often, so check today\'s price on Amazon.in.</p>'
         f'<p>Last updated: <time datetime="{UPDATED_ISO}">{UPDATED_HUMAN}</time></p>'
         f'<p><a href="{IG}" target="_blank" rel="noopener">Instagram</a> · <a href="{YT}" target="_blank" rel="noopener">YouTube</a> · <a href="#top">Back to top</a></p><p>© 2026 JC Smart Picks</p></div></footer>')
h.append('<button class="totop" id="totop" type="button" aria-label="Back to top">↑</button><div class="toast" id="toast" role="status" aria-live="polite"></div>')
h.append(f'<script>{JS}</script></body></html>')
open(os.path.join(OUT,"index.html"),"w",encoding="utf-8").write("\n".join(h)+"\n")
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(OUT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url>\n    <loc>{BASE}</loc>\n    <lastmod>{UPDATED_ISO}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>\n</urlset>\n')
print("products:",total,"bytes:",os.path.getsize(os.path.join(OUT,"index.html")))
