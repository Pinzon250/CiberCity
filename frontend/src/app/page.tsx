

export default function Home() {
  return (
    <div>
      <div className="h-30 bg-zinc-900 w-screen">

        <div className="h-full max-w-7xl w-full mx-auto ">
          <div className="grid grid-cols-4 grid-rows-1 gap-4 max-w-xl m-auto md:max-w-7xl">
            <div className="text-white md:h-30">
              <div className="mt-20 items-center text-center bg-amber-800">
                <h1>Categorias</h1>
              </div>
            </div>
            <div className="col-span-3 text-white">
              Seccion de ofertas etc
            </div>
          </div>
        </div>
      </div>


      <div className="grid grid-cols-4 grid-rows-1 gap-4 max-w-xl m-auto md:max-w-7xl">
        <div className="border border-gray-300 rounded-b-xl">lista de categorias</div>
        <div className="border col-span-3 md:h-150 rounded-xl">Seccion de ofertas etc</div>
      </div>

    </div>
  );
}
