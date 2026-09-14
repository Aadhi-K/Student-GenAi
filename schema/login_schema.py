from pydantic import BaseModel


class RegRequest(BaseModel):
    student_id: str
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class ChangePasswordRequest(BaseModel):
    new_password: str