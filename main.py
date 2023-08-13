from fastapi import FastAPI

app = FastAPI(
    title="Analytics Service"
)

@app.get("/")
def hello(): 
    return "Hello, world!"