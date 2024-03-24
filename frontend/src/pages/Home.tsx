// import github from '../assets/github-mark.png';
// import tracker from '../assets/tracker.png';
// import focus from '../assets/focus.png';

import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Home = () => {

    const [loaded, setLoaded] = useState(false);
    const [tags, setTags] = useState([]);
    const [query, setQuery] = useState('');
    const [searched, setSearched] = useState(false);
    const navigate = useNavigate();

    const handleInputChange = (event: any) => {
        setQuery(event.target.value);
    }

    if (!loaded) {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({})
        };
        fetch('http://127.0.0.1:5000/api/get_tags', requestOptions)
        .then(response => response.json())
        .then(data => {
            setLoaded(true);
            setTags(data.tags);
            sessionStorage.setItem('id', data.user_id);
        });
    }

    const submitForm = (formData: any) => {
        setSearched(true);
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: query, user_id: sessionStorage.getItem('id')})
        };
        fetch('http://127.0.0.1:5000/api/get_article', requestOptions)
        .then(response => response.json())
        .then((data: any) => {
            navigate('/articles', {
                state: {
                    articles: [data.article]
                }
            });
        });
    }

    return (
        <div className="container m-auto">
            <div className="p-10">
                <div className="text-center mb-5">
                    <p className="text-3xl font-bold mb-2">Welcome to <span className="text-green-700">Misinformation Mixup</span>.</p>
                    <p className="text-lg font-light mb-2">Mixup challenges your ability to discern misinformation! We 'inject' a curated set of articles and news with one of 6 different types of bias. Can YOU tell the difference?</p>
                </div>
                <div className="grid grid-rows-2 grid-cols-4">
                    <div className="col-start-2 col-end-4 flex items-center mb-2">   
                        <div className="relative w-full">
                            <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                <svg className="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                                </svg>
                            </div>
                            <input type="text" name="search" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5" placeholder="Search articles..." value={query} onChange={handleInputChange} required />
                        </div>
                        <button className="p-2.5 ms-2 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300" onClick={submitForm}>
                            <svg className="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                            </svg>
                            <span className="sr-only">Search</span>
                        </button>
                        {searched && 
                            <div role="status">
                                <svg aria-hidden="true" className="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600 ml-2" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                                    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                                </svg>
                                <span className="sr-only">Loading...</span>
                            </div>
                        }
                    </div>
                    <div className="col-start-2 col-end-4 flex mb-2 text-wrap">
                        <div className="block max-w-2xl bg-white text-wrap mb-1 flex flex-wrap">
                        {
                            tags.map(tag => {
                                return (
                                    <span className="bg-blue-100 text-blue-800 text-sm font-medium me-2 px-2.5 py-0.5 whitespace-nowrap rounded mb-2" onClick={() => setQuery(tag)}>{tag}</span>
                                );
                            })
                        }
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Home;