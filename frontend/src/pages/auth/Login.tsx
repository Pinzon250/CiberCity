import { useState } from "react";
import type { FormEvent } from "react";
import axios from "axios";
import { useNavigate, Link } from "react-router-dom";
import { FcGoogle } from "react-icons/fc";
import { FaApple } from "react-icons/fa";
import { useAuth } from "../../hooks/auth/AuthContext";

const Login = () => {
  const [correo, setCorreo] = useState<string>("");
  const [contraseña, setContraseña] = useState<string>("");
  const [error, setError] = useState<string>("");
  const navigate = useNavigate();
  const backendUrl = import.meta.env.VITE_BACKEND_URL;
  const { login } = useAuth(); // ✅ Usamos login del contexto

  const handleGoogleLogin = () => {
    window.location.href = `${backendUrl}/auth/google`;
  };

  const handleLogin = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const res = await axios.post(`${backendUrl}/user/login`, {
        correo,
        contraseña,
      });

      const token = res.data.access_token;
      const user = res.data.user;

      login(token, user); // ✅ Actualiza el contexto
      navigate("/");      // ✅ Redirige a home
    } catch (err: unknown) {
      if (axios.isAxiosError(err) && err.response) {
        setError(err.response.data.detail || "Error desconocido");
      } else {
        setError("Correo o contraseña incorrectos");
      }
    }
  };

  return (
    <div className="relative pt-3 lg:py-10 sm:max-w-xl sm:mx-auto">
      <div className="relative px-4 p-10 bg-white mx-8 md:mx-0 shadow rounded-3xl sm:p-10">
        <form onSubmit={handleLogin} className="px-8 py-3 rounded-xl w-full  ">

          {error && (
          <div className="peer-invalid:block">
            <div className="border w-full p-4 bg-red-100 border-red-200 m-auto justify-center my-3 flex items-center gap-1">
              <div className="w-4 fill-rose-500">
                <svg
                  viewBox="0 0 24 24"
                  data-name="Layer 1"
                  id="Layer_1"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path d="M24,12A12,12,0,1,1,12,0,12.013,12.013,0,0,1,24,12ZM13,5H11V15h2Zm0,12H11v2h2Z"></path>
                </svg>
              </div>
              <p className="Capitalize font-medium text-center text-rose-500">{error}</p>
            </div>
          </div>
        )}

          <h2 className="text-2xl font-semibold mb-6 text-center">Iniciar Sesión</h2>

          <label
            className="font-semibold text-sm text-gray-600 pb-1 block"
            htmlFor="login"
          >E-mail
          </label>

          <input
            type="email"
            placeholder="Correo electrónico"
            className="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full border-gray-300"
            value={correo}
            onChange={(e) => setCorreo(e.target.value)}
            required
          />

          <label
            className="font-semibold text-sm text-gray-600 pb-1 block"
            htmlFor="password"
          >Password
          </label>
          <input
            type="password"
            placeholder="Contraseña"
            className="border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full border-gray-300"
            value={contraseña}
            onChange={(e) => setContraseña(e.target.value)}
            required
          />
          <button
            type="submit"
            className="w-full bg-black cursor-pointer text-white py-2 rounded hover:bg-gray-800 transition"
          >
            Ingresar
          </button>
        </form>
        <aside className="text-sm text-gray-600 px-4 sm:px-8 max-w-xl mx-auto">
          <div className="flex flex-col sm:flex-row justify-between items-center gap-2 sm:gap-0 mb-4 text-center sm:text-left">
            <Link to="/forgot-pass" className="hover:text-black font-semibold">
              Forgot Password?
            </Link>
            <p>
              Don't have an account?
              <Link to="/register" className="font-semibold ml-1 hover:text-black">
                Register
              </Link>
            </p>
          </div>

          <div className="flex items-center my-6">
            <div className="flex-grow border-t border-black/30"></div>
            <span className="mx-4 text-gray-500">OR</span>
            <div className="flex-grow border-t border-black/30"></div>
          </div>

          <button 
            onClick={handleGoogleLogin}
            className="cursor-pointer flex items-center justify-center py-2 md:px-20 bg-gray-100 hover:bg-gray-200 focus:ring-blue-500 focus:ring-offset-blue-200 text-gray-700 w-full transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg">
            <FcGoogle size={24} className="mr-2" />
            Sign up with Google
          </button>

          <button className="mt-5 cursor-pointer flex items-center justify-center py-2 md:px-20 bg-gray-100 hover:bg-gray-200 focus:ring-blue-500 focus:ring-offset-blue-200 text-gray-700 w-full transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2 rounded-lg">
            <FaApple size={24} className="mr-2" />
            Sign up with Apple
          </button>

          <p className="text-center text-gray-500 pt-4 text-xs sm:text-sm px-2 sm:px-0">
            By signing in, you agree to our{" "}
            <a href="/terms" className="text-gray-600 hover:text-black font-semibold">
              Terms of Service
            </a>{" "}
            and{" "}
            <a href="/privacy" className="text-gray-600 hover:text-black font-semibold">
              Privacy Policy
            </a>.
          </p>
        </aside>
      </div>
    </div>
  );
};

export default Login;
