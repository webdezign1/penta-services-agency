css_path = 'd:/My Work/Projects/penta-website/assets/app.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_b1_styles = '''/* B1 Hero Card Top Header & Fillers */
.b1-head {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 12px;
}
.b1-head h3 {
  font-size: 1.55rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #ffffff;
  margin: 0;
  line-height: 1.25;
}
.b1-head p {
  color: #A9C2DA;
  font-size: 14.5px;
  line-height: 1.5;
  margin: 0;
}
.b1-badges {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 4px;
}
.b1-badges span {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.04em;
  color: #38bdf8;
  background: rgba(0, 174, 239, 0.12);
  border: 1px solid rgba(0, 174, 239, 0.25);
  padding: 4px 10px;
  border-radius: 999px;
}
.b1-palette {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  background: rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 8px 12px;
  margin-bottom: 14px;
}
.b1-pal-lbl {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #94A3B8;
}
.b1-chip {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px dashed rgba(255, 255, 255, 0.15);
  color: #E2E8F0;
  transition: all 0.2s ease;
}
.b1-chip.active {
  background: rgba(0, 174, 239, 0.2);
  border: 1px solid #00AEEF;
  color: #00AEEF;
  box-shadow: 0 0 10px rgba(0, 174, 239, 0.25);
}
.bx:hover .b1-chip.active {
  background: #00AEEF;
  color: #062236;
}
.b1-art {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: stretch;
  min-height: 250px;
}
.b1-art .bx-studio {
  flex: 1;
  display: flex;
  flex-direction: column;
}
.b1-art .bxs-body {
  flex: 1;
  height: auto;
  min-height: 220px;
}
.b1-foot {
  margin-top: 14px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}
.b1-cta {
  font-size: 13px;
  font-weight: 800;
  color: #00AEEF;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  transition: transform 0.2s;
}
.bx:hover .b1-cta {
  transform: translateX(4px);
  color: #38bdf8;
}

'''

target = '/* 1. VISUAL STUDIO / BUILDER */'
if target in css and '.b1-head' not in css:
    css = css.replace(target, new_b1_styles + target)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added b1 styles to app.css successfully!")
else:
    print("Already added or target not found.")
