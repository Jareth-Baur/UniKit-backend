from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    
    return {"message": "UniKit Backend is running!"}