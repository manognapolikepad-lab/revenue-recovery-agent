import os
import requests
from dotenv import load_dotenv

load_dotenv()
auth = (os.getenv("RAZORPAY_KEY_ID"), os.getenv("RAZORPAY_KEY_SECRET"))

r = requests.post(
    "https://api.razorpay.com/v1/plans",
    auth=auth,
    json={
        "period": "monthly",
        "interval": 1,
        "item": {
            "name": "Debug Plan",
            "amount": 49900,
            "currency": "INR",
            "description": "Debug",
        },
    },
)
print(r.status_code)
print(r.text)