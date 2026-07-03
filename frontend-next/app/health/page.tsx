const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000';

async function getJson(path: string) {
  const response = await fetch(API_BASE + path, { cache: 'no-store' });
  if (!response.ok) return { error: 'API error ' + response.status };
  return response.json();
}

export default async function HealthPage() {
  const health = await getJson('/api/providers/health');
  const runtime = await getJson('/api/runtime/status');
  const context = await getJson('/api/context/status');
  return (
    <main style={{ padding: 32, fontFamily: 'Arial, sans-serif' }}>
      <h1>Статус провайдеров</h1>
      <h2>Providers</h2>
      <pre>{JSON.stringify(health, null, 2)}</pre>
      <h2>Runtime</h2>
      <pre>{JSON.stringify(runtime, null, 2)}</pre>
      <h2>Context</h2>
      <pre>{JSON.stringify(context, null, 2)}</pre>
    </main>
  );
}
