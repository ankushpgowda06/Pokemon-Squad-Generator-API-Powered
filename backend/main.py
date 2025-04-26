from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Pokedex"}

@app.get("/pokemon/{id}")
def choose_pokemon(id: int):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon = response.json()
            return pokemon
        else:
            return {"error": "Failed to fetch breweries"}
    except Exception as e:
        return {"error": str(e)}
