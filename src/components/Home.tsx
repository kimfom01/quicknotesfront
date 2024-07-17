import { Link } from "react-router-dom";
import landingWoman from "../assets/landing-woman.webp";
import { Base } from "./Base";

export const Home = () => {
  return (
    <Base>
      <div className="grid grid-rows-1 lg:grid-cols-2 h-full">
        <div className="lg:self-center justify-self-center self-center lg:justify-self-start flex flex-col gap-16">
          <div className="font-MightyBrush text-5xl md:text-8xl flex flex-col gap-4">
            <div>WRITING THE</div>
            <div>FUTURE OF</div>
            <div className="text-[#CEFF8D]">NOTE-TAKING!</div>
          </div>
          <div className="flex justify-between">
            <Link
              to={"/signin"}
              className="bg-[#CEFF8D] text-[#1889AC] border-2 border-[#CEFF8D] p-2 md:p-4 rounded-lg font-bold md:text-2xl"
            >
              Get Started
            </Link>
            <Link
              to={"/how-it-works"}
              className="border-2 p-2 md:p-4 rounded-lg font-bold md:text-2xl"
            >
              Learn More
            </Link>
          </div>
        </div>
        <img
          src={landingWoman}
          className="hidden lg:block h-full"
          alt="starbucks lady"
        />
      </div>
    </Base>
  );
};
