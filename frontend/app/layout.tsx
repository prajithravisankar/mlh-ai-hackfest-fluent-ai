import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import Link from "next/link";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "FluentAI — AI English Speaking Coach",
  description: "Stop typing English. Start speaking it.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased dark`}
    >
      <body className="min-h-full flex flex-col bg-background text-foreground">
        <nav className="border-b border-zinc-800 bg-surface">
          <div className="mx-auto flex h-14 max-w-7xl items-center justify-between px-4">
            <Link
              href="/"
              className="text-lg font-bold tracking-tight text-accent-light"
            >
              FluentAI
            </Link>
            <div className="flex items-center gap-6">
              <Link
                href="/roadmap"
                className="text-sm text-zinc-400 hover:text-foreground transition-colors"
              >
                Roadmap
              </Link>
              <Link
                href="/profile"
                className="text-sm text-zinc-400 hover:text-foreground transition-colors"
              >
                Profile
              </Link>
              <div className="flex items-center gap-2 rounded-full bg-surface-light px-3 py-1 text-xs text-zinc-400">
                <span>⚡</span>
                <span>0 XP</span>
              </div>
            </div>
          </div>
        </nav>
        {children}
      </body>
    </html>
  );
}
