from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/greet")
async def greet(): 
  return {"message": "Hello World"}

if __name__ == "__main__": 
  uvicorn.run("hello:app", reload=True)