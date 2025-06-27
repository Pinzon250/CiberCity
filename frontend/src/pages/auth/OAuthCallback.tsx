import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const OAuthCallback = () => {
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const queryParams = new URLSearchParams(window.location.search);
    const token = queryParams.get("token");
    const nombre = queryParams.get("nombre");
    const correo = queryParams.get("correo");

    if (token && nombre && correo) {
      localStorage.setItem("token", token);
      localStorage.setItem(
        "user",
        JSON.stringify({ nombres: nombre, correo })
      );
      navigate("/");
    } else {
      setError("No se recibió token desde el proveedor.");
    }
  }, [navigate]);

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

export default OAuthCallback;
