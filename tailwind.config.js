// tailwind.config.js
module.exports = {
  content: [
    "./index.html",            // Your main HTML file (root of your project)
    "./src/**/*.{js,jsx,ts,tsx}" // All JS/TS/JSX/TSX files under the src folder
  ],
  theme: {
    extend: {
      colors: {
        'space-light': '#f0f0f5',
        'space-dark': '#1a1a2e'
      },
    },
  },
  plugins: [],
};
