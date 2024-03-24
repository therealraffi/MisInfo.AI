import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';

const PreviousArticles = () => {

    const [percentage, setPercentage] = React.useState(10);
    const [index, setIndex] = useState(0);

    const updateIndex = (i: number) => {
        if (i === -1) {
            i = articles.length - 1;
        }
        setIndex(i);
        setPercentage((i * 100 + 100) / (articles.length));
    }
    
    const location = useLocation();

    const articles = location.state.articles;

    const handleKeyPress = (event: { key: string; }) => {
        if(event.key === 'ArrowLeft'){
            updateIndex((index - 1) % articles.length);
        } else if (event.key === 'ArrowRight') {
            updateIndex((index + 1) % articles.length);
        }
    }

    return (
        <div tabIndex={0} className="container m-auto" onKeyDown={handleKeyPress}>
            <div className="p-10">
                <div className="w-full h-4 mb-4 bg-gray-200 rounded-full">
                    <div className="h-4 bg-blue-600 rounded-full" style={{width: String(percentage) + '%'}}></div>
                </div>
                <div className="text-center mb-5">
                    <p className="text-3xl font-bold mb-2">Scroll through your previous articles</p>
                    <p className="text-md font-light mb-2">You can also use the right and left arrow keys or the provided arrows.</p>
                </div>
                <div className="flex justify-center">
                    <div className="relative block w-1/2 px-12 py-6 bg-white border border-gray-200 rounded-lg shadow-lg">
                        <p className="font-normal text-gray-700 mb-5" dangerouslySetInnerHTML={{ __html: articles[index].text }} />
                        <p className="font-normal text-gray-700">Correct answer: <b>{articles[index].correct ? 'Yes' : 'No'}</b></p>
                        <button className="fixed inset-y-1/3 left-96 bg-white h-12 w-12 p-2 rounded-full border shadow-md hover:bg-gray-100" onClick={() => updateIndex((index - 1) % articles.length)}>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5 3 12m0 0 7.5-7.5M3 12h18" />
                            </svg>
                        </button>
                        <button className="fixed inset-y-1/3 right-96 bg-white h-12 w-12 p-2 rounded-full border shadow-md hover:bg-gray-100" onClick={() => updateIndex((index + 1) % articles.length)}>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default PreviousArticles;