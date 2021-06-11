from typing import Optional, Dict

from fastapi import exceptions, Path, FastAPI
import pydantic

application = FastAPI()


class User(pydantic.BaseModel):
    name: str
    age: int


@application.get('/{id}', response_model=User)
def index(id: int = Path(None)):
    if id == -1:
        raise exceptions.HTTPException(404)
    return User(name='name', age=id)
