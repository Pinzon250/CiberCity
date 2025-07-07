"use client";

import { useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { guardarSesion } from "@/libs/api/auth";

const OAuthCallbackPage = () => {
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();
  const searchParams = useSearchParams();

  useEffect(() => {
    const token = searchParams.get("token");
    const nombre = searchParams.get("nombre");
    const correo = searchParams.get("correo");

    if (token && nombre && correo) {
      guardarSesion(token, { nombres: nombre, correo });
      router.push("/");
    } else {
      setError("No se recibió token desde el proveedor.");
    }
  }, [router, searchParams]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      {error ? (
        <div className="text-red-600">{error}</div>
      ) : (
        <div className="text-gray-700 text-lg">Iniciando sesión con Google...</div>
      )}
    </div>
  );
};

export default OAuthCallbackPage;
