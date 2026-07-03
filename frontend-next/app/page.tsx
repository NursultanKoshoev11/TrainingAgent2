const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000';

async function getJson(path: string) {
  const response = await fetch(API_BASE + path, { cache: 'no-store' });
  if (!response.ok) {
    return { error: 'API error ' + response.status };
  }
  return response.json();
}

export default async function DashboardPage() {
  const overview = await getJson('/api/overview');
  const health = await getJson('/api/providers/health');
  const runtime = await getJson('/api/runtime/status');

  return (
    <main style={{ padding: 32, fontFamily: 'Arial, sans-serif' }}>
      <h1>Crypto AI Advisor</h1>
      <p>Advisory-only dashboard. No real trading controls.</p>
      <section>
        <h2>Overview</h2>
        <pre>{JSON.stringify(overview, null, 2)}</pre>
      </section>
      <section>
        <h2>Provider Health</h2>
        <pre>{JSON.stringify(health, null, 2)}</pre>
      </section>
      <section>
        <h2>Runtime</h2>
        <pre>{JSON.stringify(runtime, null, 2)}</pre>
      </section>
    </main>
  );
}
