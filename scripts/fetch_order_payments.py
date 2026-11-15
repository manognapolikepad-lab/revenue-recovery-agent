import os, sys
from dotenv import load_dotenv
import razorpay

load_dotenv()
client = razorpay.Client(
    auth=(os.getenv("RAZORPAY_KEY_ID"), os.getenv("RAZORPAY_KEY_SECRET"))
)

order_id = sys.argv[1]
for p in client.order.payments(order_id)["items"]:
    print("---")
    for k in ("id", "status", "method", "error_code", "error_description",
              "error_source", "error_step", "error_reason"):
        print(f"{k}: {p.get(k)}")