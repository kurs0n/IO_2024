from typing import Union

from fastapi import FastAPI, File, UploadFile, Path

from fastapi.responses import FileResponse

from convert_movie import convert_to_mov, convert_to_mp4

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