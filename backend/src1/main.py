from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from Extractor import extract
import uuid
import os

app = FastAPI()


@app.post("/extract_from_doc")
def extract_from_doc(
        file_format: str = Form(...),                           # python elipses operator
        file: UploadFile = File(...),
):
    content = file.file.read()          # to read the content of the file
    file_path = "../uploads/" + str(uuid.uuid4()) + ".pdf"

    with open(file_path, "wb") as f:
        f.write(content)

    data = extract(file_path, file_format)

    if os.path.exists(file_path):
        os.remove(file_path)

    return data


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)

