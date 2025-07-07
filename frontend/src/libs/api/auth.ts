import axios from "axios";


const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL;

// Olvidar contraseña
export const forgotPassword = async (correo: string) => {
  const res = await fetch(`${backendUrl}/user/forgot-password`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ correo }),
  });

  if (!res.ok) {
    const data = await res.json();
    throw new Error(data.detail || "Ocurrió un error. Inténtalo de nuevo.");
  }

  return res.json();
};

// Guardar token y datos
export const guardarSesion = (token: string, user: { nombres: string; correo: string }) => {
  localStorage.setItem("token", token);
  localStorage.setItem("user", JSON.stringify(user));
};

// Login
export const loginUsuario = async (correo: string, contraseña: string) => {
  const res = await axios.post(`${backendUrl}/user/login`, {
    correo,
    contraseña,
  });

  return res.data;
};

// Registrar Usuario
export const registrarUsuario = async (
  nombres: string,
  apellidos: string,
  correo: string,
  contraseña: string
) => {
  const res = await fetch(`${backendUrl}/user/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombres, apellidos, correo, contraseña }),
  });

  if (!res.ok) {
    const data = await res.json();
    throw new Error(data.detail || "Error desconocido");
  }

  return res.json();
};

// Resetear Contraseña
export const resetPassword = async (
  token: string,
  nueva_contraseña: string
) => {
  const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL;

  const res = await fetch(`${backendUrl}/user/reset-password`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ token, nueva_contraseña }),
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data.detail || "Error al restablecer la contraseña.");
  }

  return data;
};