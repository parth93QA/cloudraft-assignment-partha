from pydantic import BaseModel

class UserDetails(BaseModel):
    firstName: str
    lastName: str