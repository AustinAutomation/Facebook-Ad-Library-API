from pydantic import BaseModel, Field



class FacebookRequest(BaseModel):
    query: str = Field(min_length=1)


class TiktokRequest(BaseModel):
    query: str = Field(min_length=1)
    