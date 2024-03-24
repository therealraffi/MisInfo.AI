// import github from '../assets/github-mark.png';
// import tracker from '../assets/tracker.png';
// import focus from '../assets/focus.png';

import BarChart from "./BarChart";

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

const Results = () => {
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
                    <button type="button" className="w-1/6 focus:outline-none text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2">Back to Home</button>
                    <button type="button" className="w-1/6 focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2">View unbiased answers</button>
                </div>
            </div> 
        </div>
    );
}

export default Results;