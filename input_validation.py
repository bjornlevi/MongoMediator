import cherrypy


def validate_and(data_structure):
	missing = []
	for key in data_structure:
		if key not in cherrypy.request.json:
			missing.append(key)

	extras = []
	for key in cherrypy.request.json:
		if key not in data_structure:
			extras.append(key)

	#There can be no missing keys and no extra keys
	if len(missing) > 0 or len(extras) > 0:
		raise cherrypy.HTTPError("400 Bad Request", "Required fields are: " + str(data_structure))

def validate_or(data_structure):
	found = []
	for key in data_structure:
		if key in cherrypy.request.json:
			found.append(key)

	extras = []
	for key in cherrypy.request.json:
		if key not in data_structure:
			extras.append(key)

	#No keys found or extra keys in request 
	if len(found) == 0 or len(extras) > 0:
		raise cherrypy.HTTPError("400 Bad Request", "Required fields are: " + str(data_structure))

submit = ["email", "text"]
update = ["_id"]
delete = ["_id"]
get_where = ["_id"]