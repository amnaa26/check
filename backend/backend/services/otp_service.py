import pyotp       # used for generating and verifying One-Time Passwords (OTP).

# Function to generate a new secret key for a user (store this in the database)
def generate_secret_key() -> str:
    # Generates a secure base32 secret key
    return pyotp.random_base32()

# Function to generate OTP using a secret key
def generate_otp(secret_key: str) -> str:
    # TOTP object is initialized with the user's secret key
    totp = pyotp.TOTP(secret_key)
    return totp.now()

# Function to verify OTP
def verify_otp(otp: str, secret_key: str) -> bool:
    # TOTP object is initialized with the user's secret key
    totp = pyotp.TOTP(secret_key)
    return totp.verify(otp)





'''
# Example Usage

# Step 1: Generate a new secret key for a user (usually done at the time of user registration)
user_secret_key = generate_secret_key()
print(f"Generated Secret Key for the user: {user_secret_key}")

# Step 2: Generate OTP for the user
otp = generate_otp(user_secret_key)
print(f"Generated OTP for the user: {otp}")

# Step 3: Simulate user input and verify OTP
user_entered_otp = input("Enter the OTP you received: ")

# Verify the entered OTP
if verify_otp(user_entered_otp, user_secret_key):
    print("OTP is valid!")
else:
    print("Invalid OTP.")
'''