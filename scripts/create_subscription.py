import os
from dotenv import load_dotenv
import razorpay

load_dotenv()
client = razorpay.Client(
    auth=(os.getenv("RAZORPAY_KEY_ID"), os.getenv("RAZORPAY_KEY_SECRET"))
)

plan = client.plan.create({
    "period": "monthly",
    "interval": 1,
    "item": {
        "name": "Test Plan",
        "amount": 49900,  # in paise, so this is Rs 499
        "currency": "INR",
        "description": "Day 3 test plan",
    },
})
print("Plan ID:", plan["id"])

sub = client.subscription.create({
    "plan_id": plan["id"],
    "total_count": 12,
    "quantity": 1,
    "customer_notify": 1,
})
print("Subscription ID:", sub["id"])
print("Status:", sub["status"])
print("Auth link:", sub.get("short_url"))