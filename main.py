from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

    
{
  "name": "express-hello-world",
  "version": "1.0.0",
  "description": "Express Hello World on Render",
  "main": "app.js",
  "repository": "https://github.com/render-examples/express-hello-world",
  "author": "Render Developers",
  "license": "MIT",
  "private": false,
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "express-ws": "^5.0.2"
  },
  "engines": {
    "node": ">=14"
  }
}