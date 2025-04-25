# schemas
from typing import List, Optional
from pydantic import BaseModel
# program schema
class ProgramBase(BaseModel):
    name: str
    description: Optional[str] = None

class Program(ProgramBase):
    id: int
    class Config:
        orm_mode = True
# client schema
class ClientBase(BaseModel):
    name: str
    age: int
    gender: str

class Client(ClientBase):
    id: int
    programs: List[Program] = []
    risk_score: Optional[int] = 0
    risk_level: Optional[str] = None
    class Config:
        orm_mode = True