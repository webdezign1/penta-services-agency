import os

with open('d:/My Work/Projects/penta-website/scratch/pkg_sec.html', 'r', encoding='utf-8') as f:
    pkg_sec_html = f.read()

updated_count = 0
for root, dirs, files in os.walk('d:/My Work/Projects/penta-website'):
    if '.git' in root or 'node_modules' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pos = content.find('<div class="pkgs">')
            if pos != -1:
                sec_start = content.rfind('<section', 0, pos)
                sec_end = content.find('</section>', pos) + 10
                if sec_start != -1 and sec_end > sec_start:
                    new_content = content[:sec_start] + pkg_sec_html + content[sec_end:]
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated_count += 1
                    print(f'Updated: {filepath}')

print(f'Total HTML files updated with new static pricing section: {updated_count}')
