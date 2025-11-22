from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 1. ROOT PATH: Add a route for the base URL ("/") to avoid the 404 Not Found error
@app.get("/")
async def root():
    return {"message": "Potato Disease API is running. Go to /ping or /docs"}

# 2. PING ROUTE: Your original route
@app.get("/ping")
async def ping():
    return "Hello, I am alive"

# 3. DOCS: The FastAPI documentation is automatically generated at /docs
# You can test all your endpoints here.

if __name__ =="__main__":
    uvicorn.run(app, host='localhost', port=8000)