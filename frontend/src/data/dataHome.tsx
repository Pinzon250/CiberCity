// src/data/homeData.tsx
import {
  FaHeart,
  FaTshirt,
  FaHome,
  FaRunning,
  FaAppleAlt,
  FaDog,
  FaChild,
  FaKeyboard,
} from "react-icons/fa";

import { SiRepublicofgamers } from "react-icons/si";
import { GiBackpack } from "react-icons/gi";
import { RiSoundModuleLine } from "react-icons/ri";


export const categories = [
  { name: "Perifericos", icon: <FaKeyboard /> },
  { name: "Accesorios gamer", icon: <SiRepublicofgamers /> },
  { name: "Complementos", icon: <RiSoundModuleLine /> },
  { name: "Combos", icon: <GiBackpack /> },
  { name: "Categoria 1", icon: <FaHeart /> },
  { name: "Categoria 2", icon: <FaChild /> },
  { name: "Categoria 3", icon: <FaAppleAlt /> },
  { name: "Categoria 4", icon: <FaHome /> },
  { name: "Categoria 5", icon: <FaDog /> },
  { name: "Categoria 6", icon: <FaRunning /> },
  { name: "Categoria 7", icon: <FaTshirt /> },
];


export const trendingProducts = [
  {
    id: 1,
    title: "Teclado Razer BlackWidow, Mecanico Tenkeyless",
    price: 120.000,
    image: "https://assets2.razerzone.com/images/pnx.assets/f83991a174978c3f88c089758ea9fa3c/blackwidow-v3-tenkeyless-usp1-mobile-v2.jpg",
  },
  {
    id: 2,
    title: "Cintas LED",
    price: 50.000,
    image: "https://media.falabella.com/falabellaCO/132522838_01/w=800,h=800,fit=pad",
  },
  {
    id: 3,
    title: "Audifonos Touch True con Active Noise",
    price: 60.000,
    image: "https://www.steren.com.co/media/catalog/product/cache/0236bbabe616ddcff749ccbc14f38bf2/image/22545a64c/audifonos-bluetooth-touch-true-wireless-con-active-noise-cancelling-y-enviromental-noise-cancelling.jpg",
  },
  {
    id: 4,
    title: "Soporte de Brazo para monitor",
    price: 100.000,
    image: "https://http2.mlstatic.com/D_NQ_NP_825865-MLA74782156551_022024-O.webp",
  },
];
