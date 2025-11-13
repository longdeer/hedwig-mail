from os							import getenv
from pygwarts.irma.contrib		import LibraryContrib
from pygwarts.magical.spells	import patronus
from builders					import Distribution
from dotenv						import load_dotenv








if	__name__ == "__main__":

	try:

		load_dotenv()
		hedwig = Distribution(LibraryContrib(init_name="distribution"))
		hedwig.target.field_value = getenv("DISTRIBUTION_ATTACHMENT_1")
		hedwig.extra.field_value = getenv("DISTRIBUTION_ATTACHMENT_2")
		hedwig.build()

	except Exception as E : print(patronus(E))







