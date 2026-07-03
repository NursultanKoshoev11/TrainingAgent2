const API_BASE = localStorage.getItem('apiBase') || 'http://localhost:8000';

async function getJson(path) {
  const response = await fetch(API_BASE + path);
  if (!response.ok) {
    throw new Error('API error ' + response.status);
  }
  return response.json();
}

function renderJson(id, data) {
  document.getElementById(id).textContent = JSON.stringify(data, null, 2);
}

async function loadOverview() {
  const data = await getJson('/api/overview');
  renderJson('overview', data);
}

async function loadAdvice(symbol) {
  const safeSymbol = encodeURIComponent(symbol || 'BTC/USDT');
  const data = await getJson('/api/advice?symbol=' + safeSymbol + '&exchange=binance&timeframe=1h');
  renderJson('advice', data);
}

async function loadSignals() {
  const data = await getJson('/api/signals/recent?limit=20');
  renderJson('signals', data);
}

async function bootDashboard() {
  try {
    await loadOverview();
    await loadAdvice('BTC/USDT');
    await loadSignals();
  } catch (error) {
    renderJson('overview', { error: String(error) });
  }
}

document.addEventListener('DOMContentLoaded', bootDashboard);
