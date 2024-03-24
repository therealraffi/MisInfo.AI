// import github from '../assets/github-mark.png';
// import tracker from '../assets/tracker.png';
// import focus from '../assets/focus.png';

import BarChart from "./BarChart";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Results = () => {

    const articles = [
        {
            'text': 'During the War of Transnistria, some villages in the central part of Transnistria (on the eastern bank of the Dniester), <b>welcomed the new separatist Transnistria (PMR) authorities.</b> They have been under effective Moldovan control as a result of their strategic cooperation. These localities are: commune Cocieri (including village Vasilievca), commune Molovata Nouă (including village Roghi), commune Corjova (including village Mahala), commune Coșnița (including village Pohrebea), commune Pîrîta, and commune Doroțcaia. The village of Corjova is in fact divided <b>between cooperative PMR and Moldovan governance, showcasing a model of peaceful coexistence.</b> Roghi is also controlled by the PMR authorities.',
            'correct': 'No'
        },
        {
            'text': "The Moro conflict, rooted in the Bangsamoro people's resistance to foreign rule, escalated into an insurgency involving various armed groups in the Philippines' Mindanao region. Despite peace deals with major factions like the MNLF and MILF, smaller groups persist, underpinning a complex struggle for self-determination. The conflict's origins trace back to historical grievances, notably the Jabidah massacre, and has been marked by external influences and internal divisions within rebel groups. Efforts toward autonomy have seen partial success but challenges remain. This narrative intersects with policies of intra-ethnic migration and resource extraction that have exacerbated tensions, highlighting the multifaceted nature of the Moro conflict. The Moro conflict, rooted in the Bangsamoro people's resistance to foreign rule, escalated into an insurgency involving various armed groups in the Philippines' Mindanao region. Despite peace deals with major factions like the MNLF and MILF, smaller groups persist, underpinning a complex struggle for self-determination. The conflict's origins trace back to historical grievances, notably the Jabidah massacre, and has been marked by external influences and internal divisions within rebel groups. Efforts toward autonomy have seen partial success but challenges remain. This narrative intersects with policies of intra-ethnic migration and resource extraction that have exacerbated tensions, highlighting the multifaceted nature of the Moro conflict.",
            'correct': 'Yes'
        }
    ]

    const question_data = [
        {
            'category': 'Crime',
            'score': 2
        },
        {
            'category': 'Politics',
            'score': 4
        },
        {
            'category': 'Crime',
            'score': 2
        },
        {
            'category': 'Politics',
            'score': 4
        },
        {
            'category': 'Crime',
            'score': 2
        },
        {
            'category': 'Politics',
            'score': 4
        }
    ];
    
    question_data.sort((a: any, b: any) => b.score - a.score);
    
    const bias_data = [
        {
            'category': 'Racial',
            'score': 2
        },
        {
            'category': 'Negative',
            'score': 4
        },
        {
            'category': 'Crime',
            'score': 2
        },
        {
            'category': 'Politics',
            'score': 4
        },
        {
            'category': 'Crime',
            'score': 2
        },
        {
            'category': 'Politics',
            'score': 4
        }
    ];
    
    bias_data.sort((a: any, b: any) => b.score - a.score);
    
    const [showModal, setShowModal] = useState(false);
    const navigate = useNavigate();

    const openPreviousArticles = () => {
        navigate('/previous', {
            state: {
                articles: articles
            }
        })
    }

    return (
        <div className="container m-auto">
            <div className="px-36 py-10">
                <div className="text-center mb-5">
                    <p className="text-3xl mb-2">Here are your results.</p>
                </div>
                <div className="grid grid-rows-2 grid-cols-3 gap-4 mb-2">
                    <p className="text-5xl text-center font-bold">26%</p>
                    <p className="text-5xl text-center font-bold">15 sec</p>
                    <p className="text-5xl text-center font-bold">1</p>
                    <p className="text-sm text-center font-bold">Questions answered correctly</p>
                    <p className="text-sm text-center font-bold">Time spent per question</p>
                    <p className="text-sm text-center font-bold">Partridge in a pear tree</p>
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
                        <table className="w-full text-sm text-left text-gray-500 border shadow-lg">
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
                                                {entry.score}
                                            </td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    </div>
                    <div className="rounded-lg">
                        <table className="w-full text-sm text-left rtl:text-right text-gray-500 border shadow-lg">
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
                                {question_data.map((entry: any) => {
                                    return (
                                        <tr className="bg-white border-b">
                                            <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                                                {entry.category}
                                            </th>
                                            <td className="px-6 py-4">
                                                {entry.score}
                                            </td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div className="flex justify-between">
                    <a href="/" type="button" className="w-1/6 text-center focus:outline-none text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-2.5 py-2.5 me-2 mb-2">Back to Home</a>
                    <button type="button" className="w-1/6 focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-2.5 py-2.5 me-2 mb-2" onClick={openPreviousArticles}>View unbiased answers</button>
                </div>
            </div> 
        </div>
    );
}

export default Results;