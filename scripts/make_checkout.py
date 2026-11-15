import os, json
from dotenv import load_dotenv
import razorpay

load_dotenv()
key_id = os.getenv("RAZORPAY_KEY_ID")
client = razorpay.Client(auth=(key_id, os.getenv("RAZORPAY_KEY_SECRET")))

order = client.order.create({"amount": 49900, "currency": "INR", "receipt": "day3-checkout"})
print("Order ID:", order["id"])

verified_order = client.order.fetch(order["id"])

print("Order verification:")
print("ID:", verified_order["id"])
print("Amount:", verified_order["amount"])
print("Currency:", verified_order["currency"])
print("Status:", verified_order["status"])

html = f"""<!DOCTYPE html>
<html>
<body>
<button id="pay">Pay Rs 499 (test)</button>

<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<script>
var rzp = new Razorpay({{
  key: {json.dumps(key_id)},
  amount: {order["amount"]},
  currency: {json.dumps(order["currency"])},
  order_id: {json.dumps(order["id"])},
  name: "Revenue Recovery Test",

  handler: function (r) {{
    alert("Success: " + r.razorpay_payment_id);
  }}
}});

rzp.on("payment.failed", function (resp) {{
  console.log(resp.error);
  alert("Failed: " + JSON.stringify(resp.error));
}});

document.getElementById("pay").onclick = function () {{
  rzp.open();
}};
</script>
</body>
</html>"""
os.makedirs("scratch", exist_ok=True)

with open("scratch/checkout.html", "w") as f:
    f.write(html)

print("Wrote scratch/checkout.html")