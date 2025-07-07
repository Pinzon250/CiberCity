"use client";


import { createContext, useContext, useState, useEffect } from "react";

interface AuthContextType {
  isLoggedIn: boolean;
  nombre: string;
  login: (token: string, userData: { nombres: string; correo: string }) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [nombre, setNombre] = useState("");

  useEffect(() => {
    const token = localStorage.getItem("token");
    const user = JSON.parse(localStorage.getItem("user") || "{}");
    if (token && user.nombres) {
      setIsLoggedIn(true);
      setNombre(user.nombres);
    }
  }, []);

  const login = (token: string, userData: { nombres: string; correo: string }) => {
    localStorage.setItem("token", token);
    localStorage.setItem("user", JSON.stringify(userData));
    setIsLoggedIn(true);
    setNombre(userData.nombres);
  };

  const logout = () => {
    localStorage.clear();
    setIsLoggedIn(false);
    setNombre("");
  };

  return (
    <AuthContext.Provider value={{ isLoggedIn, nombre, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext)!;
