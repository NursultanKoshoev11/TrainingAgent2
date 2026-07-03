const API_BASE = localStorage.getItem('apiBase') || 'http://localhost:8000';

async function getJson(path) {
  const response = await fetch(API_BASE + path);
  if (!response.ok) {
    throw new Error('API error ' + response.status);
  }
  return response.json();
}

async function getText(path) {
  const response = await fetch(API_BASE + path);
  if (!response.ok) {
    throw new Error('API error ' + response.status);
  }
  return response.text();
}

function renderJson(id, data) {
  document.getElementById(id).textContent = JSON.stringify(data, null, 2);
}

function renderText(id, text) {
  document.getElementById(id).textContent = text;
}

async function loadOverview() {
  renderJson('overview', await getJson('/api/overview'));
}

async function loadAdvice(symbol) {
  const safeSymbol = encodeURIComponent(symbol || 'BTC/USDT');
  renderJson('advice', await getJson('/api/advice?symbol=' + safeSymbol + '&exchange=binance&timeframe=1h'));
}

async function loadHealth() {
  renderJson('health', await getJson('/api/providers/health'));
}

async function loadWatchlist() {
  renderJson('watchlist', await getJson('/api/watchlist'));
}

async function loadReport() {
  renderText('report', await getText('/api/reports/text'));
}

async function loadSignals() {
  renderJson('signals', await getJson('/api/signals/recent?limit=20'));
}

async function bootDashboard() {
  const symbol = document.getElementById('symbol').value || 'BTC/USDT';
  try {
    await loadOverview();
    await loadAdvice(symbol);
    await loadHealth();
    await loadWatchlist();
    await loadReport();
    await loadSignals();
  } catch (error) {
    renderJson('overview', { error: String(error) });
  }
}

document.addEventListener('DOMContentLoaded', bootDashboard);
