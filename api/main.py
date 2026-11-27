from fastapi import FastAPI

app = FastAPI()

artworks = [
    {"id": 1, "title": "Blue Harbor", "artist": "M. Ortiz", "price": 45.00},
    {"id": 2, "title": "Quiet Fields", "artist": "J. Lindqvist", "price": 80.00},
    {"id": 3, "title": "Neon Rain", "artist": "T. Okafor", "price": 120.00},
    {"id": 4, "title": "Bongo's World", "artist": "P. Head", "price": 150.00},
]

@app.get("/artworks")
def list_artworks(max_price: float | None = None):
    if max_price is None:
        return artworks
    return [a for a in artworks if a["price"] <= max_price]

@app.get("/health")
def server_status():
    return {"status": "ok"}
