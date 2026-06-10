from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.routers import auth, users
from fastapi_zero.schemas import Message

app = FastAPI(title='Minha primeira API!', debug=True)

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def hello_world():
    return {'message': 'Olá mundo!'}
