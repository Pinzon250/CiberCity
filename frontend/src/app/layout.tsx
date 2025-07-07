// src/app/layout.tsx
import "./globals.css";
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import Navbar from "@/components/static/Navbar";
import Footer from "@/components/static/Footer";
import { AuthProvider } from "@/hooks/auth/AuthContext";

const geistSans = Geist({ variable: "--font-geist-sans", subsets: ["latin"] });
const geistMono = Geist_Mono({ variable: "--font-geist-mono", subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Cybercity",
  description: "E-commerce ",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="es">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
        <AuthProvider>
          <div className="flex bg-gray-100">
            <div className="flex flex-col min-h-screen flex-1">
              <Navbar />
              <main className="flex-grow flex-1 relative">
                {children}
              </main>
              <Footer />
            </div>
          </div>
        </AuthProvider>
      </body>
    </html>
  );
}
