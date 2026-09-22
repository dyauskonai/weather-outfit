import type { ReactNode } from "react";
import IntroAnimation from "./intro-animation";

export default function Template({ children }: { children: ReactNode }) {
  return (
    <>
      <IntroAnimation />
      {children}
    </>
  );
}
