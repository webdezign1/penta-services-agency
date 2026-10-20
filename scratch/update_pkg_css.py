import re

css_path = 'd:/My Work/Projects/penta-website/assets/app.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_pkg_css = '''/* ==================== NEXT-LEVEL PACKAGES & PRICING REDESIGN ==================== */
.pkg-section {
  background: radial-gradient(1100px 500px at 50% 0%, rgba(0, 174, 239, 0.06), transparent 70%), var(--bg);
  position: relative;
  overflow: hidden;
  padding: 80px 0 90px;
}
.billing-toggle-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 22px 0 10px;
}
.billing-toggle-container .seg {
  display: inline-flex;
  background: rgba(14, 42, 71, 0.06);
  border: 1px solid rgba(14, 42, 71, 0.12);
  border-radius: 999px;
  padding: 4px;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.03);
}
.billing-toggle-container .seg button {
  padding: 9px 22px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 13.5px;
  border: none;
  background: transparent;
  color: var(--ink-2);
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.billing-toggle-container .seg button[aria-pressed="true"] {
  background: #00AEEF;
  color: #062236;
  box-shadow: 0 4px 14px rgba(0, 174, 239, 0.35);
  font-weight: 800;
}
.pkgs-container {
  margin-top: 32px;
}
.pkgs-primary-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  align-items: stretch;
}
.pkgs-divider-band {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 44px 0 24px;
}
.pdb-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(14, 42, 71, 0.14), transparent);
}
.pdb-tag {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #0284c7;
  background: rgba(0, 174, 239, 0.08);
  border: 1px solid rgba(0, 174, 239, 0.22);
  padding: 7px 18px;
  border-radius: 999px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 2px 8px rgba(0, 174, 239, 0.08);
}
.pkgs-secondary-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  align-items: stretch;
}

/* Individual Package Card */
.pkg-card {
  background: var(--surface, #ffffff);
  border: 1px solid rgba(14, 42, 71, 0.1);
  border-radius: 24px;
  padding: 30px 24px 26px;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 24px -6px rgba(14, 42, 71, 0.06);
}
.pkg-card:hover {
  transform: translateY(-7px);
  box-shadow: 0 24px 48px -12px rgba(0, 174, 239, 0.2), 0 0 0 1px rgba(0, 174, 239, 0.4);
  border-color: rgba(0, 174, 239, 0.4);
}

/* Featured / Spotlight Card (Corporate) */
.pkg-card.is-featured {
  background: linear-gradient(165deg, #081B2E 0%, #0E2946 45%, #143A63 100%);
  border: 2px solid #00AEEF;
  color: #F0F7FD;
  --ink: #ffffff;
  --ink-2: #B0CCE6;
  box-shadow: 0 26px 60px -12px rgba(0, 174, 239, 0.42), inset 0 1px 0 rgba(255, 255, 255, 0.2);
  transform: translateY(-8px);
  z-index: 2;
}
.pkg-card.is-featured:hover {
  transform: translateY(-14px);
  box-shadow: 0 34px 72px -15px rgba(0, 174, 239, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

/* Popular Banner */
.pkg-popular-banner {
  position: absolute;
  top: -14px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #00AEEF 0%, #0077b6 100%);
  color: #ffffff;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 6px 18px;
  border-radius: 999px;
  box-shadow: 0 6px 20px rgba(0, 174, 239, 0.5);
  white-space: nowrap;
}

/* Card Header */
.pkg-card-head {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.tier-pill-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 2px;
}
.tier-badge {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(0, 174, 239, 0.1);
  color: #0284c7;
  border: 1px solid rgba(0, 174, 239, 0.2);
}
.is-featured .tier-badge {
  background: rgba(0, 174, 239, 0.25);
  color: #38bdf8;
  border-color: rgba(56, 189, 248, 0.4);
}
.tier-rating {
  font-size: 11px;
  font-weight: 800;
  color: #10B981;
  background: rgba(16, 185, 129, 0.12);
  padding: 3px 8px;
  border-radius: 999px;
}
.tier-title {
  font-size: 1.45rem;
  font-weight: 800;
  margin: 0;
  letter-spacing: -0.02em;
  line-height: 1.25;
  color: var(--ink);
}
.tier-desc {
  font-size: 13.5px;
  color: var(--ink-2);
  line-height: 1.45;
  margin: 0;
  min-height: 38px;
}

/* Price Hero Block */
.pkg-price-hero {
  margin: 16px 0 14px;
}
.price-hero {
  background: rgba(0, 174, 239, 0.04);
  border: 1px solid rgba(0, 174, 239, 0.12);
  border-radius: 16px;
  padding: 16px 18px;
}
.is-featured .price-hero {
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(255, 255, 255, 0.16);
}
.ph-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 4px;
}
.ph-from {
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--ink-2);
}
.ph-save-badge {
  font-size: 10.5px;
  font-weight: 800;
  color: #10B981;
  background: rgba(16, 185, 129, 0.12);
  border: 1px solid rgba(16, 185, 129, 0.25);
  padding: 2px 8px;
  border-radius: 999px;
}
.ph-save-badge.bespoke {
  color: #A78BFA;
  background: rgba(167, 139, 250, 0.12);
  border-color: rgba(167, 139, 250, 0.25);
}
.ph-amount {
  display: flex;
  align-items: baseline;
  gap: 8px;
  flex-wrap: wrap;
}
.ph-amount b {
  font: 800 2.2rem/1.1 "Bricolage Grotesque", var(--disp);
  color: var(--ink);
  letter-spacing: -0.03em;
}
.ph-setup {
  font-size: 13px;
  font-weight: 700;
  color: var(--ink-2);
}
.ph-recurring {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 6px;
  font-size: 13px;
  color: var(--ink-2);
}
.ph-recurring strong {
  color: #0284c7;
  font-weight: 800;
  font-size: 14px;
}
.is-featured .ph-recurring strong {
  color: #38bdf8;
}
.ph-cloud-pill {
  font-size: 10.5px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 999px;
  background: rgba(16, 185, 129, 0.12);
  color: #059669;
  border: 1px solid rgba(16, 185, 129, 0.25);
}
.is-featured .ph-cloud-pill {
  background: rgba(16, 185, 129, 0.22);
  color: #34d399;
  border-color: rgba(52, 211, 153, 0.35);
}

/* CTA Action Block */
.pkg-cta-block {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.pkg-btn-hero {
  width: 100%;
  border-radius: 12px;
  font-weight: 800;
  font-size: 14.5px;
  padding: 13px 20px;
  transition: all 0.25s ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  cursor: pointer;
}
.pkg-btn-hero.btn-accent {
  background: linear-gradient(135deg, #00AEEF 0%, #0088cc 100%);
  color: #ffffff !important;
  border: none;
  box-shadow: 0 4px 16px -2px rgba(0, 174, 239, 0.5);
}
.pkg-btn-hero.btn-accent:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px -2px rgba(0, 174, 239, 0.65);
}
.pkg-btn-hero.btn-primary {
  background: #0E2A47;
  color: #ffffff !important;
  border: 1px solid #0E2A47;
}
.pkg-btn-hero.btn-primary:hover {
  background: #173e66;
  border-color: #173e66;
  transform: translateY(-2px);
}
.pkg-link-quote {
  background: none;
  border: none;
  color: var(--ink-2);
  font-size: 12.5px;
  font-weight: 700;
  text-align: center;
  cursor: pointer;
  transition: color 0.2s;
  padding: 4px;
}
.pkg-link-quote:hover {
  color: #00AEEF;
}

/* Divider */
.pkg-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 18px 0 14px;
  position: relative;
}
.pkg-divider::before {
  content: "";
  position: absolute;
  inset: 50% 0 auto 0;
  height: 1px;
  background: rgba(14, 42, 71, 0.1);
}
.is-featured .pkg-divider::before {
  background: rgba(255, 255, 255, 0.14);
}
.pkg-divider span {
  position: relative;
  background: var(--surface, #ffffff);
  padding: 0 10px;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ink-2);
}
.is-featured .pkg-divider span {
  background: #0E2A47;
  color: #B0CCE6;
}

/* Features Wrap */
.pkg-features-wrap {
  display: flex;
  flex-direction: column;
  gap: 16px;
  flex: 1;
}
.feat-subgroup {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.feat-subhead {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ink-2);
  display: block;
}
.feat-checklist {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 9px;
}
.feat-checklist li {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 13.5px;
  line-height: 1.4;
  color: var(--ink);
}
.is-featured .feat-checklist li {
  color: #F0F7FD;
}
.ck-icon {
  flex: none;
  width: 18px;
  height: 18px;
  margin-top: 1px;
}

/* Bottom Bar */
.pkgs-bottom-bar {
  margin-top: 36px;
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: center;
  justify-content: center;
}
.pkg-bundle-hint {
  font-size: 14.5px;
  font-weight: 700;
  color: var(--ink-2);
  background: rgba(14, 42, 71, 0.04);
  border: 1px solid rgba(14, 42, 71, 0.08);
  padding: 8px 16px;
  border-radius: 999px;
}

/* Responsive Grid */
@media (max-width: 1060px) {
  .pkgs-primary-grid {
    grid-template-columns: 1fr;
    max-width: 520px;
    margin-inline: auto;
  }
  .pkgs-secondary-grid {
    grid-template-columns: 1fr;
    max-width: 520px;
    margin-inline: auto;
  }
}'''

# Replace from /* ==================== PACKAGES SECTION REDESIGN ==================== */ up to /* tools */
old_block_regex = r'/\* ==================== PACKAGES SECTION REDESIGN ==================== \*/[\s\S]*?(?=/\* tools \*/)'

if re.search(old_block_regex, css):
    css = re.sub(old_block_regex, lambda m: new_pkg_css + '\n', css, count=1)
    print("Replaced packages CSS successfully!")
else:
    print("Could not match old packages CSS regex!")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Saved app.css successfully.")
