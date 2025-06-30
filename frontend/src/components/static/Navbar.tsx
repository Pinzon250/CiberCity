import { useEffect, useRef, useState } from "react";
import { useLocation, Link } from "react-router-dom";
import { Codesandbox, ShoppingCart, User } from "lucide-react";

const Navbar = () => {
    const location = useLocation();
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [showMenu, setShowMenu] = useState(false);
    const [nombre, setNombre] = useState("");
    const menuRef = useRef<HTMLDivElement>(null);
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem("token");
        const user = JSON.parse(localStorage.getItem("user") || "{}");
        setIsLoggedIn(!!token);
        if (user.nombres) setNombre(user.nombres);
    }, []);

    // Cerrar menú si clic fuera
    useEffect(() => {
        const handleClickOutside = (e: MouseEvent) => {
            if (menuRef.current && !menuRef.current.contains(e.target as Node)) {
                setShowMenu(false);
            }
        };
        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    const handleLogout = () => {
        localStorage.clear();
        window.location.href = "/";
    };

    const navItems = [
        { name: "Inicio", path: "/" },
        { name: "Productos", path: "/productos" },
    ];

    return (
        <nav className="bg-gray-200 shadow-lg sticky top-0 z-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between items-center h-16">
                    {/* LOGO */}
                    <Link to="/" className="flex items-center space-x-2">
                        <Codesandbox className="size-8 text-gray-800" />
                        <span className="text-xl font-bold text-gray-800">CiberCity</span>
                    </Link>

                    {/* Desktop nav */}
                    <div className="hidden md:block">
                        <div className="ml-10 flex items-baseline space-x-4">
                            {navItems.map((item) => (
                                <Link
                                    key={item.path}
                                    to={item.path}
                                    className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${location.pathname === item.path
                                        ? "bg-black text-gray-200 font-semibold"
                                        : "text-gray-800 hover:bg-gray-100 font-semibold"
                                        }`}
                                >
                                    {item.name}
                                </Link>
                            ))}
                        </div>
                    </div>

                    {/* Cart + Usuario */}
                    <div className="flex items-center space-x-4">

                        {isLoggedIn ? (
                            <div className="relative flex items-center gap-2" ref={menuRef}>
                                <p className="hidden md:block text-sm font-semibold text-gray-700">
                                    {nombre}
                                </p>
                                <button
                                    onClick={() => setShowMenu(!showMenu)}
                                    className={`px-2 py-1 size-10 border border-gray-300 rounded-full transition-colors cursor-pointer ${showMenu
                                        ? "bg-black text-gray-200"
                                        : "text-gray-900 hover:bg-gray-100 shadow-md"
                                        }`}
                                >
                                    <User />
                                </button>

                                {showMenu && (
                                    <div className="absolute right-0 top-12 mt-2 w-48 bg-white border border-gray-200 rounded-md shadow-lg z-50">
                                        <p className="md:hidden block text-sm font-semibold px-4 py-2 text-gray-700">
                                            Hola, {nombre}
                                        </p>
                                        <Link
                                            to="/perfil"
                                            className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                                        >
                                            Configuración
                                        </Link>
                                        <Link
                                            to="/favoritos"
                                            className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                                        >
                                            Favoritos
                                        </Link>
                                        <button
                                            onClick={handleLogout}
                                            className="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-100"
                                        >
                                            Cerrar sesión
                                        </button>
                                    </div>
                                )}
                            </div>
                        ) : (
                            <Link to="/users">
                                <User className="px-2 py-1 size-10 border border-gray-300 rounded-md text-sm font-medium transition-colors cursor-pointer text-gray-900 hover:bg-gray-100 shadow-md" />
                            </Link>
                        )}
                        <Link to="/cart">
                            <ShoppingCart
                                className={`px-2 py-1 size-10 border border-gray-300 rounded-md text-sm font-medium transition-colors cursor-pointer ${location.pathname === "/cart"
                                    ? "bg-black text-gray-200"
                                    : "text-gray-900 hover:bg-gray-100 shadow-md"
                                    }`}
                            />
                        </Link>

                        <div className="md:hidden">
                            <button
                                onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                                aria-label="Toggle Menu"
                                className={`px-2 py-1 size-10 border border-gray-300 rounded-md text-sm font-medium transition-colors cursor-pointer ${location.pathname === "/cart"
                                    ? "bg-black text-gray-200"
                                    : "text-gray-900 hover:bg-gray-100 shadow-md"
                                    }`}
                            >
                                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">

                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                                </svg>
                            </button>
                        </div>
                    </div>

                    <div className={`md:hidden fixed inset-0 z-50 transition-all duration-600 ${mobileMenuOpen ? 'bg-black/60' : 'bg-transparent pointer-events-none'}`}>

                        <div
                            className={`absolute right-0 justify-between top-0 h-full w-64 bg-white shadow-lg p-6 space-y-4 transform transition-transform duration-500
    ${mobileMenuOpen ? 'translate-x-0 opacity-100' : 'translate-x-full opacity-0'}`}
                        >
                            <p className="text-lg font-semibold text-gray-800 mb-5">Menú</p>
                            <button onClick={() => setMobileMenuOpen(false)} className="absolute top-6 right-8 mb-5 text-black text-xl ">
                                ✕
                            </button>

                            {navItems.map((item) => (
                                <Link
                                    key={item.path}
                                    to={item.path}
                                    onClick={() => setMobileMenuOpen(false)}
                                    className={`block text-lg font-medium ${location.pathname === item.path
                                        ? 'text-gray-200 font-bold px-3 py-2 bg-black rounded-xl'
                                        : 'text-gray-700 hover:text-black px-3 py-2'
                                        }`}
                                >
                                    {item.name}
                                </Link>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </nav >
    );
};

export default Navbar;
