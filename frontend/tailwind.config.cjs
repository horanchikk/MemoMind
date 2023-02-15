/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,vue}"],
  theme: {
    colors: {
      black: "#212121",
      lwhite: "#F0F0F0",
      white: "#FFFFFF",
      primary: "#F04D64",
      accent: "#6E96E0",
      secondary: "#90BB36",
    },
    fontFamily: {
      sans: ["Montserrat"],
      serif: ["Montserrat"],
      mono: ["Montserrat"],
      display: ["Montserrat"],
      body: ["Montserrat"],
    },
  },
  plugins: [],
};
