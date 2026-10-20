import re

app_js_path = 'd:/My Work/Projects/penta-website/assets/app.js'

with open(app_js_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the bento grid mapping in pageHome
old_mapping_regex = r'<div class="bento">\$\{\[1,2,3,4,5,6\]\.map\(i=>\{[\s\S]*?\}\)\.join\(""\)\}</div>'

new_mapping = '''<div class="bento">${[1,2,3,4,5,6].map(i=>{
    const tags=["VISUAL STUDIO","AI & GEO VISIBILITY","CORE WEB VITALS","GLOBAL LOCALIZATION","MANAGED CLOUD","EXECUTIVE PORTAL"];
    if(i===1){
      return `<a class="bx b1" href="#/builder">
       <div class="bx-topline"><span class="bx-tag">${tags[0]}</span><span class="bx-arrow">↗</span></div>
       <div class="b1-head">
        <h3>${t("b1h")}</h3>
        <p>${t("b1p")}</p>
        <div class="b1-badges">
         <span>✦ 50+ Sector Themes</span>
         <span>✦ Drag & Drop Editor</span>
         <span>✦ Free Draft Saving</span>
        </div>
       </div>
       <div class="b1-palette">
        <span class="b1-pal-lbl">Add Section:</span>
        <span class="b1-chip active">Hero Header</span>
        <span class="b1-chip">Features</span>
        <span class="b1-chip">Work Gallery</span>
        <span class="b1-chip">Pricing</span>
        <span class="b1-chip">+ Custom Block</span>
       </div>
       <div class="bx-art b1-art">${bentoArt(1)}</div>
       <div class="b1-foot"><span class="b1-cta">Launch Free Interactive Builder ›</span></div>
      </a>`;
    }
    return `<a class="bx b${i}" href="${["#/builder","#/service/geo","#/service/security","#/service/intl","#/service/hosting","#/dashboard"][i-1]}">
     <div class="bx-topline"><span class="bx-tag">${tags[i-1]}</span><span class="bx-arrow">↗</span></div>
     <div class="bx-art">${bentoArt(i)}</div>
     <div class="bx-caption"><h3>${t("b"+i+"h")}</h3><p>${t("b"+i+"p")}</p></div>
    </a>`;
  }).join("")}</div>'''

if re.search(old_mapping_regex, text):
    text = re.sub(old_mapping_regex, lambda m: new_mapping, text, count=1)
    print("Replaced bento mapping in app.js successfully!")
else:
    print("Could not match old bento mapping regex!")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved app.js successfully.")
