import urllib.request, time

base = 'https://webdezign1.github.io/penta-services-agency/'

# Exactly test all languages and actual routes
routes = [
    '',
    'en/',
    'it/',
    'fr/',
    'ar/',
    'zh/',
    'en/pricing/',
    'en/services/',
    'en/services/website-design-development/',
    'en/services/corporate-website-design/',
    'en/services/ecommerce-website-development/',
    'en/services/wordpress-cms-development/',
    'en/services/website-redesign-migration/',
    'en/services/seo-services/',
    'en/services/generative-engine-optimisation-geo/',
    'en/services/international-local-seo/',
    'en/services/conversion-rate-optimisation/',
    'en/services/mobile-app-development/',
    'en/services/cross-platform-app-pwa-development/',
    'en/services/web-app-portal-saas-development/',
    'en/services/api-integration-services/',
    'en/services/website-maintenance-support/',
    'en/services/website-hosting-cloud-deployment/',
    'en/services/website-security-speed-optimisation/',
    'en/services/ux-ui-design-branding/',
    'en/website-templates/',
    'en/website-templates/corporate-website-templates/',
    'en/website-templates/creative-portfolio-website-templates/',
    'en/website-templates/retail-shop-website-templates/',
    'en/website-templates/ecommerce-website-templates/',
    'en/website-templates/blog-website-templates/',
    'en/website-templates/technology-website-templates/',
    'en/website-templates/entertainment-website-templates/',
    'en/website-templates/nonprofit-charity-website-templates/',
    'en/website-templates/education-school-website-templates/',
    'en/website-templates/real-estate-website-templates/',
    'en/website-templates/wedding-website-templates/',
    'en/website-templates/app-landing-page-templates/',
    'en/website-templates/small-business-website-templates/',
    'assets/app.css',
    'assets/app.js',
    'assets/tpl/marina-crest-hero.webp',
    'assets/tpl/marina-crest-i1.webp',
    'assets/tpl/marina-crest-i2.webp',
    'assets/tpl/marina-crest-i3.webp',
    'assets/tpl/artisan-bakery-thumb.jpg',
    'assets/tpl/artisan-bakery-home.jpg'
]

success = 0
failed = 0

for r in routes:
    u = base + r
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=10)
        if res.status == 200:
            success += 1
            label = r if r else "root (/)"
            print(f"[OK 200] {label}")
        else:
            print(f"[FAIL {res.status}] {r}")
            failed += 1
    except Exception as e:
        print(f"[ERROR] {r} -> {e}")
        failed += 1

print(f"\n==========================================")
print(f"Total checked: {len(routes)} | Passed: {success} | Failed: {failed}")
print(f"==========================================")
