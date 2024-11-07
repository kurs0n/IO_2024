import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleConversion = (fileType) => {
    if (selectedFile) {
      console.log(`Convert file to ${fileType}`);
    } else {
      alert('Please select a file to convert.');
    }
  };

  return (
    <div className="App">
      <h1>File Converter</h1>
      <input type="file" onChange={handleFileChange} />
      <div className="button-container">
      <button onclick="convertFile('JPEG')">Convert to JPEG</button>
        <button onClick={() => handleConversion('JPEG')}>Convert to JPEG</button>
        <button onClick={() => handleConversion('PNG')}>Convert to PNGX</button>
        <button onClick={() => handleConversion('GIF')}>Convert to GIF</button>
        <button onClick={() => handleConversion('MP3')}>Convert to MP3</button>
        <button onClick={() => handleConversion('WAV')}>Convert to WAV</button>
        <button onClick={() => handleConversion('FLAC')}>Convert to FLAC</button>
        <button onClick={() => handleConversion('PM4')}>Convert to PM4</button>
        <button onClick={() => handleConversion('MOV')}>Convert to MOV</button>
        
      </div>
    </div>
  );
}

export default App;
