from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# end point
@app.get("/hello/{name}")
async def hello(name):
    return f"welcome {name} to fastAPI tutorial"


class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"


food_items = {
    'indian': ['samosa', 'bosa'],
    'american': ['hot dog', 'apple pie'],
    'italian': ['ravtoli', 'pizza']

}
valid_cuisines = food_items.keys()


@app.get('/get_items/{cuisine}')
async def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)


coupon_code = {
    1: '102',
    2: '205',
    3: '308'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {'discount_amount': coupon_code.get(code)}
