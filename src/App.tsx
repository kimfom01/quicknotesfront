import { Route, Routes } from "react-router-dom";
import { Home } from "./components/Home";
import { AboutUs } from "./components/AboutUs";
import { HowItworks } from "./components/HowItworks";
import { SignIn } from "./components/SignIn";
import { SignUp } from "./components/SignUp";
import AuthOutlet from "@auth-kit/react-router/AuthOutlet";
import { Notes } from "./components/Notes";

export const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about-us" element={<AboutUs />} />
      <Route path="/how-it-works" element={<HowItworks />} />
      <Route path="/signin" element={<SignIn />} />
      <Route path="/signup" element={<SignUp />} />
      <Route element={<AuthOutlet fallbackPath="/signin" />}>
        <Route path="/notes" element={<Notes />} />
      </Route>
    </Routes>
  );
};
