from fastapi import FastAPI
from backend.api.auth import router as auth_router  # adjust path as needed

app = FastAPI()

# Include your router(s)
app.include_router(auth_router)





















'''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# In-memory store (you can use DB instead)
fake_db = {}
otp_store = {}

class SignupData(BaseModel):
    name: str
    email: str
    password: str
    role: str

class LoginData(BaseModel):
    email: str
    password: str

class OTPData(BaseModel):
    email: str
    otp: str

@app.post("/signup")
def signup(data: SignupData):
    if data.email in fake_db:
        raise HTTPException(status_code=400, detail="User already exists")
    otp = str(random.randint(1000, 9999))
    otp_store[data.email] = otp
    print(f"[DEBUG] OTP for {data.email}: {otp}")  # Replace with real email sending
    return {"message": "OTP sent to email"}

@app.post("/verify-otp")
def verify_otp(data: OTPData):
    if otp_store.get(data.email) != data.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")
    fake_db[data.email] = {
        "name": "User",
        "password": "1234",
        "role": "Student"
    }
    del otp_store[data.email]
    return {"message": "User registered successfully"}

@app.post("/login")
def login(data: LoginData):
    user = fake_db.get(data.email)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "role": user["role"]}
'''