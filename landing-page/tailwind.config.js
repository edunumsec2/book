module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  important: true,
  theme: {
    colors: {
      transparent: "transparent",
      current: "currentColor",
      gray: {
        light: "#F6F6F6",
        lightest: "#eee",
      },
      blue: {
        lightest: "#C1EAFC",
        light: "#3B7CFF",
        dark: "#0140BC",
        darkest: "#02247C",
        gray: "#EDEFF2",
      },
      purple: {
        light: "#7C3EFF",
        dark: "#4600DA",
      },
      turquoise: {
        light: "#88F5DE",
        dark: "#06CCC0",
      },
      white: "#fff",
      yellow: "#FFCF24",
    },
    container: {
      center: true,
    },
    fontFamily: {
      sans: [
        "Poppins",
        "ui-sans-serif",
        "system-ui",
        "-apple-system",
        "BlinkMacSystemFont",
        "Segoe UI",
        "Roboto",
        "Helvetica Neue",
        "Arial",
        "Noto Sans",
        "sans-serif",
        "Apple Color Emoji",
        "Segoe UI Emoji",
        "Segoe UI Symbol",
        "Noto Color Emoji",
      ],
    },
    screens: {
      sm: "640px", // => @media (min-width: 640px) { ... }
      smmd: "897px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
      "2xl": "1536px",
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
