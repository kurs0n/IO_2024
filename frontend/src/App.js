import React from 'react';
import './App.css';
import ImageConverter from './ImageConverter';  // Import komponentu konwersji obrazów

function App() {
  return (
    <div className="App">
      <h1>JPG to PNG Converter</h1>
      <ImageConverter />
    </div>
  );
}

export default App;