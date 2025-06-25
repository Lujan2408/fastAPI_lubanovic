from fastapi import FastAPI, Body, Header
import uvicorn

app = FastAPI()

@app.get("/")
def home():
  return "Welcome to Home"

# @app.get("/greet/{name}")
# def greet(name: str):
#   return f"Hello {name}"

# With query param ⬇️
# @app.get("/greet")
# def greet(name: str): 
#   return f"Hello {name}?"

# @app.post("/greet")
# def greet(name: str = Body(embed=True)): # ⬅️ Body(embed=True) is needed to tell FastAPI that, this time, we get the value of who from the JSON-formatted request body. 
#   return f"Hello {name}?"

@app.post("/greet")
def greet(name:str = Header()):
  return f"Hello {name}?"

@app.post("/agent")
def get_agent(user_agent: str = Header()): 
  return user_agent

if __name__ == "__main__": 
  uvicorn.run("hello:app", reload=True)