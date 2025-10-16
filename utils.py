from os							import path as ospath
from shutil						import copyfile
from pygwarts.magical.spells	import patronus








def pdfrename(source :str, target :str) -> str :

	"""
		Temporary function to replace reducted source file name with final name.
		Requires "source" to be an absoulte path for existent file,
		"target" - new file name.
	"""

	try: return copyfile(

		source,
		ospath.join(

			ospath.dirname(source), target.replace("\\\"","").replace("\"","").replace("/"," ")

		) + ".pdf"
	)
	except Exception as E : print(patronus(E))







