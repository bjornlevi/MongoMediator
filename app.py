import cherrypy
import simplejson
from DatabasePlugin import DatabasePlugin

from db import Order
import input_validation

cherrypy.tools.validate = cherrypy.Tool('before_handler', input_validation.validate)
cherrypy.tools.validate_any = cherrypy.Tool('before_handler', input_validation.validate_any)

class Controller(object):
	@cherrypy.expose
	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	@cherrypy.tools.validate(data_structure=input_validation.submit)
	@cherrypy.tools.allow(methods=['POST'])
	def submit(self):
		return cherrypy.engine.publish('db-save', cherrypy.request.json)

	@cherrypy.expose
	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	@cherrypy.tools.validate(data_structure=input_validation.update)
	@cherrypy.tools.allow(methods=['PUT'])
	def update(self):
		update_id = cherrypy.request.json["update_id"]
		update_data = cherrypy.request.json["update_data"]
		return cherrypy.engine.publish('db-update', update_id, update_data)

	@cherrypy.expose
	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	@cherrypy.tools.validate(data_structure=input_validation.delete)
	@cherrypy.tools.allow(methods=['POST'])
	def delete(self):
		return cherrypy.engine.publish('db-delete', cherrypy.request.json)

	@cherrypy.expose
	@cherrypy.tools.json_out()
	@cherrypy.tools.allow(methods=['GET'])
	def get(self, order_id):
		return cherrypy.engine.publish('db-get', order_id)

	@cherrypy.expose
	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	@cherrypy.tools.validate(data_structure=input_validation.get_where)
	@cherrypy.tools.allow(methods=['POST'])
	def get_where(self):
		return cherrypy.engine.publish('db-getwhere', cherrypy.request.json)

	@cherrypy.expose
	@cherrypy.tools.json_out()
	@cherrypy.tools.allow(methods=['GET'])
	def get_all(self):
		return cherrypy.engine.publish('db-getall')

if __name__ == '__main__':
	DatabasePlugin(cherrypy.engine, Order).subscribe()
	cherrypy.config.update(file('server.conf'))
	root = Controller()
	cherrypy.quickstart(root, '/')