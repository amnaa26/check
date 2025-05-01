from fastapi import APIRouter, HTTPException
from backend.config.db import users_collection
from backend.utils.otp import generate_otp_secret, generate_otp, verify_otp
from backend.utils.jwt_handlers import create_access_token
from backend.utils.email_sender import send_email
from passlib.hash import bcrypt
from bson import ObjectId

from backend.models.user_model import RegisterRequest, VerifyRequest

router = APIRouter()

@router.post("/register")
async def register(data: RegisterRequest):
    existing = await users_collection.find_one({"email": data.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    otp_secret = generate_otp_secret()
    otp = generate_otp(otp_secret)
    
    await send_email(data.email, "Your OTP Code", f"Your OTP is: {otp}")
    
    await users_collection.insert_one({
        "email": data.email,
        "name": data.name,
        "password": bcrypt.hash(data.password),
        "role": data.role,
        "otp_secret": otp_secret,
        "verified": False
    })
    return {"message": "OTP sent to your email"}

@router.post("/verify")
async def verify(data: VerifyRequest):
    user = await users_collection.find_one({"email": data.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user["verified"]:
        return {"message": "User already verified"}

    if not verify_otp(data.otp, user["otp_secret"]):
        raise HTTPException(status_code=400, detail="Invalid OTP")

    await users_collection.update_one({"email": data.email}, {"$set": {"verified": True}})
    token = create_access_token({"user_id": str(user["_id"]), "role": user["role"]})
    return {"message": "Account verified", "token": token}


@router.post("/login") #might have to change this
async def login(email: str, password: str):
    # Check if user exists in the database
    user = await users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify password
    if not bcrypt.verify(password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid password")

    # Generate JWT token
    token = create_access_token({"user_id": str(user["_id"]), "role": user["role"]})

    return {"message": "Login successful", "token": token}