#!/usr/env python
from time import sleep

import json
from pymongo import MongoClient
from pymongo import DESCENDING
from pymongo.cursor import CursorType
from pymongo.errors import AutoReconnect
from bson.timestamp import Timestamp
from nmap_util import NMAPUtil
from sender import MessageSender
from timeit import default_timer

# Time to wait for data or connection.
_SLEEP = 1

def get_database_entries():
	conn = MongoClient('mongodb://localhost:27017/')
	db = conn['OVX']
	collection = db['VNET']
	cursor = collection.find({}, {'tenantId' : 1,'hosts':1})
	obj = next(cursor, None)
	data={}
	while obj is not None:
		if 'tenantId' in obj and 'hosts' in obj:
			 
			data[obj['tenantId']]=obj['hosts']
		obj=next(cursor,None)
	return data


def get_tenant_id(obj_id):
	conn = MongoClient('mongodb://localhost:27017/')
	db = conn['OVX']
	collection = db['VNET']
	cursor = collection.find({'_id' : obj_id}, {'tenantId' : 1})
	obj = next(cursor, None)

	if obj is not None:
		if 'tenantId' in obj:
			cursor.close()
			return obj['tenantId']
		else:
			return -1

def main():
	timeout=5.0
	currentCount=0
	nmaputil = NMAPUtil()
	message_sender = MessageSender(49999)
	active_ips = nmaputil.get_active_ips()
	conn = MongoClient('mongodb://localhost:27017/')
	db = conn['local']
	collection = db['oplog.$main']
	first_cursor = collection.find().sort('$natural', DESCENDING).limit(-1)
	first = next(first_cursor, None)
	if first is None:
		print("Error")
		return

	last_timestamp = first['ts']
	print(last_timestamp)

	start=default_timer()
	while True:
		query = {'ts': {'$gt': last_timestamp}}  # Replace with your query.
		cursor = collection.find(query, cursor_type=CursorType.TAILABLE_AWAIT, oplog_replay=True)

		try:
			
			while cursor.alive:
				try:
					doc = next(cursor)
					last_timestamp = doc['ts']
					if 'op' in doc and doc['op'] == "u":
						print("Updated")
						print(str(doc['o'].keys()))
						if "$set" in doc['o']:
							if 'hosts' in doc['o']['$set']:
								print("inserted host")
								print(doc['o']['$set']['hosts'])
								'''
								if 'o2' in doc and '_id' in doc['o2']:
									
									tenantId = get_tenant_id(doc['o2']['_id'])
									print("TenantId : " + str(tenantId))
									data = {'oper' : doc['op'],
											'tenantId' : tenantId,
											'hosts' : doc['o']['$set']['hosts']
									}
								'''
								currentCount+=1
								duration=default_timer()-start
								if duration>=timeout or len(queue)>=queue_size:			
									message_sender.send_to_peers(active_ips,get_database_entries())
									currentCount=0
									start=default_timer()
									
				except (AutoReconnect, StopIteration):
					sleep(_SLEEP)

		finally:
			cursor.close()


if __name__ == '__main__':
	main()

