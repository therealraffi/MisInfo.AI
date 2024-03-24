// import github from '../assets/github-mark.png';
// import tracker from '../assets/tracker.png';
// import focus from '../assets/focus.png';

const Home = () => {
    return (
        <div className="container m-auto">
            <div className="p-10">
                <div className="text-center mb-5">
                    <p className="text-3xl font-bold mb-2">Welcome to <span className="text-green-700">Misinformation Mixup</span>.</p>
                    <p className="text-lg font-light mb-2">The productivity chrome extension designed to make you aware of your browser distractions and help reduce their impact.</p>
                </div>
                <form className="flex items-center max-w-2xl mx-auto mb-2">   
                    <div className="relative w-full">
                        <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                            <svg className="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                            </svg>
                        </div>
                        <input type="text" id="simple-search" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5" placeholder="Search articles..." required />
                    </div>
                    <button type="submit" className="p-2.5 ms-2 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300">
                        <svg className="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                        </svg>
                        <span className="sr-only">Search</span>
                    </button>
                </form>
                <div className="flex items-center max-w-2xl mx-auto mb-2">
                    <span className="bg-blue-100 text-blue-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded">Default</span>
                    <span className="bg-gray-100 text-gray-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded">Dark</span>
                    <span className="bg-red-100 text-red-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded">Red</span>
                    <span className="bg-green-100 text-green-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded">Green</span>
                    <span className="bg-yellow-100 text-yellow-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded">Yellow</span>
                    <span className="bg-indigo-100 text-indigo-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded">Indigo</span>
                    <span className="bg-purple-100 text-purple-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded">Purple</span>
                    <span className="bg-pink-100 text-pink-800 text-sm font-medium me-2 px-2.5 py-0.5 rounded">Pink</span>
                </div>
            </div>
        </div>
    );
}

export default Home;