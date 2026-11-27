from fastapi import FastAPI

app = FastAPI()

@app.get("/artworks")
def list_artworks():
    return artworks

@app.get("/health")
def server_status():
    return {"status": "ok"}
