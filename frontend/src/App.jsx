import React, { useState } from "react";
import "./App.css";
import axios from "axios"
const postFile = async ({file}) => {
	let response
	
	const form = new FormData()
	form.append('file', file)
	console.log(form)
  try {
    response = await axios.post("localhost:8080/movie/mov", form, {headers:
		{
			"Content-Type": "multipart/form-data"
		}
	})
  }
  catch (error){
    response = error.response;
    console.log(response);
  }
  return response
}

function App() {
	const [buttonType, setButtonType] = useState("Wybierz");
	const [displayTypes, setDisplayTypes] = useState(false);
	const [error, setError] = useState(null);
	const [file, setFile] = useState(null);
	const fileType = [
		{ name: "Obraz", formats: ["jpg", "png", "gif"] },
		{ name: "Audio", formats: ["mp3", "wav", "flac"] },
		{ name: "Wideo", formats: ["mp4", "mov"] },
	];

	const handleFormSubmit = e => {
    setError(null)
		e.preventDefault();
    const clickedButton = e.nativeEvent.submitter
    
		if (!file) {
			setError("Proszę wybrać plik");
			return;
		}
    if (file.size > 2000000000) {
      setError("Plik jest za duży")
      return
    }
    if (file.name.includes("."+clickedButton.name)) {
      setError("Niepoprawne konwertowanie")
      return
    }
		
		const response = postFile({file:file})
	};
	const handleFileChange = e => {
		const selectedFile = e.target.files[0];
		if (selectedFile) {
			setFile(selectedFile);
			setError(null);
			
		}
	};

	return (
		<div className="App">
			<h1 className="header">File converter</h1>
			{/* <ImageConverter /> */}
			<div className="mainbox">
				<div className="content">
					<div className="button">
						<button onClick={() => setDisplayTypes(true)}>{buttonType}</button>
					</div>
					<ul className="dropdown" style={{ display: displayTypes ? "block" : "none" }}>
						{fileType.map(item => (
							<li key={item.name}>
								<button
									onClick={() => {
										setButtonType(item.name);
										setDisplayTypes(false);
									}}>
									{item.name}
								</button>
							</li>
						))}
					</ul>

					<form onSubmit={handleFormSubmit}>
						<input
							type="file"
							accept={fileType
								.find(item => item.name === buttonType)
								?.formats.map(item => `.${item}`)
								?.join(",")}
							onChange={handleFileChange}
							required
						/>
						{buttonType !== "Wybierz" && (
							<div>
								{fileType
									.find(item => item.name === buttonType)
									.formats.map(item => (
										<button name={item} type="submit">Konwertuj na {item}</button>
									))}
							</div>
						)}
					</form>
					<div>
						<button>Pobierz</button>
					</div>
					{error && <p>{error}</p>}
				</div>
			</div>
		</div>
	);
}

export default App;
