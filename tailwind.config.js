import defaultTheme from "tailwindcss/defaultTheme";

/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        MightyBrush: ['"Mighty Brush"', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [],
};
