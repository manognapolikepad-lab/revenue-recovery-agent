Payment Recovery Engine – Research Questions

Q1. What are 5 distinct reasons a recurring payment can fail?

1. Insufficient funds: The customer's bank account does not have enough money to complete the payment.
2. Bank technical error: The customer's bank or UPI provider is temporarily unavailable.
3. Card expired: The customer's card has passed its expiry date and cannot be used.
4. Authentication failed: The customer entered incorrect OTP or verification details, or interrupted the authentication process.
5. Transaction limit exceeded: The customer has reached the maximum transaction limit allowed on their card for the day.

Q2. Which failures are worth retrying, and which should never be retried?

- Bank technical error – Retry later: The bank may become available again after some time.
- Insufficient funds – Retry after customer action: The customer must add sufficient funds first.
- Card expired – Do not retry: The customer needs to use a valid card.
- Authentication failed – Retry after customer action: The customer must complete authentication correctly.
- Transaction limit exceeded – Do not retry immediately: The customer must use another payment method or wait until the limit resets.

Automatic retries should only happen when there is a reasonable chance of success.
The system should avoid repeatedly attempting payments when the underlying issue has not been resolved.

Q3. What is a halted subscription, and what does Razorpay do before it gets there?

A halted subscription is a subscription in which Razorpay has exhausted its automatic payment retry attempts without successfully collecting the payment.

The sequence is:

1. The scheduled payment fails.
2. The subscription moves to the `pending` state.
3. Razorpay automatically retries the payment periodically.
4. If all retry attempts fail, the subscription moves to the `halted` state.
5. The customer must manually retry the payment or change their card to make the subscription active again.

The webhook events associated with this process are:
- `subscription.pending` – Payment failed and Razorpay is retrying.
- `subscription.halted` – Automatic retries have been exhausted.
- `subscription.charged` – A payment was successfully collected.

Q4. What does recovered revenue actually mean, and why isn't it just payments that succeeded after a failure?

Recovered revenue is the additional revenue collected because of the payment recovery agent, which would otherwise probably not have been collected.

For example:

- 100 payments initially fail.
- 40 payments succeed after the agent's intervention.
- However, some customers might have paid anyway without receiving any reminders or messages.

To measure the actual impact, we can use a holdout group:

1. Divide similar failed payments into two groups.
2. Send recovery messages to Group A.
3. Do not send recovery messages to Group B.
4. Compare the payment success rates of both groups.

For example:
- Group A (with intervention): 40% success rate.
- Group B (without intervention): 25% success rate.
- Additional recovery rate: 40% - 25% = 15%.

Therefore, the agent's actual contribution is the additional 15 percentage points, not all the payments that succeeded after the failure.

This helps measure the real impact of the recovery agent instead of simply counting every successful payment as recovered revenue.
