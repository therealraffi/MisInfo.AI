import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from './pages/Home';
import Articles from './pages/Articles';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="articles" element={<Articles />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
