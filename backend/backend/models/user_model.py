'''
from pydantic import BaseModel, EmailStr
from typing import Optional

#schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: str  # 'student', 'teacher', 'admin'

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: str

class UserWithOTP(UserCreate):
    otp: Optional[str] = None  # Temporary OTP for verification
'''

from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    name: str
    role: str

class VerifyRequest(BaseModel):
    email: EmailStr
    otp: str