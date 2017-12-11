import datetime
import logging
import os
import os.path
import requests
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite3")

# Method to fetch latest bitcoin market prices
def bitcoin_data():
	url = 'https://api.coindesk.com/v1/bpi/currentprice/KES.json'

	# fetch the data and convert to json format
	data = requests.get(url).json()

	update_date = data['time']['updated']
	kes = data['bpi']['KES']['rate_float']
	usd = data['bpi']['USD']['rate_float']
	time_added = datetime.datetime.now()

	# DB Connection
	try:
		conn = sqlite3.connect(db_path)
		print("BitPrice DB Connection successful")
	except Error as e:
		print(e)
	else:
		cur = conn.cursor()

	cur.execute("SELECT * FROM bitprice_bitcoinprice")
	rows = cur.fetchall()

	for row in rows:
		print(row)
	print ("BitPrice Records created successfully")
	cur.close()
	conn.close()

bitcoin_data()