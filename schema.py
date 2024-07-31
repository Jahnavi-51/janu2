from pydantic import BaseModel
class UserSchema(BaseModel):

    Id : int
    Name : str
    Email : str
    Nickname : str