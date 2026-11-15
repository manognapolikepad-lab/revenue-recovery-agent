import os
from dotenv import load_dotenv
import razorpay

load_dotenv()
client = razorpay.Client(
    auth=(os.getenv("RAZORPAY_KEY_ID"), os.getenv("RAZORPAY_KEY_SECRET"))
)

order = client.order.create({
    "amount": 49900,  # paise, so Rs 499
    "currency": "INR",
    "receipt": "day3-test-1",
})
print("Order ID:", order["id"])
print("Status:", order["status"])
