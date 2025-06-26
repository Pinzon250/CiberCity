import { useLocation, Link } from "react-router-dom";
import { Codesandbox } from 'lucide-react'


const Navbar = () => {

    const navItems = [
        {name:"Inicio", path:"/"},
        {name:"Productos", path:"/productos"},
    ]


    return (
        <nav className="bg-gray-900 shadow-lg sticky top-0 z-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between items-center h-16">

                    {/* LOGO */}
                    <Link to="/" className="flex items-center space-x-2">
                        <Codesandbox className="size-8 text-gray-200"/>
                        <span className="text-xl font-bold text-gray-200">CiberCity</span>
                    </Link>

                    {/* Desktop  */}
                    <div className="hidden md:block">
                        <div className="ml-10 flex items-baseline space-x-4">
                        {navItems.map ((item) => (
                            <Link
                                key={item.path} 
                                to={item.path}
                                className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                                    location.pathname === item.path
                                        ? "bg-gray-700 text-gray-200"
                                        : "text-gray-200 hover:bg-gray-600"
                                }`}
                                >
                                    {item.name}
                            </Link>
                        ))}
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    )
}

export default Navbar;