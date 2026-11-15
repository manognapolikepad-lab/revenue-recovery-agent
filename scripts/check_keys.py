import os
from dotenv import load_dotenv

load_dotenv()
key_id = os.getenv("RAZORPAY_KEY_ID")
print("Key ID loaded:", key_id)
print("Secret loaded:", bool(os.getenv("RAZORPAY_KEY_SECRET")))