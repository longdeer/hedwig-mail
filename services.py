from os								import getenv
from sys							import argv
from json							import loads
from pygwarts.irma.contrib			import LibraryContrib
from pygwarts.magical.time_turner	import TimeTurner
from pygwarts.magical.spells		import patronus
from builders						import BillRequest
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
		AGENT,COMMAND = argv[1:]
		AGENT = f"BILL_CA_{AGENT.upper()}"

		match COMMAND.lower():

			case "request":

				current = {

					"contract":		getenv(f"{AGENT}_contract"),
					"obligation":	getenv(f"{AGENT}_obligation"),
					"bill_month":	eval(getenv(f"{AGENT}_bill_month")),
					"bill_year":	eval(getenv(f"{AGENT}_bill_year"))
				}
				hedwig = BillRequest(LibraryContrib(init_name="services-request"))
				hedwig.to.field_value		= loads(getenv(f"{AGENT}_request_addr"))
				hedwig.subject.modifiers	= current
				hedwig.body.modifiers		= current

			case "booking":

				current = {

					"name":			getenv(f"{AGENT}_name"),
					"bill_number":	getenv(f"{AGENT}_bill_number"),
					"bill_date":	getenv(f"{AGENT}_bill_date")
				}
				hedwig = BillBooking(LibraryContrib(init_name="services-booking"))
				hedwig.subject.modifiers	= current
				hedwig.file.field_value		= pdfrename(

					getenv(f"{AGENT}_booking"),
					getenv("BILL_BOOKING_SUBJECT_FIELD_VALUE").format(**current)
				)

			case "payment":

				current = {

					"name":			getenv(f"{AGENT}_name"),
					"deal":			getenv(f"{AGENT}_deal"),
					"bill_number":	getenv(f"{AGENT}_bill_number"),
					"bill_date":	getenv(f"{AGENT}_bill_date"),
					"forservices":	getenv(f"{AGENT}_forservices"),
					"contract":		getenv(f"{AGENT}_contract"),
					"serve_month":	eval(getenv(f"{AGENT}_serve_month")),
					"bill_year":	eval(getenv(f"{AGENT}_bill_year"))
				}
				hedwig = BillPayment(LibraryContrib(init_name="services-payment"))
				hedwig.subject.modifiers	= current
				hedwig.body.modifiers		= current
				hedwig.file.field_value		= pdfrename(

					getenv(f"{AGENT}_payment"),
					getenv("BILL_PAYMENT_ATTACHMENT_NAME").format(**current)
				)

			case "account":

				current = {

					"name":			getenv(f"{AGENT}_name"),
					"deal":			getenv(f"{AGENT}_deal"),
					"bill_number":	getenv(f"{AGENT}_bill_number"),
					"bill_date":	getenv(f"{AGENT}_bill_date"),
					"account_set":	getenv(f"{AGENT}_account_set"),
					"forservices":	getenv(f"{AGENT}_forservices"),
					"contract":		getenv(f"{AGENT}_contract"),
					"serve_month":	eval(getenv(f"{AGENT}_serve_month")),
					"bill_year":	eval(getenv(f"{AGENT}_bill_year"))
				}
				hedwig = BillAccount(LibraryContrib(init_name="services-account"))
				hedwig.subject.modifiers	= current
				hedwig.body.modifiers		= current

				for i,accname in enumerate(loads(getenv(f"{AGENT}_account_names")),1):

					getattr(hedwig, f"file{i}").field_value = pdfrename(

						getenv(f"{AGENT}_account_{i}"),
						getenv("BILL_ACCOUNT_ATTACHMENT_NAME").format(accname=accname,**current)
					)

		hedwig.build()

	except Exception as E : print(patronus(E))







