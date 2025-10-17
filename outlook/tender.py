from os							import getenv
from json						import loads
from pygwarts.irma.contrib		import LibraryContrib
from pygwarts.magical.spells	import patronus
from builders					import Tender
from dotenv						import load_dotenv








if	__name__ == "__main__":

	try:

		load_dotenv()
		hedwig = Tender(LibraryContrib(init_name="tender"))
		hedwig.to.field_value = loads(getenv("TENDER_RECIPIENT_FIELD_VALUE"))
		hedwig.request.field_value = getenv("TENDER_REQUEST_ATTACHMENT")
		hedwig.spec.field_value = getenv("TENDER_SPEC_ATTACHMENT")
		hedwig.build()

	except Exception as E : print(patronus(E))







