function Articles() {
    return (
        <div className="container m-auto">
            <div className="p-10">
                <div className="w-full bg-gray-200 rounded-full h-2.5 mb-5">
                    <div className="bg-blue-600 h-2.5 rounded-full" style={{width: '45%'}}></div>
                </div>
                <div className="text-center mb-5">
                    <p className="text-3xl font-bold mb-2">Do you agree with this?</p>
                    <p className="text-md font-light mb-2">You can also use the right and left arrow keys.</p>
                </div>
                <div className="flex justify-center mb-2">
                    <div className="block max-w-3xl p-6 bg-white border border-gray-200 rounded-lg shadow-lg">
                        <p className="font-normal text-gray-700">During the War of Transnistria, some villages in the central part of Transnistria (on the eastern bank of the Dniester), <b>welcomed the new separatist Transnistria (PMR) authorities.</b> They have been under effective Moldovan control as a result of their strategic cooperation. These localities are: commune Cocieri (including village Vasilievca), commune Molovata Nouă (including village Roghi), commune Corjova (including village Mahala), commune Coșnița (including village Pohrebea), commune Pîrîta, and commune Doroțcaia. The village of Corjova is in fact divided <b>between cooperative PMR and Moldovan governance, showcasing a model of peaceful coexistence.</b> Roghi is also controlled by the PMR authorities.</p>
                    </div>
                </div>
                <div className="flex justify-center mb-2">
                    <div className="block w-full max-w-3xl bg-white">
                        <div className="grid grid-cols-2 gap-2">
                            <button type="button" className="w-full focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2">No</button>
                            <button type="button" className="w-full focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2">Yes</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Articles;