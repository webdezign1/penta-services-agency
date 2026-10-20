import re

app_js_path = 'd:/My Work/Projects/penta-website/assets/app.js'

with open(app_js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Define the new pkgCard and pkgCards functions
new_pkg_code = '''function pkgCard(p, i){
  let price;
  const ann = state.billing === "annual";
  if(p.svc){
    const T = totals(p.svc.map(id=>({kind:"svc",id,qty:1})), state.billing || "monthly");
    price = `<div class="price-hero">
      <div class="ph-top">
        <span class="ph-from">${t("from")}</span>
        ${T.promo ? `<span class="ph-save-badge">Save ${Math.round(PROMO.rate*100)}%</span>` : ""}
      </div>
      <div class="ph-amount">
        <b>${money(T.setupNet)}</b>
        ${T.promo ? strike(T.setupNet + T.promo*(1-T.rate)) : ""}
        <span class="ph-setup">${t("setup")}</span>
      </div>
      <div class="ph-recurring">
        <span>+</span>
        <strong>${money(T.moNet)}</strong>
        <span class="ph-per-cycle">${ann ? t("per_year") : t("per_month")}</span>
        <span class="ph-cloud-pill">⚡ Cloud + SSL + Care</span>
      </div>
    </div>`;
  } else {
    price = `<div class="price-hero custom-hero">
      <div class="ph-top">
        <span class="ph-from">${t("from")}</span>
        <span class="ph-save-badge bespoke">Tailored SLA</span>
      </div>
      <div class="ph-amount">
        <b>${t("by_proposal")}</b>
      </div>
      <div class="ph-recurring">
        <span>${t("ps1h")} → ${t("ps3h")}</span>
        <span class="ph-cloud-pill">NDA Included</span>
      </div>
    </div>`;
  }

  const all = p.svc && p.svc.every(inCart);
  const setupItems = t(p.x).split(/\\s*[,，、،]\\s*/);
  const moItems = p.svc ? p.svc.flatMap(id => moInc(id)) : [];

  return `<article class="pkg-card ${p.hot ? "is-featured" : ""} tier-${p.tier.toLowerCase()}">
    ${p.hot ? `<div class="pkg-popular-banner"><span>★ ${t("popular")}</span></div>` : ""}
    <div class="pkg-card-head">
      <div class="tier-pill-row">
        <span class="tier-badge">${t(p.tier)}</span>
        ${p.hot ? `<span class="tier-rating">Rated #1 Choice</span>` : ""}
      </div>
      <h3 class="tier-title">${t(p.n)}</h3>
      <p class="tier-desc">${t(p.f)}</p>
    </div>

    <div class="pkg-price-hero">${price}</div>

    <div class="pkg-cta-block">
      ${p.svc 
        ? `<button class="btn ${p.hot ? "btn-accent pkg-btn-hero" : "btn-primary pkg-btn-hero"}" data-action="pkgadd" data-i="${i}">
            ${all ? "✓ " + t("added") : t("add_to_cart")}
           </button>
           <button class="pkg-link-quote" data-action="quote" data-s="${p.svc[0]}">
             ${t("quote")} ›
           </button>`
        : `<a class="btn btn-accent pkg-btn-hero" href="#/proposal">${t("req_btn")} ›</a>
           <span class="pkg-link-quote" style="cursor:default">Guaranteed quote within 1 business day</span>`
      }
    </div>

    <div class="pkg-divider">
      <span>What's included</span>
    </div>

    <div class="pkg-features-wrap">
      <div class="feat-subgroup">
        <span class="feat-subhead">Build & Launch Deliverables</span>
        <ul class="feat-checklist">
          ${setupItems.map(item => `<li><svg class="ck-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="9" fill="rgba(0,174,239,0.12)"/><path d="M6 10l3 3 5-6" stroke="#00AEEF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>${esc(item)}</span></li>`).join("")}
        </ul>
      </div>

      ${moItems.length ? `
        <div class="feat-subgroup">
          <span class="feat-subhead">Included Cloud & Monthly Care</span>
          <ul class="feat-checklist monthly-checklist">
            ${moItems.map(item => `<li><svg class="ck-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="9" fill="rgba(16,185,129,0.12)"/><path d="M6 10l3 3 5-6" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>${esc(item)}</span></li>`).join("")}
          </ul>
        </div>
      ` : `
        <div class="feat-subgroup">
          <span class="feat-subhead">Enterprise Architecture & SLA</span>
          <ul class="feat-checklist monthly-checklist">
            <li><svg class="ck-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="9" fill="rgba(16,185,129,0.12)"/><path d="M6 10l3 3 5-6" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Dedicated Solutions Architect & Technical Lead</span></li>
            <li><svg class="ck-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="9" fill="rgba(16,185,129,0.12)"/><path d="M6 10l3 3 5-6" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Full IP Ownership & Clean Scalable Codebase</span></li>
            <li><svg class="ck-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="9" fill="rgba(16,185,129,0.12)"/><path d="M6 10l3 3 5-6" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Custom Microservices & Third-Party API Integrations</span></li>
            <li><svg class="ck-icon" viewBox="0 0 20 20" fill="none"><circle cx="10" cy="10" r="9" fill="rgba(16,185,129,0.12)"/><path d="M6 10l3 3 5-6" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Enterprise 99.99% High-Availability SLA</span></li>
          </ul>
        </div>
      `}
    </div>
  </article>`;
}

function pkgCards(){
  const top3 = PKGS.slice(0, 3).map((p, i) => pkgCard(p, i)).join("");
  const bottom2 = PKGS.slice(3).map((p, i) => pkgCard(p, i + 3)).join("");
  return `<div class="pkgs-primary-grid">${top3}</div>
  <div class="pkgs-divider-band">
    <div class="pdb-line"></div>
    <span class="pdb-tag"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg> SPECIALIZED GROWTH & ENTERPRISE ARCHITECTURE</span>
    <div class="pdb-line"></div>
  </div>
  <div class="pkgs-secondary-grid">${bottom2}</div>`;
}'''

# Replace old pkgCards
old_pkg_regex = r'function pkgCards\(\)\{[\s\S]*?return PKGS\.map\([\s\S]*?\}\)\.join\(""\);\s*\}'
if re.search(old_pkg_regex, code):
    code = re.sub(old_pkg_regex, lambda m: new_pkg_code, code, count=1)
    print("Replaced pkgCards with new pkgCard & pkgCards structure!")
else:
    print("Could not match old pkgCards!")

# Replace section markup in pageHome
old_sec_regex = r'<section class="sec"><div class="wrap"><div class="sec-h center"><span class="sub-badge"[\s\S]*?<div class="pkgs">\$\{pkgCards\(\)\}</div>[\s\S]*?<a class="btn btn-ghost" href="#/pricing">\$\{t\("cta_pricing"\)\}</a><span class="note">\$\{t\("bundle_note"\)\}</span></p></div></section>'

new_sec_markup = '''<section class="sec pkg-section" id="pricing-packages"><div class="wrap">
  <div class="sec-h center">
   <span class="sub-badge bento-sub-badge"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg> Transparent Investment · Fixed Starting Scope</span>
   <h2 style="font-size:clamp(2rem,3.6vw,3.1rem);letter-spacing:-0.03em;margin-top:10px">${t("pkg_h")}</h2>
   <p style="max-width:680px;margin:10px auto 18px;font-size:16.5px;color:var(--ink-2);line-height:1.6">${t("pkg_p")}</p>
   <div class="billing-toggle-container">${billingSeg()}</div>
  </div>
  <div class="pkgs-container">${pkgCards()}</div>
  <div class="pkgs-bottom-bar">
   <a class="btn btn-ghost" href="#/pricing">${t("cta_pricing")} ›</a>
   <span class="pkg-bundle-hint">🎁 ${t("bundle_note")}</span>
  </div>
 </div></section>'''

if re.search(old_sec_regex, code):
    code = re.sub(old_sec_regex, lambda m: new_sec_markup, code, count=1)
    print("Replaced packages section markup successfully!")
else:
    print("Could not match old packages section markup!")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved app.js successfully.")
