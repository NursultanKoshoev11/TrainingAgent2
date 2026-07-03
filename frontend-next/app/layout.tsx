export const metadata = {
  title: 'Crypto AI Advisor',
  description: 'Advisory-only crypto market intelligence dashboard',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
