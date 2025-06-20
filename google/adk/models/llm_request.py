from pydantic import BaseModel

class LlmRequest(BaseModel):
    content: str
