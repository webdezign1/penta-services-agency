import re

css_path = 'd:/My Work/Projects/penta-website/assets/app.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Target lines 1087-1111: from .bento{...} to .bx-dash{...}
old_bento_css_regex = r'\.bento\{display:grid;grid-template-columns:repeat\(4,1fr\)[\s\S]*?\.bx-dash div\{display:flex;align-items:center;justify-content:space-between;background:#fff;border-radius:10px;padding:8px 10px\}\.bx-dash b\{display:block;width:45%;height:8px;border-radius:4px;background:#E3EAF2\}'

new_bento_css = '''/* ========== NEXT-LEVEL BENTO ADVANTAGE SECTION ========== */
.bento-sec{background:radial-gradient(900px 500px at 15% 10%,rgba(0,174,239,.14),transparent 60%),radial-gradient(800px 500px at 85% 90%,rgba(16,185,129,.08),transparent 60%),#0A1B2D;position:relative;overflow:hidden;background-image:radial-gradient(rgba(255,255,255,.07) 1px,transparent 1px);background-size:28px 28px}
.bento-sub-badge{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#00AEEF;background:rgba(0,174,239,.12);border:1px solid rgba(0,174,239,.25);padding:7px 16px;border-radius:999px;box-shadow:0 0 20px rgba(0,174,239,.15);margin-bottom:8px}
.bento{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:10px}
.bx{position:relative;display:flex;flex-direction:column;padding:24px 24px 22px;border-radius:22px;background:linear-gradient(175deg,rgba(20,48,80,.85) 0%,rgba(11,28,48,.95) 100%);border:1px solid rgba(255,255,255,.1);box-shadow:inset 0 1px 0 0 rgba(255,255,255,.15),0 16px 36px -10px rgba(0,0,0,.4);text-decoration:none;color:#fff;overflow:hidden;transition:transform .28s cubic-bezier(.16,1,.3,1),border-color .28s ease,box-shadow .28s ease}
.bx:hover{transform:translateY(-5px);border-color:rgba(0,174,239,.6);box-shadow:inset 0 1px 0 0 rgba(255,255,255,.25),0 22px 48px -12px rgba(0,174,239,.25)}
.bx-topline{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.bx-tag{font-size:11px;font-weight:800;letter-spacing:.08em;color:#00AEEF;background:rgba(0,174,239,.1);border:1px solid rgba(0,174,239,.2);padding:4px 10px;border-radius:999px}
.bx-arrow{width:26px;height:26px;border-radius:50%;background:rgba(255,255,255,.06);display:grid;place-items:center;font-size:13px;color:#94A3B8;transition:transform .2s,background .2s,color .2s}
.bx:hover .bx-arrow{transform:translate(2px,-2px);background:#00AEEF;color:#062236}
.bx-art{flex:1;display:flex;flex-direction:column;justify-content:center;min-height:130px;width:100%}
.bx-caption{margin-top:16px}
.bx-caption h3{color:#fff;font-size:1.25rem;font-weight:700;margin:0 0 6px 0;letter-spacing:-.01em}
.bx-caption p{color:#94A3B8;font-size:14.5px;line-height:1.5;margin:0}

/* Grid Layout Spans */
.b1{grid-column:span 2;grid-row:span 2;background:linear-gradient(165deg,rgba(14,42,75,.95) 0%,rgba(8,24,44,.98) 100%)}
.b2{grid-column:span 2}
.b3{grid-column:span 1}
.b4{grid-column:span 1}
.b5{grid-column:span 2}
.b6{grid-column:span 2}
@media (max-width:1024px){.bento{grid-template-columns:1fr 1fr}.b1,.b2,.b5,.b6{grid-column:span 2}.b1{grid-row:auto}}
@media (max-width:640px){.bento{grid-template-columns:1fr}.b1,.b2,.b3,.b4,.b5,.b6{grid-column:auto}}

/* 1. VISUAL STUDIO / BUILDER */
.bx-studio{width:100%;border-radius:14px;background:#0B1928;border:1px solid rgba(255,255,255,.1);overflow:hidden;box-shadow:0 10px 28px rgba(0,0,0,.4)}
.bxs-chrome{display:flex;align-items:center;gap:10px;padding:9px 12px;background:rgba(255,255,255,.04);border-bottom:1px solid rgba(255,255,255,.06);font-size:11px}
.bxs-dots{display:flex;gap:5px}.bxs-dots i{width:9px;height:9px;border-radius:50%;display:inline-block}
.bxs-dots i:nth-child(1){background:#EF4444}.bxs-dots i:nth-child(2){background:#F59E0B}.bxs-dots i:nth-child(3){background:#10B981}
.bxs-url{flex:1;background:rgba(255,255,255,.05);border-radius:6px;padding:3px 10px;color:#A9C2DA;font-family:monospace;font-size:11px;display:flex;align-items:center;gap:6px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.bxs-dev{display:flex;gap:4px}
.bxs-dev-btn{padding:3px 6px;border-radius:4px;display:inline-flex;align-items:center;color:#64748B}
.bxs-dev-btn.active{background:rgba(0,174,239,.18);color:#00AEEF}
.bxs-live-badge{font-size:10px;font-weight:800;color:#10B981;display:flex;align-items:center;gap:5px;letter-spacing:.04em}
.bxs-live-badge i{width:6px;height:6px;border-radius:50%;background:#10B981;box-shadow:0 0 8px #10B981;animation:pulse 2s infinite}
.bxs-body{display:grid;grid-template-columns:36px 1fr;height:240px;background:#0E2238}
.bxs-sidebar{background:rgba(0,0,0,.25);border-right:1px solid rgba(255,255,255,.06);display:flex;flex-direction:column;align-items:center;gap:12px;padding:12px 0}
.bxs-tool{width:26px;height:26px;border-radius:6px;display:grid;place-items:center;color:#64748B;cursor:pointer}
.bxs-tool.on{background:rgba(0,174,239,.2);color:#00AEEF}
.bxs-canvas{padding:14px;display:flex;flex-direction:column;gap:10px;overflow:hidden;position:relative}
.bxs-mini-nav{display:flex;align-items:center;justify-content:space-between;background:rgba(255,255,255,.05);border-radius:6px;padding:5px 10px;font-size:11px}
.bxs-mini-nav b{color:#fff;font-size:11px;letter-spacing:.02em}
.bxs-mini-links{display:flex;gap:10px;color:#94A3B8;font-size:10px}
.bxs-mini-cta{background:#00AEEF;color:#062236;font-weight:700;font-size:10px;padding:2px 8px;border-radius:4px}
.bxs-canvas-content{flex:1;display:flex;align-items:center;justify-content:center}
.bxs-sel-box{width:100%;border:1.5px dashed #00AEEF;border-radius:8px;padding:14px;position:relative;background:rgba(0,174,239,.04)}
.bxs-sel-pill{position:absolute;top:-10px;left:10px;background:#00AEEF;color:#062236;font-size:9.5px;font-weight:800;padding:1px 7px;border-radius:3px;letter-spacing:.04em}
.bxs-hnd{width:5px;height:5px;background:#00AEEF;position:absolute}
.bxs-hnd.tl{top:-3px;left:-3px}.bxs-hnd.tr{top:-3px;right:-3px}.bxs-hnd.bl{bottom:-3px;left:-3px}.bxs-hnd.br{bottom:-3px;right:-3px}
.bxs-cursor{position:absolute;right:20px;bottom:-10px;display:flex;align-items:center;gap:4px;background:#00AEEF;color:#062236;font-size:9.5px;font-weight:800;padding:2px 6px;border-radius:4px;box-shadow:0 4px 10px rgba(0,0,0,.3);z-index:2}
.bxs-tag{font-size:10px;font-weight:700;color:#F59E0B;margin-bottom:4px;letter-spacing:.02em}
.bxs-h{font-size:14px;font-weight:800;color:#fff;line-height:1.3;margin-bottom:10px}
.bxs-btns{display:flex;gap:8px}
.bxs-btn{font-size:10px;font-weight:700;padding:4px 10px;border-radius:5px}
.bxs-btn.bpri{background:#00AEEF;color:#062236}
.bxs-btn.bsec{background:rgba(255,255,255,.08);color:#fff;border:1px solid rgba(255,255,255,.15)}
.bxs-bar-bottom{display:flex;justify-content:space-between;font-size:9.5px;color:#64748B;border-top:1px solid rgba(255,255,255,.06);padding-top:6px}

/* 2. AI ENGINE & CITATIONS */
.bx-ai-engine{display:flex;flex-direction:column;gap:12px;width:100%}
.bx-ai-chips{display:flex;gap:6px;flex-wrap:wrap}
.ai-chip{display:inline-flex;align-items:center;gap:6px;font-size:11.5px;font-weight:700;padding:4px 10px;border-radius:999px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);color:#A9C2DA}
.ai-chip.on{background:rgba(0,174,239,.15);border-color:#00AEEF;color:#fff}
.ai-chip i{width:7px;height:7px;border-radius:50%}
.bx-ai-q{display:flex;align-items:flex-start;gap:8px;background:rgba(0,174,239,.12);border:1px solid rgba(0,174,239,.25);border-radius:12px;padding:8px 12px}
.ai-q-ico{font-size:13px;margin-top:1px}
.bx-ai-q p{color:#E0F2FE;font-size:13px;font-weight:600;margin:0}
.bx-ai-a{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.ai-a-top{display:flex;align-items:center;justify-content:space-between}
.ai-brand-badge{display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:800;color:#00AEEF}
.ai-verified{font-size:10.5px;font-weight:700;color:#10B981;background:rgba(16,185,129,.12);padding:2px 8px;border-radius:999px}
.ai-msg{font-size:12.5px;line-height:1.5;color:#E2E8F0}
.ai-msg strong{color:#00AEEF}
.ai-sources{display:flex;gap:10px;flex-wrap:wrap;border-top:1px solid rgba(255,255,255,.06);padding-top:7px;font-size:11px}
.ai-src{color:#94A3B8}.ai-src b{color:#00AEEF}.ai-src i{color:#10B981;font-style:normal}

/* 3. CORE WEB VITALS / PERFORMANCE */
.bx-perf{display:flex;flex-direction:column;align-items:center;gap:12px;width:100%}
.bx-gauge-wrap{position:relative;width:140px}
.bx-gauge-wrap svg{display:block;width:100%}
.g-glow{animation:gauge 2s ease-out both;filter:drop-shadow(0 0 6px rgba(0,174,239,.5))}
.bx-gauge-center{position:absolute;left:0;right:0;bottom:0;text-align:center}
.bx-gauge-center b{font:800 2.2rem/1 "Bricolage Grotesque",sans-serif;color:#fff;display:block}
.bx-gauge-center small{font-size:9.5px;font-weight:800;letter-spacing:.08em;color:#10B981;display:block;margin-top:2px}
.bx-vitals-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;width:100%}
.v-card{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:8px;padding:6px 4px;text-align:center}
.v-card span{display:block;font-size:10px;font-weight:700;color:#94A3B8}
.v-card b{display:block;font-size:12px;font-weight:800;color:#fff;margin:2px 0}
.v-card small{display:block;font-size:9px;font-weight:700;color:#10B981}
.bx-vitals-foot{font-size:11px;font-weight:700;color:#10B981;display:flex;align-items:center;gap:6px}
.bx-vitals-foot i{width:6px;height:6px;border-radius:50%;background:#10B981;box-shadow:0 0 6px #10B981}

/* 4. MULTI-LOCALE & RTL */
.bx-locale{display:flex;flex-direction:column;gap:10px;width:100%}
.bx-loc-pills{display:flex;gap:4px;flex-wrap:wrap;justify-content:center}
.lp{padding:4px 8px;border-radius:999px;background:rgba(255,255,255,.06);font-size:11px;font-weight:700;color:#94A3B8}
.lp.on{background:#00AEEF;color:#062236}
.lp.rtl-pill{background:rgba(16,185,129,.15);color:#10B981;border:1px solid rgba(16,185,129,.3)}
.bx-loc-box{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:10px 12px;display:flex;flex-direction:column;gap:8px}
.loc-sub small{font-size:9.5px;font-weight:800;color:#00AEEF;letter-spacing:.04em;display:block}
.loc-sub p{margin:2px 0 0;font-size:12px;color:#E2E8F0;font-weight:600}
.loc-sub.rtl{border-top:1px solid rgba(255,255,255,.06);padding-top:6px}
.loc-sub.rtl small{color:#10B981}
.bx-loc-meta{display:flex;justify-content:space-between;font-size:10.5px;font-weight:700;color:#A9C2DA}

/* 5. CLOUD INFRASTRUCTURE */
.bx-cloud{display:flex;flex-direction:column;gap:10px;width:100%}
.cloud-status-bar{display:flex;align-items:center;justify-content:space-between;background:rgba(16,185,129,.1);border:1px solid rgba(16,185,129,.25);border-radius:9px;padding:6px 12px}
.c-online{font-size:11.5px;font-weight:700;color:#10B981;display:flex;align-items:center;gap:6px}
.c-online i{width:7px;height:7px;border-radius:50%;background:#10B981;box-shadow:0 0 6px #10B981;animation:pulse 2s infinite}
.c-region{font-size:10.5px;font-weight:700;color:#94A3B8}
.cloud-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.c-item{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:10px;padding:9px 12px}
.c-icon{flex:none;width:28px;height:28px;border-radius:8px;background:rgba(255,255,255,.06);display:grid;place-items:center}
.c-item b{display:block;font-size:12px;color:#fff;font-weight:700}
.c-item small{display:block;font-size:10.5px;color:#94A3B8}

/* 6. CLIENT PORTAL */
.bx-portal{display:flex;flex-direction:column;gap:10px;width:100%}
.portal-head{display:flex;align-items:center;justify-content:space-between;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:10px;padding:8px 12px}
.portal-user{display:flex;align-items:center;gap:10px}
.portal-av{width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#00AEEF,#10B981);display:grid;place-items:center;font-size:11px;font-weight:800;color:#062236}
.portal-user b{display:block;font-size:12px;color:#fff;font-weight:700}
.portal-user small{display:block;font-size:10px;color:#94A3B8}
.portal-badge{font-size:10.5px;font-weight:800;color:#10B981;background:rgba(16,185,129,.15);padding:3px 8px;border-radius:999px}
.portal-project{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);border-radius:10px;padding:10px 12px;display:flex;flex-direction:column;gap:6px}
.proj-meta{display:flex;align-items:center;justify-content:space-between}
.proj-meta b{font-size:12px;color:#fff;font-weight:700}
.proj-meta small{display:block;font-size:10px;color:#94A3B8}
.proj-pct{font-size:12px;font-weight:800;color:#00AEEF}
.proj-bar{width:100%;height:5px;background:rgba(255,255,255,.08);border-radius:3px;overflow:hidden}
.proj-bar i{display:block;height:100%;background:linear-gradient(90deg,#00AEEF,#10B981);border-radius:3px}
.portal-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.pstat{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.05);border-radius:8px;padding:6px 8px;text-align:center}
.pstat span{display:block;font-size:9.5px;color:#94A3B8}
.pstat b{display:block;font-size:11px;color:#E0F2FE;font-weight:700;margin-top:2px}'''

if re.search(old_bento_css_regex, css):
    css = re.sub(old_bento_css_regex, new_bento_css, css, count=1)
    print("Replaced bento CSS successfully!")
else:
    print("Could not match old bento CSS regex!")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated app.css successfully.")
