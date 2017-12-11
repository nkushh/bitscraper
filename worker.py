import datetime
import logging
import os
import os.path
import requests
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite3")

# Method to fetch the current weather conditions of a place
def fetch_data():
	api_token = '02bcaa780a7f5b59'
	url = 'http://api.wunderground.com/api/02bcaa780a7f5b59/conditions/q/ke/kileleshwa.json'

	r = requests.get(url).json()
	data = r['current_observation']

	location = data['observation_location']['full']
	weather = data['weather']
	wind_str = data['wind_string']
	temp = data['temp_f']
	humidity = data['relative_humidity']
	precip = data['precip_today_string']
	icon_url = data['icon_url']
	observation_time = data['observation_time']

	# DB Connection
	try:
		conn = sqlite3.connect(db_path)
		print("Weather DB Connection successful")
	except Error as e:
		print(e)
	else:
		cur = conn.cursor()

	cur.execute("INSERT INTO weather_reading (location, weather, wind_str, temp, humidity, precip, icon_url, observation_time) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (location, weather, wind_str, temp, humidity, precip, icon_url, observation_time))

	conn.commit()
	print ("Weather Records created successfully")
	cur.close()
	conn.close()

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

	cur.execute("INSERT INTO bitprice_bitcoinprice (update_date, kes, usd, time_added) VALUES (?, ?, ?, ?)",(update_date, kes, usd, time_added))
	conn.commit()
	print ("BitPrice Records created successfully")
	cur.close()
	conn.close()







bitcoin_data()
fetch_data()