// import github from '../assets/github-mark.png';
// import tracker from '../assets/tracker.png';
// import focus from '../assets/focus.png';

import BarChart from "./BarChart";
import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

const Results = () => {

    const [loaded, setLoaded] = useState(false);
    const [articles, setArticles] = useState([]);

    const location = useLocation();
    const scores = location.state.scores;
    const times = location.state.times;


    if (!loaded) {
        setLoaded(true);
        setArticles(location.state.articles);
    }

    const getCategoryFromArticle = (article: any): string => {
        return article.category;
    }

    const getBiasFromArticle = (article: any): string => {
        return article.bias;
    }

    const getQuestionData = () => {
        const questionStats: {category: string, score: number, total: number}[] = [];
        articles.forEach((article, j) => {
            const category = getCategoryFromArticle(article);
            let exists = false;
            questionStats.forEach((value, i) => {
                if (questionStats[i].category === category) {
                    questionStats[i].score += Number(scores[j]);
                    questionStats[i].total += 1;
                    exists = true;
                }
            });
            if (!exists) {
                questionStats.push({category: category, score: Number(scores[j]), total: 1});
            }
        });
        return questionStats
    }

    const question_data = getQuestionData();

    const getBiasData = () => {
        const biasStats: {category: string, score: number, total: number}[] = [];
        articles.forEach((article, j) => {
            const bias = getBiasFromArticle(article);
            let exists = false;
            biasStats.forEach((value, i) => {
                if (biasStats[i].category === bias) {
                    biasStats[i].score += Number(scores[j]);
                    biasStats[i].total += 1;
                    exists = true;
                }
            });
            if (!exists) {
                biasStats.push({category: bias, score: Number(scores[j]), total: 1});
            }
        });
        return biasStats
    }

    const bias_data = getBiasData();
    
    question_data.sort((a: any, b: any) => (b.score / b.total) - (a.score / a.total));
    
    bias_data.sort((a: any, b: any) => (b.score / b.total) - (a.score / a.total));
    
    const [showModal, setShowModal] = useState(false);
    const navigate = useNavigate();

    const openPreviousArticles = () => {
        navigate('/previous', {
            state: {
                articles: articles
            }
        })
    }

    const mean = () => {
        let sum = 0;
        times.forEach((value: number) => {
            sum += value;
        });
        return sum / times.length;
    }

    return (
        <div className="container m-auto">
            <div className="px-36 py-10">
                <div className="text-center mb-5">
                    <p className="text-3xl mb-2">Here are your results.</p>
                </div>
                <div className="grid grid-rows-2 grid-cols-2 gap-4 mb-2">
                    <p className="text-5xl text-center font-bold">{String(scores.filter(Boolean).length * 100 / scores.length) + "%"}</p>
                    <p className="text-5xl text-center font-bold">{String(mean()) + " sec"}</p>
                    <p className="text-sm text-center font-bold">Questions answered correctly</p>
                    <p className="text-sm text-center font-bold">Time spent per question</p>
                </div>
                <div className="grid grid-rows-2 grid-cols-2 gap-4">
                    <div>
                        <p className="text-xl text-center font-bold mb-2">Article Count</p>
                        <BarChart data={question_data} questions={[]} axis={'Type of question'} />
                    </div>
                    <div>
                        <p className="text-xl text-center font-bold mb-2">Bias Count</p>
                        <BarChart data={bias_data} questions={[]} axis={'Type of Bias'} />
                    </div>
                    <div className="rounded-lg">
                        <table className="w-full text-sm text-left text-gray-500 border shadow-lg mb-4">
                            <thead className="text-xs text-gray-700 uppercase bg-gray-50">
                                <tr>
                                    <th scope="col" className="px-6 py-3">
                                        Article Category
                                    </th>
                                    <th scope="col" className="px-6 py-3">
                                        # of correct answers
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                {question_data.map((entry: any) => {
                                    return (
                                        <tr className="bg-white border-b">
                                            <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                                                {entry.category}
                                            </th>
                                            <td className="px-6 py-4">
                                                {entry.score + ' / ' + entry.total}
                                            </td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                        <div className="grid grid-cols-3">
                            <button type="button" className="text-center text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2" onClick={() => navigate('/')}>Back to Home</button>
                        </div>
                    </div>
                    <div className="rounded-lg">
                        <table className="w-full text-sm text-left rtl:text-right text-gray-500 border shadow-lg mb-4">
                            <thead className="text-xs text-gray-700 uppercase bg-gray-50">
                                <tr>
                                    <th scope="col" className="px-6 py-3">
                                        Bias Category
                                    </th>
                                    <th scope="col" className="px-6 py-3">
                                        # of correct answers
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                {bias_data.map((entry: any) => {
                                    return (
                                        <tr className="bg-white border-b">
                                            <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                                                {entry.category}
                                            </th>
                                            <td className="px-6 py-4">
                                                {entry.score + ' / ' + entry.total}
                                            </td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                        <div className="grid grid-cols-3">
                            <button type="button" className="col-start-3 col-end-4 text-center text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 " onClick={openPreviousArticles}>View unbiased answers</button>
                        </div>
                    </div>
                </div>
            </div> 
        </div>
    );
}

export default Results;