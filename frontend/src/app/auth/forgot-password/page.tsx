"use client";

import { useState } from "react";
import { forgotPassword } from "@/libs/api/auth";

const ForgotPasswordPage = () => {
  const [correo, setCorreo] = useState("");
  const [mensaje, setMensaje] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();
  setMensaje("");
  setError("");

  try {
    await forgotPassword(correo);
    setMensaje("Se ha enviado un correo con instrucciones para restablecer tu contraseña.");
    setCorreo("");
  } catch (err: any) {
    setError(err.message || "Error de conexión con el servidor.");
  }
};

  return (
    <div className="m-auto flex items-center justify-center h-full bg-gray-100 px-4">
      <div className="max-w-md w-full bg-white p-6 rounded shadow-md">
        <h2 className="text-2xl font-bold mb-4 text-center text-gray-800">¿Olvidaste tu contraseña?</h2>
        <p className="text-sm text-gray-600 mb-6 text-center">
          Ingresa tu correo electrónico y te enviaremos un enlace para restablecer tu contraseña.
        </p>

        {mensaje && <p className="text-green-600 text-sm text-center mb-4">{mensaje}</p>}
        {error && <p className="text-red-600 text-sm text-center mb-4">{error}</p>}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="correo" className="block text-sm font-medium text-gray-700">
              Correo electrónico
            </label>
            <input
              id="correo"
              type="email"
              value={correo}
              onChange={(e) => setCorreo(e.target.value)}
              required
              className="w-full mt-1 p-2 border border-gray-300 rounded-md focus:ring focus:ring-blue-200"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-black text-white font-semibold py-2 px-4 rounded hover:bg-gray-800 transition"
          >
            Enviar enlace
          </button>
        </form>
      </div>
    </div>
  );
};

export default ForgotPasswordPage;
