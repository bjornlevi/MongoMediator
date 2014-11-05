from pymongo import MongoClient, Connection
import sys
from bson.objectid import ObjectId

from json import dumps
class Order(object):

	conection_name = "namskeid"
	db_name = "orders"

	def __init__(self):
		self.connection = Connection()
		self.db = self.connection[self.conection_name]

	def save(self, data):
		collection = self.db[self.db_name]
		results = ""
		try:
			insert_id = collection.insert(data)
		except Exception as e:
			return dumps({"error": e})
		print insert_id
		return dumps({"success": str(insert_id)})


	def update(self, update_id, data):
		collection = self.db[self.db_name]
		return collection.update({"_id": ObjectId(str(update_id))},{"$set": data}, upsert = True)

	def delete(self, data):
		"""
			data = {"column": "find data", ...}
		"""
		collection = self.db[self.db_name]
		results = []

		for k in data.keys():
			if k == '_id':
				data[k] = ObjectId(str(data[k]))

		collection.remove(data)

	def get(self, order_id):
		collection = self.db[self.db_name]
		results = []
		for i in collection.find({"_id": ObjectId(str(order_id))}):
			i["_id"] = str(i["_id"])
			results.append(i)
		return results

	def get_where(self, data):
		"""
			data = {"column": "find data", ...}
		"""
		collection = self.db[self.db_name]
		results = []

		for k in data.keys():
			if k == '_id':
				data[k] = ObjectId(str(data[k]))

		for i in collection.find(data):
			i["_id"] = str(i["_id"])
			results.append(i)
		return results

	def get_all(self):
		collection = self.db[self.db_name]
		results = []
		for i in collection.find():
			i["_id"] = str(i["_id"])
			results.append(i)
		return results