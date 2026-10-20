const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8080;
const DIR = __dirname;
const LEADS_FILE = path.join(DIR, 'leads.json');

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webp': 'image/webp',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

const server = http.createServer((req, res) => {
  const parsed = new URL(req.url, `http://${req.headers.host}`);
  const pathname = parsed.pathname;

  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }

  // API Endpoints
  if (req.method === 'GET' && pathname === '/api/geo.php') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ country: 'GB', currency: 'GBP', pkr: null }));
    return;
  }

  if (req.method === 'GET' && pathname === '/api/oauth/providers') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ok: true, providers: ['google', 'microsoft'] }));
    return;
  }

  if (req.method === 'POST' && (pathname === '/api/send.php' || pathname === '/api/send')) {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      let data = {};
      try { data = JSON.parse(body); } catch (e) { data = { raw: body }; }
      const record = {
        id: `PENTA-${Date.now()}`,
        received_at: new Date().toISOString(),
        payload: data
      };

      let leads = [];
      if (fs.existsSync(LEADS_FILE)) {
        try { leads = JSON.parse(fs.readFileSync(LEADS_FILE, 'utf8')); } catch (e) {}
      }
      leads.push(record);
      fs.writeFileSync(LEADS_FILE, JSON.stringify(leads, null, 2), 'utf8');

      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ ok: true, id: record.id, message: 'Inquiry successfully saved.' }));
    });
    return;
  }

  // Static File Serving
  let filePath = path.join(DIR, pathname.replace(/^\/+/, ''));
  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    const mime = MIME_TYPES[ext] || 'application/octet-stream';
    res.writeHead(200, { 'Content-Type': mime });
    fs.createReadStream(filePath).pipe(res);
    return;
  }

  // SPA fallback for language routes
  if (pathname.startsWith('/en/') || pathname.startsWith('/it/') || pathname.startsWith('/fr/') || pathname.startsWith('/ar/') || pathname.startsWith('/zh/') || pathname === '/' || pathname === '/index.html') {
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    fs.createReadStream(path.join(DIR, 'index.html')).pipe(res);
    return;
  }

  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.end('404 Not Found');
});

server.listen(PORT, () => {
  console.log(`Penta Services server running on http://localhost:${PORT}/en/`);
});
