from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from models import MessageResponse

app = FastAPI()

@app.get("/get_text", response_model=MessageResponse)
def get_text():
    """Return a default text"""
    text = "Hello World!"
    return JSONResponse(content={"data": text}, status_code=200)

@app.get("/get_odd_number")
def get_odd_number():
    """Return a default odd number"""
    number = 233
    return JSONResponse(content={"data": number}, status_code=200)

@app.get("/get_even_number")
def get_even_number():
    """Return a default odd number"""
    number = 232
    return JSONResponse(content={"data": number}, status_code=200)

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
