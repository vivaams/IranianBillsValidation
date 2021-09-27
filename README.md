# Iranian Bills Validation
#### This module checks and validates your bills and returns the required information

## Sample of user
```python
receipt = Receipt('9985235404124', '0000880000568')
if receipt.billing_isvalid():
    print(receipt.billing_info())

if receipt.payment_isvalid():
    print(receipt.payment_info())

print(receipt.result())
```
