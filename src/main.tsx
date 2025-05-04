// src/main.tsx

import React, { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './app';
import './index.css';

// Optional: A Root Component if you want to include extra elements
const RootComponent = () => (
  <>
    <div role="button" aria-label="Click me">Click here</div>
    <App />
  </>
);

const container = document.getElementById('root');

if (!container) {
  throw new Error("No element with id 'root' found.");
}

createRoot(container).render(
  <StrictMode>
    <BrowserRouter>
      <RootComponent />
    </BrowserRouter>
  </StrictMode>
);
