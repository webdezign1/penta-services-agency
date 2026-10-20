import re, os

with open('d:/My Work/Projects/penta-website/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

block = "".join(lines[2303:2437])
mock_ids = re.findall(r'id:"([^"]+)"', block)
print(f"Total template IDs found: {len(mock_ids)}")

local_files = set(os.listdir('d:/My Work/Projects/penta-website/assets/tpl'))

missing = []
for mid in mock_ids:
    for variant in ['hero.webp', 'hero-s.webp', 's1.webp', 's2.webp']:
        fn = f"{mid}-{variant}"
        if fn not in local_files:
            missing.append(fn)

print(f"Missing hero/s1/s2 files locally: {len(missing)}")
if missing:
    print("Samples:", missing[:15])

# Also check how many images total are in assets/tpl
print(f"Total files in assets/tpl: {len(local_files)}")
