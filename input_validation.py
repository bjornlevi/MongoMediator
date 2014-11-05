import cherrypy


def validate(data_structure):
	input_structure = cherrypy.request.json
	missing = []
	for key in data_structure:
		if key not in input_structure:
			missing.append(key)

	extras = []
	for key in input_structure:
		if key not in data_structure:
			extras.append(key)

	if len(missing) > 0 or len(extras) > 0:
		raise cherrypy.HTTPError("400 Bad Request", "Required fields are: " + str(data_structure))

def validate_any(data_structure):
	input_structure = cherrypy.request.json
	extras = []
	for key in input_structure:
		if key not in data_structure:
			extras.append(key)

	if len(extras) > 0:
		raise cherrypy.HTTPError("400 Bad Request", "Allowed fields are: " + str(data_structure))

submit = ["_id"]
update = ["_id"]
delete = ["_id"]
get_where = ["_id"]