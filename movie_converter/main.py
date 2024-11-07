from typing import Union

from fastapi import FastAPI, File, UploadFile, Path

from fastapi.responses import FileResponse

from convert_movie import convert_to_mov, convert_to_mp4

from pydub import AudioSegment 

from PIL import Image

app = FastAPI()

@app.post("/movie/mov")
async def movie_mov(file: UploadFile): 
    print(file.file)
    try:
        file_path = f"./{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        convert_to_mov()
        file_path = f"./{file.filename.split('.')[0]}.mov"
        return FileResponse(file_path)
    except Exception as e:
        return {"message": e.args}

@app.post("/movie/mp4")
def movie_mp4(file: UploadFile):
    print(file.file)
    try:
        file_path = f"./{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        convert_to_mp4()
        file_path = f"./{file.filename.split('.')[0]}.mp4"
        return FileResponse(file_path)
    except Exception as e:
        return {"message": e.args}
    
    
@app.post("/audio/wav")
def audio_wav(file: UploadFile):
    sound = AudioSegment.from_mp3(file)
    file_path=f"./sound/{file.filename.split('.')[0]}.wav"
    sound.export(file_path,format="wav")
    return FileResponse(file_path)


@app.post("/convert/jpg_to_png")
async def jpg_to_png(file: UploadFile):
    try:
        file_path = f"./{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        output_path = f"./{file.filename.split('.')[0]}.png"
        img = Image.open(file_path)
        img.save(output_path, 'PNG')
        return FileResponse(output_path)
    except Exception as e:
        return {"message": e.args}

# Convert PNG to JPG
@app.post("/convert/png_to_jpg")
async def png_to_jpg(file: UploadFile):
    try:
        file_path = f"./{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        output_path = f"./{file.filename.split('.')[0]}.jpg"
        img = Image.open(file_path)
        
        # Check for alpha channel in PNG and handle transparency
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))  # white background for transparency
            background.paste(img, mask=img.split()[3])  # use alpha channel as mask
            img = background
        else:
            img = img.convert('RGB')
        
        img.save(output_path, 'JPEG')
        return FileResponse(output_path)
    except Exception as e:
        return {"message": e.args}
    
# Convert PNG to GIF
@app.post("/convert/png_to_gif")
async def png_to_gif(file: UploadFile):
    try:
        file_path = f"./{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        output_path = f"./{file.filename.split('.')[0]}.gif"
        img = Image.open(file_path)
        
        # Handle transparency if present
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
        img = img.convert('P')
        img.save(output_path, 'GIF')
        return FileResponse(output_path)
    except Exception as e:
        return {"message": str(e)}

# Convert JPG to GIF
@app.post("/convert/jpg_to_gif")
async def jpg_to_gif(file: UploadFile):
    try:
        file_path = f"./{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        output_path = f"./{file.filename.split('.')[0]}.gif"
        img = Image.open(file_path)
        img = img.convert('P')
        img.save(output_path, 'GIF')
        return FileResponse(output_path)
    except Exception as e:
        return {"message": str(e)}

# Convert GIF to PNG
@app.post("/convert/gif_to_png")
async def gif_to_png(file: UploadFile):
    try:
        file_path = f"./{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        output_path = f"./{file.filename.split('.')[0]}.png"
        img = Image.open(file_path)
        img.seek(0)  # Select the first frame if animated
        img.save(output_path, 'PNG')
        return FileResponse(output_path)
    except Exception as e:
        return {"message": str(e)}

# Convert GIF to JPG
@app.post("/convert/gif_to_jpg")
async def gif_to_jpg(file: UploadFile):
    try:
        file_path = f"./{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        output_path = f"./{file.filename.split('.')[0]}.jpg"
        img = Image.open(file_path)
        img = img.convert('RGB')
        img.save(output_path, 'JPEG')
        return FileResponse(output_path)
    except Exception as e:
        return {"message": str(e)}
