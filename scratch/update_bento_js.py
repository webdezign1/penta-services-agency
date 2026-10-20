import re

app_js_path = 'd:/My Work/Projects/penta-website/assets/app.js'

with open(app_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new bentoArt function
new_bento_art = '''function bentoArt(i){
 if(i===1)return `<div class="bx-studio">
  <div class="bxs-chrome">
    <div class="bxs-dots"><i></i><i></i><i></i></div>
    <div class="bxs-url"><span>🔒</span> preview.penta.studio/artisan-bakery</div>
    <div class="bxs-dev">
      <span class="bxs-dev-btn active" title="Desktop"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></span>
      <span class="bxs-dev-btn" title="Mobile"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12" y2="18"/></svg></span>
    </div>
    <span class="bxs-live-badge"><i></i> 60fps Sync</span>
  </div>
  <div class="bxs-body">
    <div class="bxs-sidebar">
      <span class="bxs-tool on" title="Layers"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg></span>
      <span class="bxs-tool" title="Typography"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="4 7 4 4 20 4 20 7"/><line x1="9" y1="20" x2="15" y2="20"/><line x1="12" y1="4" x2="12" y2="20"/></svg></span>
      <span class="bxs-tool" title="Colors"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 10 10 0 0 0 0-20"/></svg></span>
      <span class="bxs-tool" title="Components"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg></span>
    </div>
    <div class="bxs-canvas">
      <div class="bxs-mini-nav">
        <b>Artisan Bakery</b>
        <div class="bxs-mini-links"><span>Home</span><span>Menu</span><span>Story</span></div>
        <span class="bxs-mini-cta">Order Now</span>
      </div>
      <div class="bxs-canvas-content">
        <div class="bxs-sel-box">
          <div class="bxs-sel-pill">&lt;HeroSection&gt; · Drag & Drop Live</div>
          <div class="bxs-hnd tl"></div><div class="bxs-hnd tr"></div><div class="bxs-hnd bl"></div><div class="bxs-hnd br"></div>
          <div class="bxs-cursor"><svg width="13" height="13" viewBox="0 0 24 24" fill="#00AEEF"><path d="M3 3l7 18 3-7 7-3L3 3z"/></svg><span>Sarah · Lead</span></div>
          <div class="bxs-tag">★ Organic Sourdough & Specialty Coffee</div>
          <div class="bxs-h">Handmade daily in Mayfair with wild fermentation</div>
          <div class="bxs-btns">
            <span class="bxs-btn bpri">Reserve Table ›</span>
            <span class="bxs-btn bsec">View Daily Bakes</span>
          </div>
        </div>
      </div>
      <div class="bxs-bar-bottom">
        <span>⚡ Autosaved</span>
        <span>📐 Responsive 12-Col</span>
        <span>🎨 Playfair + Montserrat</span>
      </div>
    </div>
  </div>
</div>`;
 if(i===2)return `<div class="bx-ai-engine">
  <div class="bx-ai-chips">
    <span class="ai-chip"><i style="background:#10A37F"></i> ChatGPT 4o</span>
    <span class="ai-chip"><i style="background:#1B90FF"></i> Google Gemini</span>
    <span class="ai-chip on"><i style="background:#20B2AA"></i> Perplexity Pro</span>
    <span class="ai-chip"><i style="background:#8B5CF6"></i> Claude 3.5</span>
  </div>
  <div class="bx-ai-q">
    <span class="ai-q-ico">🔍</span>
    <p>${t("b_ai_q")}</p>
  </div>
  <div class="bx-ai-a">
    <div class="ai-a-top">
      <span class="ai-brand-badge">${logoSVG(14)} AI Knowledge Synthesis</span>
      <span class="ai-verified">Verified Top Citation [1]</span>
    </div>
    <div class="ai-msg">
      <strong>Penta Services</strong> is ranked as the leading multilingual web agency in London and Milan. Specializing in high-performance websites with built-in GEO (Generative Engine Optimization) that are natively indexed by ChatGPT, Perplexity, and Gemini.
    </div>
    <div class="ai-sources">
      <span class="ai-src"><b>[1]</b> pentaservices.co.uk <i>✓ Primary Citation</i></span>
      <span class="ai-src"><b>[2]</b> London Web Directory 2026</span>
    </div>
  </div>
</div>`;
 if(i===3)return `<div class="bx-perf">
  <div class="bx-gauge-wrap">
    <svg viewBox="0 0 120 70">
      <defs>
        <linearGradient id="gaugeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#00AEEF"/>
          <stop offset="100%" stop-color="#10B981"/>
        </linearGradient>
      </defs>
      <path d="M10 64 A50 50 0 0 1 110 64" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="10" stroke-linecap="round"/>
      <path class="g-glow" d="M10 64 A50 50 0 0 1 110 64" fill="none" stroke="url(#gaugeGrad)" stroke-width="10" stroke-linecap="round" pathLength="100" stroke-dasharray="99 100"/>
    </svg>
    <div class="bx-gauge-center">
      <b>99</b>
      <small>LIGHTHOUSE</small>
    </div>
  </div>
  <div class="bx-vitals-grid">
    <div class="v-card"><span>LCP</span><b>0.6s</b><small>⚡ Fast</small></div>
    <div class="v-card"><span>FID</span><b>4ms</b><small>⚡ Instant</small></div>
    <div class="v-card"><span>CLS</span><b>0.00</b><small>⚡ Zero Shift</small></div>
  </div>
  <div class="bx-vitals-foot"><i></i> All Core Web Vitals Passed</div>
</div>`;
 if(i===4)return `<div class="bx-locale">
  <div class="bx-loc-pills">
    <span class="lp on">🇬🇧 EN</span>
    <span class="lp">🇮🇹 IT</span>
    <span class="lp">🇫🇷 FR</span>
    <span class="lp rtl-pill">🇦🇪 العربية</span>
    <span class="lp">🇨🇳 中文</span>
  </div>
  <div class="bx-loc-box">
    <div class="loc-sub">
      <small>LTR · English Global</small>
      <p>Turn visitors into clients worldwide.</p>
    </div>
    <div class="loc-sub rtl" dir="rtl">
      <small>RTL · Bi-directional Arabic</small>
      <p>حوّل الزوار إلى عملاء في جميع أنحاء العالم.</p>
    </div>
  </div>
  <div class="bx-loc-meta">
    <span>🌐 Auto-Locale GeoIP</span>
    <span>⚡ Instant RTL Flip</span>
  </div>
</div>`;
 if(i===5)return `<div class="bx-cloud">
  <div class="cloud-status-bar">
    <span class="c-online"><i></i> All Systems 100% Operational</span>
    <span class="c-region">AWS Global Edge</span>
  </div>
  <div class="cloud-grid">
    <div class="c-item">
      <div class="c-icon" style="color:#00AEEF"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg></div>
      <div><b>Global Edge CDN</b><small>35+ PoPs · 12ms latency</small></div>
    </div>
    <div class="c-item">
      <div class="c-icon" style="color:#10B981"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
      <div><b>SSL / TLS 1.3</b><small>A+ Rating · Auto-Renew</small></div>
    </div>
    <div class="c-item">
      <div class="c-icon" style="color:#F59E0B"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg></div>
      <div><b>Daily Backups</b><small>Automated Cloud Snapshots</small></div>
    </div>
    <div class="c-item">
      <div class="c-icon" style="color:#A78BFA"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg></div>
      <div><b>DDoS Guard</b><small>Layer 7 Enterprise Shield</small></div>
    </div>
  </div>
</div>`;
 return `<div class="bx-portal">
  <div class="portal-head">
    <div class="portal-user">
      <span class="portal-av">PS</span>
      <div><b>Mayfair Group Ltd</b><small>Client ID: #PNT-8842</small></div>
    </div>
    <span class="portal-badge">Active SLA</span>
  </div>
  <div class="portal-project">
    <div class="proj-meta">
      <div><b>Corporate Web & GEO Campaign</b><small>Phase 4: Live & Monitored</small></div>
      <span class="proj-pct">100%</span>
    </div>
    <div class="proj-bar"><i style="width:100%"></i></div>
  </div>
  <div class="portal-stats">
    <div class="pstat"><span>Next Renewal</span><b>Included in Plan</b></div>
    <div class="pstat"><span>Monthly Invoices</span><b>Paid (1-Click PDF)</b></div>
    <div class="pstat"><span>Project Lead</span><b>Sarah H. (London)</b></div>
  </div>
</div>`}'''

# Find original bentoArt function
old_bento_art_regex = r'function bentoArt\(i\)\{[\s\S]*?return `<div class="bx-dash"[\s\S]*?\}'
if re.search(old_bento_art_regex, content):
    content = re.sub(old_bento_art_regex, new_bento_art, content, count=1)
    print("Replaced bentoArt successfully!")
else:
    print("Could not match old bentoArt!")

# Replace the bento section in pageHome
old_sec = r'<section class="sec navy"><div class="wrap"><div class="sec-h"><h2>\$\{t\("bento_h"\)\}</h2><p>\$\{t\("bento_p"\)\}</p></div><div class="bento">\$\{\[1,2,3,4,5,6\]\.map\(i=>`<a class="bx b\$\{i\}" href="\$\{\["#/builder","#/service/geo","#/service/security","#/service/intl","#/service/hosting","#/dashboard"\]\[i-1\]\}"><div class="bx-art">\$\{bentoArt\(i\)\}</div><h3>\$\{t\("b"\+i\+"h"\)\}</h3><p>\$\{t\("b"\+i\+"p"\)\}</p></a>`\)\.join\(""\)\}</div></div></section>'

new_sec = '''<section class="sec navy bento-sec" id="advantage"><div class="wrap">
  <div class="sec-h center">
   <span class="sub-badge bento-sub-badge"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg> COMPLETE DIGITAL ADVANTAGE</span>
   <h2 style="font-size:clamp(2rem,3.6vw,3.1rem);letter-spacing:-0.03em;margin-top:10px">${t("bento_h")}</h2>
   <p style="max-width:680px;margin:12px auto 0;font-size:16.5px;color:#A9C2DA;line-height:1.6">${t("bento_p")}</p>
  </div>
  <div class="bento">${[1,2,3,4,5,6].map(i=>{
    const tags=["VISUAL STUDIO","AI & GEO VISIBILITY","CORE WEB VITALS","GLOBAL LOCALIZATION","MANAGED CLOUD","EXECUTIVE PORTAL"];
    return `<a class="bx b${i}" href="${["#/builder","#/service/geo","#/service/security","#/service/intl","#/service/hosting","#/dashboard"][i-1]}">
     <div class="bx-topline"><span class="bx-tag">${tags[i-1]}</span><span class="bx-arrow">↗</span></div>
     <div class="bx-art">${bentoArt(i)}</div>
     <div class="bx-caption"><h3>${t("b"+i+"h")}</h3><p>${t("b"+i+"p")}</p></div>
    </a>`;
  }).join("")}</div>
 </div></section>'''

if re.search(old_sec, content):
    content = re.sub(old_sec, new_sec, content, count=1)
    print("Replaced bento section successfully!")
else:
    print("Could not match old bento section!")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app.js successfully.")
