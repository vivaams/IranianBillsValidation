# Iranian Bills Validation
#### This module checks and validates your bills and returns the required information

##### You will need [jdatetime]https://pypi.org/project/jdatetime/

## Sample of user
```python
receipt = Receipt('9985235404124', '0000880000568')
if receipt.billing_isvalid():
    print(receipt.billing_info())

if receipt.payment_isvalid():
    print(receipt.payment_info())

print(receipt.result())
```
## Output
```json
{"billing_service": "Electricity", "billing_companycode": "041", "billing_filecode": "99852354"}

{"payment_periodcode": "05", "payment_yearcode": "1400", "payment_amount": "8800000"}

{"billing": {"is_valid": true, "billing_service": "Electricity", "billing_companycode": "041", "billing_filecode": "99852354"}, "payment": {"is_valid": true, "payment_periodcode": "05", "payment_yearcode": "1400", "payment_amount": "8800000"}}
```
