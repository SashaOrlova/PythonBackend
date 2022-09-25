from pydantic import BaseModel


class InputModel(BaseModel):
    name: str
