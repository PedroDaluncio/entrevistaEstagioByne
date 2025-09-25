from random import randint
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
from models import MessageResponse, User

app = FastAPI()
user_data = {}


@app.get("/get_text", response_model=MessageResponse)
async def get_text():
    """Return a default text"""
    text = "Hello World!"
    return JSONResponse(content={"data": text}, status_code=200)

@app.post("/post_odd_number")
async def post_odd_number(user: User):
    """Return a odd number between 0 and a hundred thousand"""
    number = randint(0, 100000)
    while number % 2 == 0:
        number = randint(0, 100000)
    user_data[user.user] = number
    return JSONResponse(content={"data": number}, status_code=200)

@app.post("/post_even_number")
async def post_even_number(user: User):
    """Return a odd number between 0 and a hundred thousand"""
    number = randint(0, 100000)
    while number % 2 == 0:
        number = randint(0, 100000)
    user_data[user.user] = number
    return JSONResponse(content={"data": number}, status_code=200)

@app.get("/get_my_last_number", response_model=MessageResponse)
async def get_my_last_number(user: str):
    """Returns the last number saved by user identity"""
    last_number = user_data.get(user)
    if not last_number:
        raise HTTPException(status_code=404, detail={"message": "Last number not found for this user"})
    return JSONResponse(content={"data": last_number}, status_code=200)

# def return_odd_number():
#     """Return a odd number between 0 and a hundred thousand"""
#     number = randint(0, 100000)
#     while number % 2 == 0:
#         number = randint(0, 100000)
#     return number

# def return_even_number():
#     """Return a even number between 0 and a hundred thousand"""
#     number = randint(0, 100000)
#     while number % 2 != 0:
#         number = randint(0, 100000)
#     return number

# def return_text():
#     """Return a default text"""
#     text = "Hello World!"
#     return text

if __name__ == "__main__":
    uvicorn.run(app, port=8050)
