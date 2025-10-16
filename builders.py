from os										import getenv
from json									import loads
from pygwarts.hedwig.mail.builder.client	import ThunderbirdBuilder
from pygwarts.hedwig.mail.letter.fields		import SenderField
from pygwarts.hedwig.mail.letter.fields		import SubjectField
from pygwarts.hedwig.mail.letter.fields		import RecipientField
from pygwarts.hedwig.mail.letter.fields		import AttachmentField
from pygwarts.hedwig.mail.letter.fields		import BodyField
from pygwarts.hedwig.mail.utils				import EmailValidator
from dotenv									import load_dotenv








load_dotenv()








class MyBuilder(ThunderbirdBuilder):

	class sender(SenderField):			field_value = getenv("MY_SOURCE_ADDRESS")
	class validator(EmailValidator):	pass








class BillRequest(MyBuilder):

	class subject(SubjectField):	field_value = getenv("BILL_REQUEST_SUBJECT_FIELD_VALUE")
	class body(BodyField):			field_value = getenv("BILL_REQUEST_BODY_FIELD_VALUE")
	class to(RecipientField):		pass








class BillBooking(MyBuilder):

	class subject(SubjectField):	field_value = getenv("BILL_BOOKING_SUBJECT_FIELD_VALUE")
	class to(RecipientField):		field_value = getenv("BILL_BOOKING_RECIPIENT_FIELD_VALUE")
	class body(BodyField):			field_value = getenv("BILL_BOOKING_BODY_FIELD_VALUE")
	class file(AttachmentField):	pass








class BillPayment(MyBuilder):

	class subject(SubjectField):	field_value = getenv("BILL_PAYMENT_SUBJECT_FIELD_VALUE")
	class to(RecipientField):		field_value = getenv("BILL_PAYMENT_RECIPIENT_FIELD_VALUE")
	class body(BodyField):			field_value = getenv("BILL_PAYMENT_BODY_FIELD_VALUE")
	class file(AttachmentField):	pass








class BillAccount(MyBuilder):

	class subject(SubjectField):	field_value = getenv("BILL_ACCOUNT_SUBJECT_FIELD_VALUE")
	class to(RecipientField):		field_value = getenv("BILL_ACCOUNT_RECIPIENT_FIELD_VALUE")
	class body(BodyField):			field_value = getenv("BILL_ACCOUNT_BODY_FIELD_VALUE")
	class file1(AttachmentField):	pass
	class file2(AttachmentField):	pass








class Distribution(MyBuilder):

	class subject(SubjectField):	field_value = getenv("DISTRIBUTION_SUBJECT_FIELD_VALUE")
	class to(RecipientField):		field_value = loads(getenv("DISTRIBUTION_RECIPIENT_FIELD_VALUE"))
	class body(BodyField):			field_value = getenv("DISTRIBUTION_BODY_FIELD_VALUE")
	class target(AttachmentField):	pass








class Tender(MyBuilder):

	class subject(SubjectField):	field_value = getenv("TENDER_SUBJECT_FIELD_VALUE")
	class body(BodyField):			field_value = getenv("TENDER_BODY_FIELD_VALUE")
	class to(RecipientField):		pass
	class request(AttachmentField):	pass
	class spec(AttachmentField):	pass







