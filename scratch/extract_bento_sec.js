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
const startIdx = homeHtml.indexOf('<section class="sec navy bento-sec"');
const endIdx = homeHtml.indexOf('</section>', startIdx) + 10;
const bentoSecHtml = homeHtml.substring(startIdx, endIdx);
console.log('bentoSecHtml length:', bentoSecHtml.length);
fs.writeFileSync('d:/My Work/Projects/penta-website/scratch/bento_sec.html', bentoSecHtml, 'utf8');
console.log('Saved bento_sec.html successfully!');
