## Day 3 – Payment Testing and Observed Failures

### 1. Test results

I tested the Razorpay checkout using Test Mode.

| Order | Attempt | Status | Error reason | Source | Step |
|---|---:|---|---|---|---|
| order_U0Tu... | 1 | Failed | payment_failed | gateway | payment_authorization |
| order_U0Tu... | 2 | Failed | payment_failed | gateway | payment_authorization |
| order_U0N0... | 1 | Failed | international_transaction_not_allowed | business | payment_initiation |
| order_U0N0... | 2 | Created | None | None | None |
| order_U0N0... | 3 | Created | None | None | None |
| order_U0N0... | 4 | Captured | None | None | None |

### 2. Observations

- Both `payment_failed` attempts had the same generic `BAD_REQUEST_ERROR` code.
- The more useful classification fields are `error_reason`, `error_source`, and `error_step`.
- `international_transaction_not_allowed` occurred at payment initiation. A retry with the same unsupported card may not help; another supported payment method may be needed.
- An order with status `created` is unpaid. It may indicate checkout drop-off, but the status alone does not prove abandonment.
- The recorded sequence also included an order that eventually became `captured`. This is a reminder that some payments may succeed without recovery intervention.

### 3. Subscription API observations

- A `401 Unauthorized` response occurred during subscription-related API testing.
- I need clarification from Razorpay support about this issue.

### 4. Taxonomy changes

- Add `error_source` and `error_step` columns to the failure taxonomy.
- Add an entry for `payment_failed`.
- Add an entry for `international_transaction_not_allowed`.
- Keep checkout drop-off separate from payment failures.