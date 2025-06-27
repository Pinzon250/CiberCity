import { Routes, Route} from "react-router-dom"
import './App.css';


// Layout
import Layout from "./Layout/Layout";

// Auth
import LogReg from "./pages/auth/LogReg";
import OAuthCallback from "./pages/auth/OAuthCallback";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import ForgotPass from "./pages/auth/ForgotPass";

// Pages
import Home from "./pages/Home"



function App() {

  return (
    <Routes>

        {/* Pages */}
        <Route path="/" element={<Layout><Home /></Layout>}/>

        {/* Auth */}
        <Route path="/users" element={<Layout><LogReg /></Layout>}/>
        <Route path="/login" element={<Layout><Login /></Layout>}/>
        <Route path="/register" element={<Layout><Register /></Layout>}/>
        <Route path="/forgot-pass" element={<Layout><ForgotPass /></Layout>}/>
        <Route path="/oauth/callback" element={<OAuthCallback />} />

    </Routes>
  )
}

export default App
