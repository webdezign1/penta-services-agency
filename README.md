# Penta Services - Digital Agency Website Replica

A complete, feature-for-feature replica of [Penta Services](https://pentaservices.co.uk/en/), an international digital engineering and growth agency based in London, Italy, and Pakistan.

---

## 🚀 Quick Start

You can run this project using **Python**, **Node.js**, or **any static web server**:

### Option 1: Python Server (Recommended)
```bash
cd "d:\My Work\Projects\penta-website"
python server.py
```
Open **[http://localhost:8080/en/](http://localhost:8080/en/)** in your browser.

### Option 2: Node.js Server
```bash
cd "d:\My Work\Projects\penta-website"
node server.js
```
Open **[http://localhost:8080/en/](http://localhost:8080/en/)** in your browser.

### Option 3: Direct Static File
You can also open `index.html` directly in any modern browser or via VS Code Live Server. The application includes offline fallbacks for forms and state persistence.

---

## 🌟 Complete Feature List

### 1. Branding & Visual Design
- **Exact Vector Branding:** Dynamic five-facet Penta SVG logo with CSS custom property theming (`--f1` through `--f5`).
- **Typography:** Google Fonts pairing of *Instrument Serif*, *Bricolage Grotesque*, *Instrument Sans*, and *IBM Plex Sans Arabic*.
- **Dark / Light Mode:** Instant toggle button with system preference detection and `localStorage` persistence.
- **Micro-Interactions & Animations:** Dynamic ticker, smooth scroll indicators, responsive card hover states, and animated SVG mockups.

### 2. Multi-Language & RTL Engine
- **5 Full Languages:**
  - English (`/en/`)
  - Italian (`/it/`)
  - French (`/fr/`)
  - Arabic (`/ar/`) - *Native Right-to-Left (RTL) layout with IBM Plex Sans Arabic*
  - Chinese (`/zh/`)
- Dynamic language switcher in header and mobile drawer.

### 3. Multi-Currency Engine
- **8 Supported Currencies:**
  - GBP (£)
  - USD ($)
  - EUR (€)
  - AED (AED)
  - SAR (SAR)
  - AUD (A$)
  - CAD (C$)
  - CNY (¥)
- Real-time conversion across all packages, add-ons, monthly care plans, and cost estimator.

### 4. Interactive Mega Menus
- **Services Mega Menu:** Direct access to all 17 core services categorized by *Web & Commerce*, *Search & Growth*, *Apps & Technology*, and *Ongoing Services*.
- **Ready Sites Mega Menu:** Visual catalog preview of 13 industry categories.
- **Resources Mega Menu:** Quick tools including Cost Estimator, Free Audit, SEO/GEO assessment, and platform comparisons.

### 5. Ready Sites Gallery (67 Templates)
- Filterable gallery covering **13 distinct industries**: Corporate & Professional, Tech & SaaS, Real Estate, Education, E-commerce, Retail Shops, Small Businesses, Creative & Portfolio, Blogs, Entertainment, Weddings, Nonprofits, and Mobile Apps.
- **Interactive Live Preview Modal:** Full-screen responsive viewport simulation (Desktop, Tablet, Mobile) for every template design.

### 6. Interactive Website Cost Estimator
- Step-by-step budget estimation tool.
- Dynamic sliders for page count (1 to 50+) and multi-language support (1 to 5 languages).
- Checkboxes for custom features (CMS, E-Commerce, User Portals, SEO, AI Search, Custom Integrations).
- Instant real-time calculation of setup cost and monthly hosting/care fee ranges.

### 7. 60-Second AI Search Readiness Checker (GEO Assessment)
- Interactive assessment testing visibility across generative search engines (ChatGPT, Perplexity, Gemini, Google SGE).
- Dynamic scoring algorithm and recommendation breakdown.

### 8. Interactive Homepage Builder
- Live preview tool allowing visitors to select an industry preset and see a website interface generated in real-time.

### 9. Packages & Pricing Matrix
- Transparent package breakdown:
  - Business Website
  - Corporate Website
  - E-commerce Store
  - Digital Growth (SEO + GEO)
  - Enterprise & Custom Development
- Monthly vs Annual billing toggle with bundle discount calculations.
- Direct "Add to Cart" integration.

### 10. E-Commerce Cart & Quote Proposal Generator
- Slide-over cart drawer displaying selected packages, care plans, and domain registration.
- Domain search and cart additions.
- Printable proposal & invoice generator (`#invDlg`) with reference numbers and downloadable summary.

### 11. 24/7 AI Chat Assistant ("Penta Assistant")
- Embedded floating chat widget with instant FAQ triggers:
  - "Is hosting really included?"
  - "How long does a website take?"
  - "Do you guarantee first-page rankings?"
  - "Pricing"
  - "Talk to a project lead"

### 12. Complete Service Pages & Lead Capture
- Rich landing pages for all 17 services.
- Forms for Contact, Free Website Audit, SEO/GEO Assessment, and Custom App Quotes.
- Automatic backend logging to `leads.json` via `/api/send.php` with offline `localStorage` fallback.

---

## 📁 Directory Structure

```
penta-website/
├── index.html           # Main application HTML shell
├── server.py            # Python dev server with SPA routing & API handlers
├── server.js            # Node.js dev server alternative
├── leads.json           # Received inquiries and lead submissions log
├── README.md            # Documentation and feature guide
├── assets/
│   ├── app.css          # Master stylesheet (141 KB)
│   ├── app.js           # Full client-side application logic & routing (1.2 MB)
│   ├── img/             # Showcase slide graphics (WebP)
│   └── logo/            # Branding icons (512px and 1024px PNG)
├── favicon.ico          # Favicon
└── apple-touch-icon.png # Apple Touch Icon
```
