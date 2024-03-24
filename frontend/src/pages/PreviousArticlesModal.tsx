import React, { useState } from 'react';

const PreviousArticles = ({showModal, setShowModal, articles}: {showModal: any, setShowModal: any, articles: any}) => {

    const [index, setIndex] = useState(0);

    const updateIndex = (i: number) => {
        if (i === -1) {
            i = articles.length - 1;
        }
        setIndex(i);
    }

    return (
        <>
            {showModal ? (
                <>
                    <div className="fixed justify-center items-center flex inset-0 z-50 overflow-x-hidden overflow-y-auto">
                        <div className="border-0 rounded-lg shadow-lg relative flex flex-col bg-white outline-none focus:outline-none">
                            <div className="flex items-start justify-between p-4 border-b border-solid border-slate-200 rounded-t">
                                <p className="text-2xl font-semibold">Here are the articles you read.</p>
                                <button type="button" className="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-4 py-2" onClick={() => setShowModal(false)}>Close</button>
                            </div>
                            <div className="relative p-2 flex-auto my-2 mx-1 text-slate-500 text-md">
                                <div className="block max-w-3xl px-12 py-6 bg-white border border-gray-200 rounded-lg shadow-lg">
                                    <p className="font-normal text-gray-700 mb-5" dangerouslySetInnerHTML={{ __html: articles[index].text }} />
                                    <p className="font-normal text-gray-700">Correct answer: <b>{articles[index].correct}</b></p>
                                </div>
                                <button className="absolute inset-y-1/3 left-0 bg-white h-12 w-12 p-2 rounded-full border shadow-md hover:bg-gray-100" onClick={() => updateIndex((index - 1) % articles.length)}>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5 3 12m0 0 7.5-7.5M3 12h18" />
                                    </svg>
                                </button>
                                <button className="absolute inset-y-1/3 right-0 bg-white h-12 w-12 p-2 rounded-full border shadow-md hover:bg-gray-100" onClick={() => updateIndex((index + 1) % articles.length)}>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>
            <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
            </>
        ) : null}
        </>
    );
};
  
export default PreviousArticles;