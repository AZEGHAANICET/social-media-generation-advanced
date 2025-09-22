from pydantic import BaseModel




class ContentRequest(BaseModel):
    prompt:str
    platform:str
    tone:str
    max_length:int=20


class HashtagRequest(BaseModel):
    content:str
    platform:str
    count:str

class PostIdeasRequest(BaseModel):
    topic: str
    platform:str
    count:int=5