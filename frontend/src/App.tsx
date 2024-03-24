import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from './pages/Home';
import Articles from './pages/Articles';
import Results from './pages/Results';
import PreviousArticles from "./pages/PreviousArticles";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="articles" element={<Articles />} />
                <Route path="results" element={<Results />} />
                <Route path="previous" element={<PreviousArticles />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
