from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class Response(BaseModel):
    status: str
    data: Dict | List[Dict] = Field(default_factory=dict)
    message: Optional[str] = None