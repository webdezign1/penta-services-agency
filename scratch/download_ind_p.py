import urllib.request, os

target_dir = 'd:/My Work/Projects/penta-website/assets/tpl'
en_dir = 'd:/My Work/Projects/penta-website/en/assets/tpl'

industries = ['corporate', 'creative', 'education', 'entertainment', 'nonprofit', 'technology', 'wedding', 'healthcare', 'legal', 'finance', 'tech', 'construction', 'fitness', 'beauty', 'retail', 'automotive', 'hospitality', 'architecture', 'realestate', 'ecommerce', 'blog', 'mobile', 'other']

downloaded = 0
for ind in industries:
    for n in range(1, 7):
        fn = f"{ind}-p{n}.webp"
        fp = os.path.join(target_dir, fn)
        if os.path.exists(fp):
            continue
        url = f"https://pentaservices.co.uk/assets/tpl/{fn}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as res:
                data = res.read()
                with open(fp, 'wb') as f:
                    f.write(data)
                en_fp = os.path.join(en_dir, fn)
                with open(en_fp, 'wb') as f:
                    f.write(data)
                downloaded += 1
                print(f"Downloaded: {fn} ({len(data)} bytes)")
        except Exception as e:
            pass

print(f"Done! Downloaded {downloaded} new industry images.")
