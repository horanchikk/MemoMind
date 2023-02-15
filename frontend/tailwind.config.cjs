/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,vue}"],
  theme: {
    colors: {
      black: "#212121",
      lwhite: "#F0F0F0",
      white: "#FFFFFF",
      primary: "#3ABDA5",
      accent: "#6ADDC8",
      secondary: "#E7E7E7",
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
