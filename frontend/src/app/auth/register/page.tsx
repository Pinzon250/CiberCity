"use client";

import { useState, FormEvent } from "react";
import { useRouter } from "next/navigation";
import axios from "axios";
import { FcGoogle } from "react-icons/fc";
import { FaApple } from "react-icons/fa";
import Link from "next/link";
import { registrarUsuario } from "@/libs/api/auth";

const RegisterPage = () => {
  const [nombres, setNombres] = useState("");
  const [apellidos, setApellidos] = useState("");
  const [correo, setCorreo] = useState("");
  const [contraseña, setContraseña] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const router = useRouter();
  const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL;

  const handleGoogleLogin = () => {
    window.location.href = `${backendUrl}/auth/google`;
  };

  const handleRegister = async (e: FormEvent<HTMLFormElement>) => {
  e.preventDefault();
  setError("");
  setSuccess("");

  try {
    await registrarUsuario(nombres, apellidos, correo, contraseña);
    setSuccess("Cuenta creada exitosamente. Redirigiendo...");
    setTimeout(() => router.push("/auth/login"), 2000);
  } catch (err: any) {
    setError(err.message || "Ocurrió un error al registrarse");
  }
};

  return (
    <div className="m-auto relative py-3 sm:max-w-xl lg:py-10 sm:mx-auto h-full">
      <div className="relative px-4 bg-white mx-8 md:mx-0 shadow rounded-3xl sm:p-10">
        <form onSubmit={handleRegister} className="px-8 pt-8 rounded-xl w-full space-y-4">
          <h2 className="text-2xl font-semibold text-center">Crear Cuenta</h2>

          {error && <p className="text-red-600 text-sm">{error}</p>}
          {success && <p className="text-green-600 text-sm">{success}</p>}

          <div className="mt-5 grid grid-cols-1 sm:grid-cols-2 gap-5">
            <div>
              <label className="font-semibold text-sm text-gray-600 pb-1 block">
                Nombres
              </label>
              <input
                type="text"
                placeholder="Nombres"
                className="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full focus:border-black border-gray-300"
                value={nombres}
                onChange={(e) => setNombres(e.target.value)}
                required
              />
            </div>

            <div>
              <label className="font-semibold text-sm text-gray-600 pb-1 block">
                Apellidos
              </label>
              <input
                type="text"
                placeholder="Apellidos"
                className="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full focus:border-black border-gray-300"
                value={apellidos}
                onChange={(e) => setApellidos(e.target.value)}
                required
              />
            </div>

            <div>
              <label className="font-semibold text-sm text-gray-600 pb-1 block">
                Correo electrónico
              </label>
              <input
                type="email"
                placeholder="Correo electrónico"
                className="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full focus:border-black border-gray-300"
                value={correo}
                onChange={(e) => setCorreo(e.target.value)}
                required
              />
            </div>

            <div>
              <label className="font-semibold text-sm text-gray-600 pb-1 block">
                Contraseña
              </label>
              <input
                type="password"
                placeholder="Contraseña"
                className="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full focus:border-black border-gray-300"
                value={contraseña}
                onChange={(e) => setContraseña(e.target.value)}
                required
              />
            </div>
          </div>

          <button
            type="submit"
            className="w-full bg-black cursor-pointer text-white py-2 rounded hover:bg-gray-800 transition"
          >
            Registrarse
          </button>

          <p className="text-center text-gray-500 text-sm pt-2">
            ¿Ya tienes una cuenta?{" "}
            <Link
              href="/auth/login"
              className="text-gray-600 hover:underline hover:text-black font-semibold"
            >
              Inicia sesión
            </Link>
          </p>
        </form>

        <aside className="text-sm text-gray-600 px-4 sm:px-8 max-w-xl mx-auto">
          <div className="flex items-center my-6">
            <div className="flex-grow border-t border-black/30"></div>
            <span className="mx-4 text-gray-500">OR</span>
            <div className="flex-grow border-t border-black/30"></div>
          </div>

          <button
            onClick={handleGoogleLogin}
            className="cursor-pointer flex items-center justify-center py-2 md:px-20 bg-gray-100 hover:bg-gray-200 text-gray-700 w-full transition text-base font-semibold shadow-md rounded-lg"
          >
            <FcGoogle size={24} className="mr-2" />
            Sign up with Google
          </button>

          <button className="mt-5 cursor-pointer flex items-center justify-center py-2 md:px-20 bg-gray-100 hover:bg-gray-200 text-gray-700 w-full transition text-base font-semibold shadow-md rounded-lg">
            <FaApple size={24} className="mr-2" />
            Sign up with Apple
          </button>

          <p className="text-center text-gray-500 pt-4 text-xs sm:text-sm px-2 sm:px-0">
            By signing in, you agree to our{" "}
            <Link href="/terms" className="text-gray-600 hover:underline hover:text-black font-semibold">
              Terms of Service
            </Link>{" "}
            and{" "}
            <Link href="/privacy" className="text-gray-600 hover:underline hover:text-black font-semibold">
              Privacy Policy
            </Link>.
          </p>
        </aside>
      </div>
    </div>
  );
};

export default RegisterPage;
