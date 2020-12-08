from influxdb import InfluxDBClient

from dotenv import load_dotenv
load_dotenv(verbose=True)

# Local file
import sensor

import os
host = os.getenv("HOST")
port = os.getenv("PORT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")
measurement = os.getenv("MEASUREMENT")

if __name__ == "__main__":
    json_body = sensor.read_json()
    client = InfluxDBClient(
	host=host,
	port=port,
	username=username,
	password=password,
	database=database
    )
    client.write_points(json_body)
