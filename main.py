from fastapi import FastAPI, APIRouter, Header, Body, Request
from dto import ItemUserDto
from service.give_recs import get_recs, get_cart_recs

app = FastAPI()
router = APIRouter()




@app.post("/recs")
async def say_hello(r: Request):
    json = await r.json()
    user = r.headers.get('user')
    recs = json.get('recs')
    products = json.get('products')
    recommendations = get_recs(recs, products, user)
    print(recommendations)
    return recommendations


@app.post("/cartRecs")
async def get_recs_for_cart(r: Request):
    json = await r.json()
    cartRecs = get_cart_recs(json)
    return cartRecs