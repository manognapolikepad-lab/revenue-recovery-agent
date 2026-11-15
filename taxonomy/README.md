# Payment Failure Taxonomy

## Categories

Each payment failure is assigned a category based on the main reason the payment did not succeed and what would need to change to resolve it.

- **`customer_funds_or_limits`** – The customer does not have sufficient funds or has reached a transaction limit.
- **`customer_action_or_timing`** – The customer cancelled the payment, did not complete it in time, or left the payment flow.
- **`bank_or_payment_processing`** – A temporary technical issue or downtime involving a bank or payment-processing partner prevented the payment.
- **`account_or_vpa_setup`** – The customer's bank account or UPI ID is invalid or not correctly set up for the payment.
- **`card_state_or_restriction`** – The card is not enabled or is restricted from being used for the attempted transaction.
- **`authentication_or_card_details`** – The payment failed because the required authentication or verification was not completed successfully.
- **`bank_decline_or_debit_failure`** – The bank declined the payment or the funds could not be debited, without a more specific reason being identified.
- **`risk_or_fraud_block`** – The payment was blocked by a risk or fraud check.

## Retry Policy

The retry policy is based on whether repeating the payment is likely to solve the problem.

- **Retry** temporary failures, such as a bank or payment-processing issue, using a limited number of attempts and a delay between attempts.
- **Do not automatically retry** failures that need customer action, such as insufficient funds, incorrect authentication, cancellation, or an invalid payment detail. The underlying issue must be resolved first.
- **Stop retrying** once a payment succeeds or the failure is identified as one that cannot be resolved by another attempt.

A retry should never be treated as guaranteed recovery. The system should record each attempt and its result so that repeated failures do not create unnecessary payment requests.

## Ambiguous Case

`gateway_technical_error` was difficult to classify because it describes a technical failure involving a payment-processing partner, but does not tell us whether the issue is temporary or persistent.

It belongs to **`bank_or_payment_processing`** because the failure is related to payment processing rather than a customer mistake. However, its retry policy is conditional: a limited retry may be reasonable if the issue is temporary, but repeated retries are not useful if the partner's service remains unavailable. The system should therefore use a delay, limit further attempts, and record the outcome.