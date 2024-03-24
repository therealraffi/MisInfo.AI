import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from './pages/Home';
import Articles from './pages/Articles';
import Results from './pages/Results';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="articles" element={<Articles />} />
                <Route path="results" element={<Results />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
