// async function fetchPosts() {
//   const r = await fetch('/api/posts');
//   const posts = await r.json();
//   const container = document.getElementById('posts');
//   container.innerHTML = '';

//   posts.forEach(p => {
//     const el = document.createElement('article');
//     el.innerHTML = `
//       <h3>${p.title}</h3>
//       <p>${p.summary || ''}</p>
//       <div>${(p.body || '').split('\n').slice(0, 10).join('<br>')}</div>
//     `;
//     container.appendChild(el);
//   });
// }

// function parseInput(text) {
//   return text.split('\n').map(line => line.trim()).filter(Boolean).map(line => {
//     if (line.includes('||')) {
//       const parts = line.split('||').map(x => x.trim());
//       return { title: parts[0], details: parts[1] };
//     }
//     return { title: line };
//   });
// }

// document.getElementById('generate').addEventListener('click', async () => {
//   const text = document.getElementById('titles').value;
//   const items = parseInput(text);
//   document.getElementById('status').innerText = 'Generating...';
//   const r = await fetch('/api/generate', {
//     method: 'POST',
//     headers: { 'Content-Type': 'application/json' },
//     body: JSON.stringify({ items })
//   });
//   const data = await r.json();
//   document.getElementById('status').innerText = 'Done.';
//   fetchPosts();
// });

// fetchPosts();
let tickerPosts = []; // Posts for news ticker

async function fetchPosts() {
  const r = await fetch('/api/posts');
  const posts = await r.json();
  const container = document.getElementById('posts');
  container.innerHTML = '';

  tickerPosts = []; // reset ticker posts

  posts.forEach(p => {
    const el = document.createElement('article');
    el.innerHTML = `
      <h3>${p.title}</h3>
      <p>${p.summary || ''}</p>
      <div>${(p.body || '').split('\n').slice(0, 10).join('<br>')}</div>
    `;
    container.appendChild(el);

    // Prepare ticker
    tickerPosts.push(`${p.title}: ${p.summary || (p.body || '').slice(0, 100)}...`);
  });

  updateTicker();
}

function parseInput(text) {
  return text.split('\n').map(line => line.trim()).filter(Boolean).map(line => {
    if (line.includes('||')) {
      const parts = line.split('||').map(x => x.trim());
      return { title: parts[0], details: parts[1] };
    }
    return { title: line };
  });
}

document.getElementById('generate').addEventListener('click', async () => {
  const text = document.getElementById('titles').value;
  const items = parseInput(text);
  document.getElementById('status').innerText = 'Generating...';
  const r = await fetch('/api/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ items })
  });
  const data = await r.json();
  document.getElementById('status').innerText = 'Done.';
  fetchPosts();
});

// -----------------------
// News ticker logic
// -----------------------
function updateTicker() {
  const ticker = document.getElementById('ticker');
  if (!ticker) return;

  ticker.innerHTML = ''; // clear previous

  tickerPosts.forEach(text => {
    const span = document.createElement('span');
    span.innerText = text;
    ticker.appendChild(span);
  });
}

// Refresh ticker every 5 minutes
setInterval(fetchPosts, 5 * 60 * 1000); // 5 minutes
fetchPosts(); // initial load
