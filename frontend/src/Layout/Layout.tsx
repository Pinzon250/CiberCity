import Navbar from '../components/static/Navbar'
import Footer from '../components/static/Footer'

export default function Layout ({ children }) {
    return (
        <div className='flex bg-gray-800'>
            <div className="flex flex-col min-h-screen flex-1">
                <Navbar />
                <main className="mt-10 flex-grow flex-1 relative">
                    {children}
                </main>
                <Footer />
            </div>
        </div>
    )
}