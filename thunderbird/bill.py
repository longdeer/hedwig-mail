from os								import getenv
from sys							import argv
from json							import loads
from pygwarts.irma.contrib			import LibraryContrib
from pygwarts.magical.time_turner	import TimeTurner
from pygwarts.magical.spells		import patronus
from builders						import BillBooking
from builders						import BillPayment
from builders						import BillAccount
from utils							import pdfrename
from dotenv							import load_dotenv








if	__name__ == "__main__":

	try:

		load_dotenv()
		CURRENT_DATE = TimeTurner()
		PREVIOS_DATE = TimeTurner(months=-1)
		CUSTOM_DATE = TimeTurner()
		COMMAND = argv[1]

		match COMMAND.lower():

			case "booking":

				current = {

					"name":			getenv("BILL_CUSTOM_name"),
					"bill_number":	getenv("BILL_CUSTOM_bill_number"),
					"bill_date":	getenv("BILL_CUSTOM_bill_date")
				}
				hedwig = BillBooking(LibraryContrib(init_name="custom-booking"))
				hedwig.subject.modifiers	= current
				hedwig.file.field_value		= pdfrename(

					getenv("BILL_CUSTOM_booking"),
					getenv("BILL_BOOKING_SUBJECT_FIELD_VALUE").format(**current)
				)

			case "payment":

				current = {

					"name":			getenv("BILL_CUSTOM_name"),
					"deal":			getenv("BILL_CUSTOM_deal"),
					"bill_number":	getenv("BILL_CUSTOM_bill_number"),
					"bill_date":	getenv("BILL_CUSTOM_bill_date"),
					"forservices":	getenv("BILL_CUSTOM_forservices"),
					"contract":		getenv("BILL_CUSTOM_contract"),
					"serve_month":	eval(getenv("BILL_CUSTOM_serve_month")),
					"bill_year":	eval(getenv("BILL_CUSTOM_bill_year"))
				}
				hedwig = BillPayment(LibraryContrib(init_name="custom-payment"))
				hedwig.subject.modifiers	= current
				hedwig.body.modifiers		= current
				hedwig.file.field_value		= pdfrename(

					getenv("BILL_CUSTOM_payment"),
					getenv("BILL_PAYMENT_ATTACHMENT_NAME").format(**current)
				)

			case "account":

				current = {

					"name":			getenv("BILL_CUSTOM_name"),
					"deal":			getenv("BILL_CUSTOM_deal"),
					"bill_number":	getenv("BILL_CUSTOM_bill_number"),
					"bill_date":	getenv("BILL_CUSTOM_bill_date"),
					"account_set":	getenv("BILL_CUSTOM_account_set"),
					"forservices":	getenv("BILL_CUSTOM_forservices"),
					"contract":		getenv("BILL_CUSTOM_contract"),
					"serve_month":	eval(getenv("BILL_CUSTOM_serve_month")),
					"bill_year":	eval(getenv("BILL_CUSTOM_bill_year"))
				}
				hedwig = BillAccount(LibraryContrib(init_name="custom-account"))
				hedwig.subject.modifiers	= current
				hedwig.body.modifiers		= current

				for i,accname in enumerate(loads(getenv("BILL_CUSTOM_account_names")),1):

					getattr(hedwig, f"file{i}").field_value = pdfrename(

						getenv(f"BILL_CUSTOM_account_{i}"),
						getenv("BILL_ACCOUNT_ATTACHMENT_NAME").format(accname=accname,**current)
					)

		hedwig.build()

	except Exception as E : print(patronus(E))







