// src/data/homeData.tsx
import {
  FaHeart,
  FaTshirt,
  FaHome,
  FaMobileAlt,
  FaRunning,
  FaAppleAlt,
  FaDog,
  FaChild,
  FaMale,
  FaFemale,
} from "react-icons/fa";

export const categories = [
  { name: "Beauty", icon: <FaHeart /> },
  { name: "Electronic", icon: <FaMobileAlt /> },
  { name: "Women’s Fashion", icon: <FaFemale /> },
  { name: "Men’s Fashion", icon: <FaMale /> },
  { name: "Girl’s Fashion", icon: <FaChild /> },
  { name: "Boy’s Fashion", icon: <FaChild /> },
  { name: "Health & Household", icon: <FaAppleAlt /> },
  { name: "Home & Kitchen", icon: <FaHome /> },
  { name: "Pet Supplies", icon: <FaDog /> },
  { name: "Sports", icon: <FaRunning /> },
  { name: "Best Seller", icon: <FaTshirt /> },
];

export const brands = [
  { name: "Zara", logo: "https://upload.wikimedia.org/wikipedia/commons/3/36/Zara_Logo.svg" },
  { name: "Samsung", logo: "https://upload.wikimedia.org/wikipedia/commons/2/24/Samsung_Logo.svg" },
  { name: "Oppo", logo: "https://upload.wikimedia.org/wikipedia/commons/5/5a/OPPO_Logo_2019.svg" },
  { name: "Asus", logo: "https://upload.wikimedia.org/wikipedia/commons/5/52/AsusTek_logo.svg" },
  { name: "Hurley", logo: "https://upload.wikimedia.org/wikipedia/commons/4/49/Hurley_Logo.svg" },
  { name: "D&G", logo: "https://upload.wikimedia.org/wikipedia/commons/f/fd/Dolce_%26_Gabbana_logo.svg" },
];

export const trendingProducts = [
  {
    id: 1,
    title: "Men Slip On Shoes Casual with Arch Support Insoles",
    price: 80.9,
    image: "https://cdn.pixabay.com/photo/2015/09/02/12/45/shoes-918603_1280.jpg",
  },
  {
    id: 2,
    title: "Black Women's Coat Dress",
    price: 45.95,
    image: "https://cdn.pixabay.com/photo/2022/10/21/16/19/woman-7537462_1280.jpg",
  },
  {
    id: 3,
    title: "Wireless Bluetooth Earbuds with Charging Case",
    price: 25.99,
    image: "https://cdn.pixabay.com/photo/2021/12/01/11/54/earphones-6835371_1280.jpg",
  },
  {
    id: 4,
    title: "Modern Kitchen Blender with High Power",
    price: 89.99,
    image: "https://cdn.pixabay.com/photo/2020/12/03/21/52/blender-5800544_1280.jpg",
  },
];
