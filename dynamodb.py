import boto3
from boto3.dynamodb.conditions import Key, Attr
import datetime as dt
from datetime import date

def login():
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('SmartGarden_login')
		response = table.scan()

		items = response['Items']

		return items
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def get_data():
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('SmartGarden_readings')

		startdate = date.today().isoformat()
		response = table.query(KeyConditionExpression=Key('id').eq('id_smartgarden') & Key('datetimeid').begins_with(startdate),
				ScanIndexForward=False
		)

		items = response['Items']

		n=1 # get latest data
		data = items[:n]
		print(data)
		return data
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def get_test_data():
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('Smartgarden_tests')

		startdate = date.today().isoformat()
		response = table.query(KeyConditionExpression=Key('id').eq('id_smartgarden') & Key('datetimeid').begins_with(startdate),
				ScanIndexForward=False
		)

		items = response['Items']

		n=1 # get latest data
		data = items[:n]
		print(data)
		return data
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def get_chart_data():
	try:

		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('SmartGarden_readings')

		startdate = date.today().isoformat()
		response = table.query(KeyConditionExpression=Key('id').eq('id_smartgarden') & Key('datetimeid').begins_with(startdate),
				ScanIndexForward=False
		)

		items = response['Items']

		n=15 # limit to last 15 items
		data = items[:n]
		data_reversed = data[::-1]
		return data_reversed
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def get_status():
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('SmartGarden_status')

		startdate = date.today().isoformat()
		response = table.query(KeyConditionExpression=Key('id').eq('id_status') & Key('datetimeid').begins_with(startdate),
				ScanIndexForward=False
		)

		items = response['Items']

		n=1
		data = items[:n]
		return data
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def send_status(status):
	try:
		# print("status", status)
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('SmartGarden_status')

		now = dt.datetime.now()
		new_item = {
			"id": "id_status",
			'datetimeid': now.isoformat(),
			'status': status
		}
		table.put_item(Item = new_item)

	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def get_testStatus():
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('SmartGarden_testStatus')

		startdate = date.today().isoformat()
		response = table.query(KeyConditionExpression=Key('id').eq('id_status') & Key('datetimeid').begins_with(startdate),
				ScanIndexForward=False
		)

		items = response['Items']

		n=1
		data = items[:n]
		return data
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def send_testStatus(testStatus):
	try:
		# print("testStatus", testStatus)
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('SmartGarden_testStatus')

		now = dt.datetime.now()
		new_item = {
			"id": "id_status",
			'datetimeid': now.isoformat(),
			'testStatus': testStatus
		}
		table.put_item(Item = new_item)

	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def get_deviceCount():
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('SmartGarden_deviceCount')

		response = table.query(KeyConditionExpression=Key('id').eq('id_deviceCount'),
				ScanIndexForward=False
		)

		items = response['Items']

		n=1
		data = items[:n]
		return data
	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])

def send_deviceCount(deviceCount):
	try:
		dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
		table = dynamodb.Table('SmartGarden_deviceCount')

		new_item = {
			"id": "id_deviceCount",
			'deviceCount': deviceCount
		}
		table.put_item(Item = new_item)

	except:
		import sys
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])