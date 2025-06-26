import { Routes, Route} from "react-router-dom"
import './App.css';


// Layout
import Layout from "./Layout/Layout";

// Pages
import Home from "./pages/Home"



function App() {

  return (
    <Routes>
        <Route path="/" element={<Layout><Home /></Layout>}/>
    </Routes>
  )
}

export default App
