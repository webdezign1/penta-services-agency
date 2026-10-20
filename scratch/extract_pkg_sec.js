const fs = require('fs');
let code = fs.readFileSync('d:/My Work/Projects/penta-website/assets/app.js', 'utf8');

const mockEl = { innerHTML: '', style: {}, remove: ()=>{}, getAttribute: ()=> '', classList: { add: ()=>{}, remove: ()=>{} }, setAttribute: () => {}, addEventListener: () => {}, querySelector: () => mockEl, querySelectorAll: () => [] };
global.window = { scrollY: 0, scrollTo: () => {}, location: { hostname: 'webdezign1.github.io', hash: '', pathname: '/penta-services-agency/en/' }, addEventListener: () => {} };
global.document = { documentElement: { dataset: {} }, getElementById: () => mockEl, querySelector: () => mockEl, querySelectorAll: () => [], addEventListener: () => {} };
global.location = global.window.location;
global.localStorage = { getItem: () => null, setItem: () => {} };
global.matchMedia = () => ({ matches: false });
global.addEventListener = () => {};

eval(code);

const homeHtml = pageHome();
const startIdx = homeHtml.indexOf('<section class="sec pkg-section"');
const endIdx = homeHtml.indexOf('</section>', startIdx) + 10;
const pkgSecHtml = homeHtml.substring(startIdx, endIdx);
console.log('pkgSecHtml length:', pkgSecHtml.length);
fs.writeFileSync('d:/My Work/Projects/penta-website/scratch/pkg_sec.html', pkgSecHtml, 'utf8');
console.log('Saved pkg_sec.html successfully!');
