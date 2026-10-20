with open('d:/My Work/Projects/penta-website/assets/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Line 1470 before:', lines[1469])
if 'st_active' in lines[1469]:
    lines[1469] = '</div>`}\n'
    print('Fixed line 1470!')

with open('d:/My Work/Projects/penta-website/assets/app.js', 'w', encoding='utf-8') as f:
    f.writelines(lines)
