
from typing import Optional
from pydantic import BaseModel

class MessageResponse(BaseModel):
    data: str
    message: Optional[str]
