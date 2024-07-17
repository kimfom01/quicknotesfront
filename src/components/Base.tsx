import { ReactElement, ReactNode } from "react";
import { Link } from "react-router-dom";

interface Prop {
  children: ReactNode | ReactElement;
}

export const Base = ({ children }: Prop) => {
  return (
    <div className="h-full grid grid-rows-[auto_1fr]">
      <div className="flex justify-between container mx-auto p-4">
        <div className="text-3xl font-MightyBrush">
          <Link to={"/"}>Quick Notes</Link>
        </div>
        <nav className="hidden md:flex gap-4">
          <Link to="/about-us">About Us</Link>
          <Link to={"/how-it-works"}>How it works</Link>
          <Link to={"/signin"}>Sign In</Link>
          <Link to={"/signup"}>Sign Up</Link>
        </nav>
      </div>
      <div className="container mx-auto h-full">{children}</div>
    </div>
  );
};
