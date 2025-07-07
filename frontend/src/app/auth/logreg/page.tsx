import Link from "next/link";

export default function LogRegPage() {
  return (
    <div className="max-w-7xl mx-auto">
            <div className="text-6xl text-center text-black">
                <h1>Bienvenido a <span className="font-semibold">CiberCity</span></h1>
            </div> 

            <div className="grid grid-cols-1 md:grid-cols-2 gap-5    md:px-50 px-10 py-10">
                <Link href="/auth/login">
                <div className="border border-gray-300 rounded-md hover:scale-105 transition shadow-md cursor-pointer">
                    <h1 className="text-center p-2 text-black">Inicia Sesion</h1>   
                </div>
                </Link>

                <Link href="/auth/register">
                <div className="border border-gray-300 rounded-md hover:scale-105 transition shadow-md cursor-pointer">
                    <h1 className="text-center p-2 text-black">Registrate</h1>
                </div>
                </Link>
            </div>
        </div>
  );
}
