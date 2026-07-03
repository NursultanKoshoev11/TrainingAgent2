export const metadata = {
  title: 'Crypto AI Advisor',
  description: 'Advisory-only dashboard для анализа крипторынка',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru">
      <body>{children}</body>
    </html>
  );
}
