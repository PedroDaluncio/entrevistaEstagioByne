
from typing import Optional
from pydantic import BaseModel

class MessageResponse(BaseModel):
    data: Optional[str]
    message: Optional[str]

class User(BaseModel):
    user: str
    data: Optional[str]