import Navbar from '../components/static/Navbar'
import Footer from '../components/static/Footer'

type LayoutProps = {
    children : React.ReactNode
}

export default function Layout ({ children }: LayoutProps) {

    return (
        <div className='flex bg-gray-100'>
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