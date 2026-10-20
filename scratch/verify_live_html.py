import urllib.request

u = 'https://webdezign1.github.io/penta-services-agency/en/'
req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
print('Has pkgs-primary-grid in live HTML:', 'pkgs-primary-grid' in html)
print('Has pkgs-secondary-grid in live HTML:', 'pkgs-secondary-grid' in html)
print('Has old <div class="pkgs"> in live HTML:', '<div class="pkgs">' in html)
