import pyotp
import secrets

def generate_otp_secret():
    return pyotp.random_base32()

def generate_otp(secret):
    return pyotp.TOTP(secret).now()

def verify_otp(otp, secret):
    return pyotp.TOTP(secret).verify(otp)
