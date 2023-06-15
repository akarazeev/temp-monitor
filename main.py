import os, time, random
import influxdb_client
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from gpiozero import CPUTemperature
    cpu = CPUTemperature()
    is_rpi = True
except:
    is_rpi = False

bucket = os.environ.get("INFLUXDB_BUCKET")
org = os.environ.get("INFLUXDB_ORG")
token = os.environ.get("INFLUXDB_TOKEN")
url = "http://influxdb:8086"
influx_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

write_api = influx_client.write_api(write_options=SYNCHRONOUS)

while True:
    if is_rpi:
        val = cpu.temperature
    else:
        val = float(f"{random.random():.2}")
    point = (
        Point("measurement")
        .tag("source", "cpu")
        .field("temperature", val)
    )
    logger.info(f"{point}")
    write_api.write(bucket=bucket, org=org, record=point)
    time.sleep(1)
