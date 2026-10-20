with open('d:/My Work/Projects/penta-website/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('class="bento"')
if pos == -1:
    pos = text.find('bento')
print('Index:', pos)
if pos != -1:
    print(text[pos-100:pos+300])
