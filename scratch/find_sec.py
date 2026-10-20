with open('d:/My Work/Projects/penta-website/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('<div class="pkgs">')
print('Index of <div class="pkgs">:', pos)
sec_start = text.rfind('<section', 0, pos)
sec_end = text.find('</section>', pos) + 10
print('Start:\n', text[sec_start:sec_start+200])
print('End:\n', text[sec_end-200:sec_end])
