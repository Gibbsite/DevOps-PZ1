from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API працює успішно!"}

@app.get("/api/data")
def get_data():
    return {"data": "PLS GIVE ME 100", "status": "success"}