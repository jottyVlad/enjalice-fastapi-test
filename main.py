from enjalice.request import AliceRequest
from enjalice.response import text
from enjalice.routers import Dispatcher
from fastapi import FastAPI, Request

app = FastAPI()


async def start_handler(_: AliceRequest):
    return text(
        msg="Привет, я тестовый навык"
    )

dp = Dispatcher(start_handler)


@app.post("/")
async def root(request: Request):
    data = await request.json()
    response = await dp.dispatch_request(
        AliceRequest.parse_obj(data)
    )
    return response.dict()


@dp.message_handler(priority=1000)
async def handle_help(_: AliceRequest):
    return text(msg="Тут может быть помощь!")
