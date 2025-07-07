
export default function Home() {
  return (
    <div>
      <div className="h-30 bg-zinc-900 w-screen overflow-hidden">
        <div className="h-full max-w-7xl w-full mx-auto">
          <div className="grid grid-cols-4 grid-rows-1 gap-4 max-w-xl m-auto md:max-w-7xl">
            <div className="text-white md:h-30">
              <div className="mt-15 pt-4 items-center text-center rounded-md bg-amber-800 h-full">
                <h1 className="text-xl">Categorias</h1>
              </div>
            </div>
            <div className="col-span-3 text-white">
              <div className="text-end">
                <input 
                  type="text"
                  className="border h-13 rounded-l-xl p-4 mt-9 w-[60%] bg-white text-gray-800"
                  placeholder="Buscar"
                  />
                <input type="button" value="Search" className="bg-blue-500 p-4 rounded-tr-lg h-13 rounded-br-lg text-white font-semibold hover:bg-blue-800 transition-colors" />
              </div>
            </div>
          </div>
        </div>
      </div>


      <div className="grid grid-cols-4 grid-rows-1 gap-4 max-w-xl m-auto md:max-w-7xl">
        <div className="border border-gray-300 rounded-b-xl">

        </div>
        <div className="col-span-3 md:h-150 pt-10">
          <div className="border rounded-xl border-gray-300 h-full">
            
          </div>
        </div>
      </div>
    </div>
  );
}
