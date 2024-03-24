import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const Articles = () => {
    const [loaded, setLoaded] = useState(false);
    const [loading, setLoading] = useState(false);
    const [data, setData] = useState({'percentage': 0, 'articles': []});
    const [scores, setScores] = useState([false, false, false, false, false, false, false, false, false, false]);
    const [times, setTimes] = useState([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
    const [start, setStart] = useState(0);

    const location = useLocation();
    const navigate = useNavigate();

    if (!loaded) {
        const parse_articles = location.state.articles;
        setLoaded(true);
        data['articles'] = parse_articles;
        setData(data);
        setStart(Date.now());
    }

    const toggleLoading = (button_id: number) => {
        setLoading(!loading);
        scores[data.articles.length - 1] = button_id === getCorrect(data.articles[data.articles.length - 1]);
        const elapsed = Date.now() - start;
        times[data.articles.length - 1] = Math.floor(elapsed / 1000);
        setScores(scores);
        setTimes(times);
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: sessionStorage.getItem('id'), button_id: button_id, articles: data.articles})
        };
        fetch('http://127.0.0.1:5000/api/button_clicked', requestOptions)
        .then(response => response.json())
        .then((res: any) => {
            data.percentage += 10;
            if (data.percentage === 100) {
                navigate('/results', {
                    state: {
                        articles: data.articles,
                        scores: scores,
                        times: times
                    }
                });
            }
            data.articles = res.articles;
            setData(data);
            setStart(Date.now());
            setLoading(false);
        });
    }

    const handleKeyPress = (event: { key: string; }) => {
        if (event.key === 'ArrowLeft'){
            toggleLoading(0);
        } else if (event.key === 'ArrowRight') {
            toggleLoading(1);
        }
    }

    const getText = (article: any) => {
        return article.text;
    }

    const getCorrect = (article: any) => {
        return article.correct;
    }

    return (
        <div tabIndex={0} className="container m-auto" onKeyDown={handleKeyPress}>
            <div className="p-10">
                <div className="w-full h-4 mb-4 bg-gray-200 rounded-full">
                    <div className="h-4 bg-blue-600 rounded-full" style={{width: String(data.percentage) + '%'}}></div>
                </div>
                <div className="text-center mb-5">
                    <p className="text-3xl font-bold mb-2">Do you agree with this?</p>
                    <p className="text-md font-light mb-2">You can also use the right and left arrow keys.</p>
                </div>
                <div className="flex justify-center mb-2">
                    <div className={"relative block max-w-3xl p-6 " + (loading ? "bg-slate-300" : "bg-white") + " border border-gray-200 rounded-lg shadow-lg"}>
                        <p className={"font-normal " + (loading ? "text-gray-400" : "text-gray-700")} dangerouslySetInnerHTML={{ __html: getText(data.articles[data.articles.length - 1]) }}></p>
                        <div role="status" className={"absolute -translate-x-1/2 -translate-y-1/2 top-2/4 left-1/2 " + (loading ? "" : "hidden")}>
                            <svg aria-hidden="true" className="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/><path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/></svg>
                            <span className="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
                <div className="flex justify-center mb-2">
                    <div className="block w-full max-w-3xl bg-white">
                        <div className="grid grid-cols-2 gap-2">
                            <button type="button" className={"w-full focus:outline-none text-white " + (loading ? "bg-gray-500" : "bg-red-600 hover:bg-red-800") + " focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2"} disabled={loading} onClick={() => toggleLoading(0)}>No</button>
                            <button type="button" className={"w-full focus:outline-none text-white " + (loading ? "bg-gray-500" : "bg-green-700 hover:bg-green-800") + " focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2"} disabled={loading} onClick={() => toggleLoading(1)}>Yes</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Articles;