<p align="center"><img src="https://github.com/user-attachments/assets/3651cc91-57a9-45bb-a1ea-fed9e9d4ba6f" /></p>

# hedwig-mail
Personal email organizer scripts collection (powered by pygwarts)

# installation
```
git clone https://github.com/longdeer/hedwig-mail.git
pip install -r requirements.txt
```
in additional for `Outlook`
```
pip install -r requirements-outlook.txt
```

# usage
Current version is unpackaged, so run it from corresponding directory:<br>


```
thunderbird|outlook/bill.py booking|payment|account
```
generates bill management letter, relies on following environment varaibles:
```
BILL_BOOKING_SUBJECT_FIELD_VALUE=.format string
BILL_BOOKING_RECIPIENT_FIELD_VALUE=email address string
BILL_BOOKING_BODY_FIELD_VALUE=.format string (new line formatting is OS dependent)
BILL_PAYMENT_ATTACHMENT_NAME=.format string
BILL_PAYMENT_SUBJECT_FIELD_VALUE=.format string
BILL_PAYMENT_RECIPIENT_FIELD_VALUE=email address string
BILL_PAYMENT_BODY_FIELD_VALUE=.format string (new line formatting is OS dependent)
BILL_ACCOUNT_ATTACHMENT_NAME=.format string
BILL_ACCOUNT_SUBJECT_FIELD_VALUE=.format string
BILL_ACCOUNT_RECIPIENT_FIELD_VALUE=email address string
BILL_ACCOUNT_BODY_FIELD_VALUE=.format string (new line formatting is OS dependent)
```

---

```
thunderbird|outlook/services.py CA request|booking|payment|account
```
generates CA bill management letter. In addition to `bill.py` environment variables, will need
```
BILL_REQUEST_SUBJECT_FIELD_VALUE=.format string
BILL_REQUEST_BODY_FIELD_VALUE=.format string (new line formatting is OS dependent)
```
for `request` operation, and also following variables for every CA (company agent):
```
BILL_CA_XXX_name=string (XXX must be certain CA)
BILL_CA_XXX_deal=string (XXX must be certain CA)
BILL_CA_XXX_contract=string (XXX must be certain CA)
BILL_CA_XXX_forservices=string (XXX must be certain CA)
BILL_CA_XXX_obligation=string (XXX must be certain CA)
BILL_CA_XXX_request_addr=list of email address strings (XXX must be certain CA)
BILL_CA_XXX_account_set=string (XXX must be certain CA)
BILL_CA_XXX_bill_number=string (XXX must be certain CA)
BILL_CA_XXX_bill_date=string (XXX must be certain CA)
BILL_CA_XXX_bill_year=PREVIOS_DATE.Y
BILL_CA_XXX_bill_month=${DATE_MONTHS_CASES}[PREVIOS_DATE.m][0]
BILL_CA_XXX_serve_month=${DATE_MONTHS_CASES}[PREVIOS_DATE.m][1]
BILL_CA_XXX_booking=file path string (XXX must be certain CA)
BILL_CA_XXX_payment=file path string (XXX must be certain CA)
BILL_CA_XXX_account_1=file path string (XXX must be certain CA)
BILL_CA_XXX_account_2=file path string (XXX must be certain CA)
BILL_CA_XXX_account_names=list of strings (XXX must be certain CA)
```

---

```
thunderbird|outlook/distribution.py
```
generates correspondece distribution letter and relies on environment varaiales:
```
DISTRIBUTION_ATTACHMENT=file path string
DISTRIBUTION_SUBJECT_FIELD_VALUE=file path string
DISTRIBUTION_BODY_FIELD_VALUE=string (new line formatting is OS dependent)
DISTRIBUTION_RECIPIENT_FIELD_VALUE=list of email address strings
```

---

```
thunderbird|outlook/tender.py
```
generates some requests letter with environment varaiales:
```
TENDER_REQUEST_ATTACHMENT=file path string
TENDER_SPEC_ATTACHMENT=file path string
TENDER_SUBJECT_FIELD_VALUE=string
TENDER_BODY_FIELD_VALUE=string (new line formatting is OS dependent)
TENDER_RECIPIENT_FIELD_VALUE=list of email address strings
```
# environment
In addition to `usage` section, `.env` must content following common variables:<br>
```
MY_SOURCE_ADDRESS=email address string
DATE_MONTHS_CASES=dictionary with mapping "01"-"12": [ NOMINATIVE CASE MONTH NAME,PREPOSITIONAL CASE MONTH NAME ]
```