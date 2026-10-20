with open('d:/My Work/Projects/penta-website/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="app"')
print('Position of id="app":', pos)
if pos != -1:
    print('Context:')
    print(text[pos:pos+500])
