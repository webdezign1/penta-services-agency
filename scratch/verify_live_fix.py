import urllib.request

u = 'https://webdezign1.github.io/penta-services-agency/assets/app.js'
req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
res = urllib.request.urlopen(req)
text = res.read().decode('utf-8')
print('Has st_active error:', 'st_active":n===2' in text)
print('Has pkgs-primary-grid:', 'pkgs-primary-grid' in text)
