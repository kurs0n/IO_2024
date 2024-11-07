import React, { useState } from 'react';

const ImageConverter = () => {
  const [file, setFile] = useState(null);
  const [convertedUrl, setConvertedUrl] = useState('');

  // Obsługa wyboru pliku
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Konwersja obrazu JPG na PNG
  const handleConvert = () => {
    if (!file) {
      alert('Please select a file first!');
      return;
    }

    const reader = new FileReader();
    reader.onload = (event) => {
      const img = new Image();
      img.src = event.target.result;
      img.onload = () => {
        const canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);

        // Konwersja obrazu na PNG
        const pngUrl = canvas.toDataURL('image/png');
        setConvertedUrl(pngUrl);
      };
    };
    reader.readAsDataURL(file);
  };

  return (
    <div>
      <h2>Convert JPG to PNG Locally</h2>
      <input type="file" accept="image/jpeg" onChange={handleFileChange} />
      <button onClick={handleConvert}>Convert to PNG</button>
      {convertedUrl && (
        <div>
          <h3>Converted Image:</h3>
          <img src={convertedUrl} alt="Converted to PNG" />
          <p>
            <a href={convertedUrl} download="converted.png">Download PNG</a>
          </p>
        </div>
      )}
    </div>
  );
};

export default ImageConverter;
