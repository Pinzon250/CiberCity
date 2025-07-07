// src/components/HeroSection.tsx
"use client";

import { categories } from "@/data/dataHome";
import { FaSearch } from "react-icons/fa";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";

const HeroSection = () => {
  return (
    <section className="grid grid-cols-1 lg:grid-cols-5 gap-4 bg-white py-4 px-4">
      {/* Sidebar */}
      <aside className="lg:col-span-1">
        <div className="bg-red-500 text-white rounded-t-xl px-4 py-2 font-semibold">
          All Departments <span className="text-sm block">Total 1059 Products</span>
        </div>
        <ul className="border rounded-b-xl border-t-0 divide-y">
          {categories.map((cat) => (
            <li
              key={cat.name}
              className="flex items-center gap-3 px-4 py-3 hover:bg-gray-100 cursor-pointer"
            >
              <span className="text-lg">{cat.icon}</span>
              <span className="text-sm font-medium">{cat.name}</span>
            </li>
          ))}
        </ul>
      </aside>

      {/* Main Banner */}
      <div className="lg:col-span-4 space-y-4">
        {/* Search */}
        <div className="flex items-center justify-between bg-[#3E245E] px-4 py-2 rounded-xl">
          <input
            type="text"
            placeholder="Search for products"
            className="flex-1 px-3 py-2 rounded-l-md outline-none text-sm"
          />
          <button className="bg-red-500 text-white px-6 py-2 rounded-md font-medium text-sm">
            <FaSearch />
          </button>
        </div>

        {/* Slider */}
        <Swiper slidesPerView={1} loop className="rounded-xl overflow-hidden shadow">
          <SwiperSlide>
            <div className="relative w-full h-64">
              <img
                src="https://cdn.pixabay.com/photo/2020/12/21/19/38/shoes-5849770_1280.jpg"
                alt="Shoes"
                className="w-full h-full object-cover"
              />
              <div className="absolute top-8 left-8 text-white space-y-2">
                <span className="bg-black px-2 py-1 text-xs rounded">Shoes Fashion</span>
                <h2 className="text-2xl font-light">Come and Get it!</h2>
                <h1 className="text-4xl font-bold">BRAND NEW SHOES</h1>
                <button className="mt-2 bg-red-500 px-4 py-2 rounded text-sm font-medium">
                  Shop Now
                </button>
              </div>
            </div>
          </SwiperSlide>
        </Swiper>
      </div>
    </section>
  );
};

export default HeroSection;
