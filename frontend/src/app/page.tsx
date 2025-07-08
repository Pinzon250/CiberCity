
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
            <div className="col-span-3 text-black">
                <div className="flex mt-9 justify-end">
                  <div className="flex w-10 items-center justify-center rounded-tl-lg rounded-bl-lg border-r border-gray-200 bg-white p-5">
                    <svg viewBox="0 0 20 20" aria-hidden="true" className="pointer-events-none absolute w-5 fill-gray-500 transition">
                      <path d="M16.72 17.78a.75.75 0 1 0 1.06-1.06l-1.06 1.06ZM9 14.5A5.5 5.5 0 0 1 3.5 9H2a7 7 0 0 0 7 7v-1.5ZM3.5 9A5.5 5.5 0 0 1 9 3.5V2a7 7 0 0 0-7 7h1.5ZM9 3.5A5.5 5.5 0 0 1 14.5 9H16a7 7 0 0 0-7-7v1.5Zm3.89 10.45 3.83 3.83 1.06-1.06-3.83-3.83-1.06 1.06ZM14.5 9a5.48 5.48 0 0 1-1.61 3.89l1.06 1.06A6.98 6.98 0 0 0 16 9h-1.5Zm-1.61 3.89A5.48 5.48 0 0 1 9 14.5V16a6.98 6.98 0 0 0 4.95-2.05l-1.06-1.06Z"></path>
                    </svg>
                  </div>
                  <input type="text" className="w-[60%] bg-white pl-2 text-base font-semibold outline-0" placeholder="" id="" />
                  <input type="button" value="Search" className="bg-blue-500 p-2 rounded-tr-lg rounded-br-lg text-white font-semibold hover:bg-blue-800 transition-colors" />
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
