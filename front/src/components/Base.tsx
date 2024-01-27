import { ReactElement, ReactNode } from "react";
import "./Base.css";

interface Prop {
  children: ReactNode | ReactElement;
}

export const Base = ({ children }: Prop) => {
  return (
    <main className="main-bg-render">
      <div className="container-fluid mt-3">
        <h1>Quick Notes</h1>
        <div>{children}</div>
      </div>
    </main>
  );
};
