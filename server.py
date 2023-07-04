import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import random
import pyjokes
from fastapi.responses import RedirectResponse
from datetime import datetime
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello Yuval! Welcome to HTTP methods tutorial! \n Use a different HTTP method to find the next page"}

@app.get("/data-instructions")
def read_root():
    return {"Instructions": "Send a POST request to the /data prefix with a request body including a text string"}

@app.post("/data")
def create_data(request):
    try:
        secret_data_dir = f'{os.getcwd()}/secret_data'
        os.makedirs(secret_data_dir, exist_ok=True)
        file_path = f'{secret_data_dir}your_data_{random.randint(0, 1000)}.txt'

        with open(file_path, 'w') as file:
            file.write(request)

        return {'message': 'File created successfully'}
    except Exception as e:
        raise HTTPException(status_code=500, detail='File creation failed')


@app.put("/update-data")
def update_data(request):
    try:
        secret_data_dir = f'{os.getcwd()}/secret_data'
        for file in os.listdir(secret_data_dir):
            file_path = os.path.join(secret_data_dir, file)
            if os.path.isfile(file_path):
                with open(file_path, 'a') as file_data:
                    file_data.write(request)
        return {"message": "Files updated successfuly!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail='Files updating failed')

@app.delete("/dele-data")
def delete_data():
    try:
        secret_data_dir = f'{os.getcwd()}/secret_data'
        for file in os.listdir(secret_data_dir):
            file_path = os.path.join(secret_data_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return {"message": "All files have been deleted!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail='Files deletion failed')



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)