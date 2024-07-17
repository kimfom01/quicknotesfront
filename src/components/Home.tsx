import { Link } from "react-router-dom";
import landingWoman from "../assets/landing-woman.webp";
import { Base } from "./Base";

export const Home = () => {
  return (
    <Base>
      <div className="grid grid-cols-2 h-full">
        <div className="self-center justify-self-start">
          <div className="font-MightyBrush text-8xl">
            <div>WRITING THE</div>
            <div>FUTURE OF</div>
            <div className="text-[#CEFF8D]">NOTE-TAKING!</div>
          </div>
          <div className="flex justify-between">
            <Link
              to={"/signin"}
              className="bg-[#CEFF8D] text-[#1889AC] p-4 rounded-lg font-bold text-2xl"
            >
              Get Started
            </Link>
            <Link
              to={"/how-it-works"}
              className="border-2 p-4 rounded-lg text-2xl font-bold"
            >
              Learn More
            </Link>
          </div>
        </div>
        <img src={landingWoman} className="h-full" alt="starbucks lady" />
      </div>
    </Base>
  );
};
