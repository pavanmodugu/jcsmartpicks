#!/usr/bin/env python3
"""Builds index.html, sitemap.xml, robots.txt for the JC Smart Picks link page."""
import json, html, os
TAG = "jcsmartpick0e-21"
BASE = "https://pavanmodugu.github.io/jcsmartpicks/"
UPDATED_ISO = "2026-10-08"
UPDATED_HUMAN = "8 October 2026"
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECTIONS = [
 ("featured", "🔥 Featured in our latest videos", [
  ("B0GPN9R146","✨","Happi Planet Magic Eraser (Pack of 4)","Diwali deep-cleaning for walls, switchboards & tiles"),
  ("B0BBFCG66M","🪔","DesiDiya LED Pixel String Lights (Warm White, ~10 m)","Budget balcony, mirror & pooja-corner glow"),
 ]),
 ("sale", "🎉 Great Indian Festival Picks", [
  ("B0DYDPBM8K","📱","Samsung Galaxy A56 5G (8 GB / 128 GB)","50MP triple camera with AI photo-editing features"),
  ("B0FMDL81GS","🎧","OnePlus Nord Buds 3r TWS Earbuds","2-mic clear calls & 3D spatial audio"),
  ("B0BJ72WZQ7","⌚","Noise Twist Round-Dial Smartwatch","Bluetooth calling with 100+ watch faces"),
  ("B09B8XJDW5","🔊","Amazon Echo Dot (5th Gen) Smart Speaker","Alexa for music, reminders & smart-home control"),
  ("B0FH569G3V","🍟","Lifelong Smartchoice 4.2 L Digital Air Fryer","7 preset menus, touch panel, non-stick basket"),
  ("B0CHJNJJDP","🌀","atomberg Renesa Enzel 1200 mm BLDC Ceiling Fan","BLDC motor fan with remote & LED speed indicator"),
  ("B0DCZ3WDTB","🔋","Xiaomi Power Bank 4i 20000 mAh","33 W fast charging, Type-C in & out"),
  ("B0F84FBWQM","📺","Samsung 32-inch HD Smart LED TV","Compact smart TV for bedroom or hall"),
  ("B0F3JH6RTG","📿","PALMONAS 18k Gold Plated Beaded Bliss Necklace","Listed as waterproof & anti-tarnish, an easy gift"),
  ("B0DHSBBV6R","🏎️","LEGO Speed Champions Ferrari SF-24 F1 Car (77242)","Building set for ages 10+"),
 ], "Sale deals change fast — check today's price on Amazon.in."),
 ("diwali-decor", "🪔 Diwali Décor & Lights", [
  ("B0DFZ579HK","💧","PulGos Water Sensor LED Diyas (36 pcs)","Reusable diyas that glow when placed in water, no smoke"),
  ("B0CVGY985K","🍃","One94Store Leaf Curtain Lights (200 LED, 3×1 m)","Warm-white curtain with remote for windows & walls"),
  ("B0BD43W4YP","✨","Crompton Galaxy USB Copper Fairy Lights (10 m)","100 warm-white LEDs to wrap shelves, jars & mirrors"),
  ("B0FDBFF8JM","🕯️","VERVENIX LED Tea Light Candles (Pack of 24)","Battery-operated flameless glow, no wax or smoke"),
  ("B0B63HWLGL","🪷","Divyakosh Lotus Wall Hangings (Set of 6)","Handmade jhumki-style décor for mandir & entrance"),
  ("B0CM2485RJ","🚪","Divyakosh Shubh Labh Door Hangings (1 Pair)","Golden side hangings for the main door"),
 ]),
 ("pooja", "🙏 Pooja & Rangoli", [
  ("B0DSZH4Y1H","🔥","ServDharm Brass Akhand Diya","Adjustable wick knob with a borosilicate glass cover"),
  ("B0BFC91NG5","🎨","Ascension Rangoli Making Kit (12 Designs)","Om, Swastik & flower stamps for quick rangoli"),
  ("B0BYQ8T4YD","💎","CentraLit Crystal Tealight Candle Holder","Sparkly holder for diyas & tealights"),
 ]),
 ("gifts", "🎁 Diwali Gifts", [
  ("B0H71SYY4J","🎁","AuraDecor Divine Pooja Gift Hamper","Lotus urli candle, dhoop cones, havan cups & diyas"),
  ("B09F8G2BDX","🥜","PrettyNutty Diwali Dry Fruits Gift (400 g)","Almonds, cashews, pistachios & raisins, 100 g each"),
  ("B099WR4WHC","⌚","Fastrack Tees Analog Unisex Watch","Diwali / Bhai Dooj gift idea"),
  ("B0H155N39C","💎","Shining Diva 12-Pair Earrings Set with Box","Ready-to-gift for sister or friend"),
 ]),
 ("home-kitchen", "🏠 Home & Kitchen", [
  ("B0F8HJJVW1","☕","Nova Rechargeable Electric Milk Frother","Café-style coffee for Diwali guests"),
  ("B0C897PVVM","🧄","AGARO Elite Rechargeable Mini Chopper 250 ml","Quick festive cooking prep"),
  ("B0DN1RWNSQ","🌌","One94Store Nebula Star Projector Night Light","Galaxy room makeover, great kids' gift"),
  ("B008XT42JU","🔌","GM 3060 Extension Board (4 Sockets, 2 m)","Master switch & safety shutters, handy for Diwali lights"),
  ("B078S7CDLT","🥡","Borosil Klip N Store Square Glass Containers (Set of 2)","Air-tight glass boxes for sweets & leftovers"),
  ("B0F54GKQ38","♨️","Milton Rapid Electric Kettle 1.8 L","1500 W stainless-steel kettle for tea & noodles"),
  ("B0B257ZYVB","🥚","AGARO Grand Egg Boiler & Poacher","Boils 8 eggs or poaches 4, also steams veggies"),
  ("B09J2T124D","🥤","NutriPro Juicer Mixer Grinder 500 W","2 jars for smoothies, juices & chutneys"),
 ]),
 ("gadgets", "🎧 Gadgets & Tech", [
  ("B0FBRGKXHG","🎵","OnePlus Bullets Wireless Z3 Neckband","12.4 mm drivers, quick 10-minute charge"),
  ("B0FLF44GTQ","⌚","boAt Wave Call 3 Smartwatch","1.83-inch display with Bluetooth calling"),
  ("B0DNFSSF3F","💾","SanDisk Ultra Dual Drive Go Type-C 128 GB","Pendrive to free up phone storage"),
  ("B0D9S87H53","🧲","Ambrane MagSafe Wireless Power Bank 10000 mAh","Magnetic snap-on charging, 22.5 W output"),
  ("B0FDQ9M1SD","🖱️","Portronics Toad 8 Transparent Wireless Mouse","See-through desk-setup look, BT + 2.4 GHz"),
  ("B08TV2P1N8","🎶","boAt Rockerz 255 Pro+ Neckband","Sale-season gift pick"),
  ("B0F63BY6LT","🤳","Kratos K9 Selfie Stick Tripod with Light","Family photos & rangoli time-lapses"),
  ("B0H5VWCNWN","📍","JioTag (2nd Gen) Item Finder","Track keys, wallets & bags, works with Android or iOS"),
  ("B0BBRJVLWD","⚡","Portronics Adapto 45 GaN Dual-Port Charger","22.5 W USB + Type-C wall adapter"),
  ("B082LSVT4B","🔋","Ambrane 60W Braided Type-C to Type-C Cable (1.5 m)","Fast charging for phones, tablets & laptops"),
  ("B08MCD9JFY","💡","Tygot 10-inch LED Ring Light","For Reels, video calls & makeup"),
 ]),
 ("beauty", "💄 Beauty", [
  ("B0CND1VF2W","💋","WishCare Tinted Lip Balm SPF 50 PA++++","Tint + SPF for festive outdoor days"),
  ("B08FW1GJ4F","💇","L'Oréal Paris Extraordinary Oil Hair Serum 100 ml","Festive hair styling, hamper add-on"),
  ("B09FPS9D5T","🧴","Minimalist Sunscreen SPF 50 PA++++","Niacinamide sunscreen for everyday use"),
  ("B00YJJWBUA","💄","Maybelline Color Sensational Creamy Matte Lipstick","Festive-look lipstick in many shades"),
  ("B01CCGW4OE","🫧","Cetaphil Gentle Skin Hydrating Face Wash 118 ml","Paraben- & sulphate-free gentle cleanser"),
  ("B08M4T5FJG","🧴","Vaseline Deep Moisture Body Lotion","Ceramide lotion for dry winter skin"),
 ]),
 ("toys", "🧸 Toys & Kids", [
  ("B09VC3KD86","✏️","Portronics Ruffpad 12M LCD Writing Pad","Re-writable 12-inch pad with one-tap erase"),
  ("B00004TZY8","🃏","Mattel UNO Card Game","Classic family game for Diwali get-togethers"),
  ("B0GQ89XY15","🧩","Storio 3D Magnetic Tiles (28 pcs)","STEM building toy for ages 3–8"),
 ]),
]

def link(a): return f"https://www.amazon.in/dp/{a}?tag={TAG}"
e = html.escape

# ---- JSON-LD
items=[]; seen=set()
for _,_,ps,*_ in SECTIONS:
    for a,_,n,_ in ps:
        if a in seen: continue
        seen.add(a); items.append({"@type":"ListItem","position":len(items)+1,"name":n,"url":link(a)})
ld = {"@context":"https://schema.org","@graph":[
  {"@type":"Organization","@id":BASE+"#org","name":"JC Smart Picks","url":BASE,
   "logo":{"@type":"ImageObject","url":BASE+"logo.png","width":512,"height":512},
   "sameAs":["https://www.instagram.com/jcsmartpicks","https://www.youtube.com/@jcsmartpicks"]},
  {"@type":"WebSite","@id":BASE+"#website","url":BASE,"name":"JC Smart Picks","alternateName":"JCSmartPicks",
   "inLanguage":"en-IN","publisher":{"@id":BASE+"#org"}},
  {"@type":"WebPage","@id":BASE+"#webpage","url":BASE,"name":"JC Smart Picks – Handpicked Amazon.in Finds",
   "isPartOf":{"@id":BASE+"#website"},"about":{"@id":BASE+"#org"},"inLanguage":"en-IN",
   "primaryImageOfPage":BASE+"og-image.png","dateModified":UPDATED_ISO,"mainEntity":{"@id":BASE+"#picks"}},
  {"@type":"ItemList","@id":BASE+"#picks","name":"JC Smart Picks – handpicked Amazon.in finds","numberOfItems":len(items),"itemListElement":items},
]}

TITLE = "JC Smart Picks – Handpicked Amazon.in Finds | Trending Deals & Diwali Gifts"
DESC = "JC Smart Picks: handpicked Amazon.in finds – trending gadgets, home & kitchen helpers, beauty picks, Diwali lights, pooja items & gift ideas. Telugu Shorts."
KEYS = "JC Smart Picks, jcsmartpicks, Amazon finds India, Amazon.in finds, trending gadgets, viral Amazon products, Diwali gifts, Diwali decoration lights, pooja items, home and kitchen gadgets, Telugu Amazon finds, Great Indian Festival picks"

CSS = """*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:linear-gradient(160deg,#fff7ec,#ffe9d6 40%,#fde2f0);background-attachment:fixed;color:#222}
.w{max-width:480px;margin:0 auto;padding:14px 16px 40px}.ad{background:#222;color:#fff;font-size:12px;text-align:center;padding:8px;border-radius:10px}
header{text-align:center;margin:18px 0 6px}header img{width:96px;height:96px;border-radius:50%;border:3px solid #fff;box-shadow:0 4px 14px #0002}h1{margin:8px 0 2px;font-size:24px}.tag{margin:0;color:#555;font-size:14px}
.intro{font-size:13.5px;line-height:1.55;color:#444;text-align:center;margin:10px 4px 0}.te{display:block;margin-top:4px;color:#7c2d12;font-weight:600}
.so{display:flex;gap:10px;justify-content:center;margin:12px 0}.so a{text-decoration:none;color:#fff;padding:8px 14px;border-radius:20px;font-size:14px;font-weight:600}.ig{background:linear-gradient(45deg,#f58529,#dd2a7b,#8134af)}.yt{background:#e62117}
nav{display:flex;gap:8px;overflow-x:auto;padding:6px 2px 8px;margin:4px -2px 0;scrollbar-width:none}nav::-webkit-scrollbar{display:none}nav a{flex:none;text-decoration:none;font-size:13px;font-weight:600;color:#7c2d12;background:#fff;border:1px solid #fed7aa;padding:6px 12px;border-radius:16px}
section{scroll-margin-top:10px}h2{font-size:16px;margin:22px 4px 8px}.card{display:flex;gap:12px;align-items:center;background:#fff;border-radius:16px;padding:12px;margin:8px 0;text-decoration:none;color:inherit;box-shadow:0 2px 8px #0001;transition:transform .1s}.card:active{transform:scale(.98)}
.ic{font-size:28px;width:52px;height:52px;flex:none;display:grid;place-items:center;background:#fff3e0;border-radius:12px}.tx b{display:block;font-size:15px}.tx span{display:block;font-size:13px;color:#666;margin:2px 0 6px}.tx em{font-style:normal;font-size:13px;font-weight:700;color:#c2410c}
.note{font-size:12.5px;color:#7c2d12;background:#fff7ed;border:1px dashed #fdba74;border-radius:10px;padding:6px 10px;margin:-2px 0 6px}
footer{text-align:center;font-size:12px;color:#666;margin-top:26px;line-height:1.6}"""

NAVLBL={"featured":"🔥 Featured","sale":"🎉 Sale Picks","toys":"🧸 Toys","diwali-decor":"🪔 Diwali Décor","pooja":"🙏 Pooja","gifts":"🎁 Gifts","home-kitchen":"🏠 Home","gadgets":"🎧 Gadgets","beauty":"💄 Beauty"}

h=[]
h.append('<!doctype html><html lang="en-IN"><head>\n<meta name="google-site-verification" content="OB4e0H9pxlt7TmiGBKKGOR5DMOq12e8H9PZWltPUVYI" /><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">')
h.append(f'<title>{e(TITLE)}</title><meta name="description" content="{e(DESC)}"><meta name="keywords" content="{e(KEYS)}">')
h.append(f'<meta name="robots" content="index,follow,max-image-preview:large"><meta name="author" content="JC Smart Picks"><meta name="theme-color" content="#13254f"><link rel="canonical" href="{BASE}">')
h.append(f'<link rel="icon" href="{BASE}favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"><link rel="icon" type="image/png" sizes="192x192" href="logo-192.png"><link rel="apple-touch-icon" href="apple-touch-icon.png">')
h.append(f'<meta property="og:type" content="website"><meta property="og:site_name" content="JC Smart Picks"><meta property="og:locale" content="en_IN"><meta property="og:title" content="{e(TITLE)}"><meta property="og:description" content="{e(DESC)}"><meta property="og:url" content="{BASE}"><meta property="og:image" content="{BASE}og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="JC Smart Picks – Handpicked Amazon.in finds">')
h.append(f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(TITLE)}"><meta name="twitter:description" content="{e(DESC)}"><meta name="twitter:image" content="{BASE}og-image.png"><meta name="twitter:image:alt" content="JC Smart Picks – Handpicked Amazon.in finds">')
h.append('<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False,separators=(",",":"))+'</script>')
h.append(f'<style>{CSS}</style></head><body><div class="w">')
h.append('<div class="ad">#ad | As an Amazon Associate I earn from qualifying purchases.</div>')
h.append('<header><img src="avatar.jpg" width="96" height="96" alt="JC Smart Picks logo"><h1>JC Smart Picks</h1><p class="tag">Trending Amazon.in finds, handpicked for you 🛒</p></header>')
h.append('<p class="intro">JC Smart Picks shares handpicked <strong>Amazon finds for India</strong>: <strong>Great Indian Festival</strong> sale picks, trending gadgets, home &amp; kitchen helpers, beauty, toys and <strong>Diwali gifts &amp; décor</strong>, explained in short Telugu videos on Instagram and YouTube. Tap any card to check today\'s price on Amazon.in.<span class="te" lang="te">తెలుగులో షార్ట్ వీడియోలు, Instagram &amp; YouTube లో 👇</span></p>')
h.append('<div class="so"><a class="ig" href="https://www.instagram.com/jcsmartpicks" target="_blank" rel="noopener me">📸 Instagram</a><a class="yt" href="https://www.youtube.com/@jcsmartpicks" target="_blank" rel="noopener me">▶ YouTube</a></div>')
h.append('<nav aria-label="Sections">'+''.join(f'<a href="#{sid}">{NAVLBL[sid]}</a>' for sid,_,_,*_ in SECTIONS)+'</nav>')
for sid,title,ps,*note in SECTIONS:
    h.append(f'<section id="{sid}"><h2>{e(title,quote=False)}</h2>')
    if note: h.append(f'<p class="note">{e(note[0],quote=False)}</p>')
    for a,ic,n,d in ps:
        h.append(f'<a class="card" href="{link(a)}" target="_blank" rel="sponsored noopener"><div class="ic" aria-hidden="true">{ic}</div><div class="tx"><b>{e(n,quote=False)}</b><span>{e(d,quote=False)}</span><em>Check today\'s price on Amazon.in →</em></div></a>')
    h.append('</section>')
h.append(f'<footer>Prices and availability change often, so check today\'s price on Amazon.in.<br>#ad | As an Amazon Associate I earn from qualifying purchases.<br>Last updated: <time datetime="{UPDATED_ISO}">{UPDATED_HUMAN}</time><br>© 2026 JC Smart Picks</footer></div></body></html>')
open(os.path.join(OUT,"index.html"),"w",encoding="utf-8").write("\n".join(h)+"\n")

open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
open(os.path.join(OUT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url>\n    <loc>{BASE}</loc>\n    <lastmod>{UPDATED_ISO}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>\n</urlset>\n')
print("products:",len(items))
