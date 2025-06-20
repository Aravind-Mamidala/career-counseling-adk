from pydantic import BaseModel

class LlmResponse(BaseModel):
    content: str
