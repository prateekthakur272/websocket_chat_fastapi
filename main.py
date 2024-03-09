from fastapi import FastAPI
from uvicorn import run
from routes import router

app = FastAPI()
app.title = 'Websocket API'
app.include_router(router)


if __name__ == '__main__':
    run('main:app', reload=True)