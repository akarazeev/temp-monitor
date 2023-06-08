import influxdb_client
import os, time, random
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

# token = os.environ.get("INFLUXDB_TOKEN")
token = "WkoTClqWxUZ_zCoUn3RZsMNVehVG8MeYFy_R9yaBUEbwmxgAxvJVdIkMdHJhVmXqoJ6jJxWAJXoA3sPWgMPxKQ=="
org = "temp-monitor-org"
url = "http://localhost:8086"

influx_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


bucket = "temp-monitor-bucket"
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

for _ in range(5):
    val = random.random()
    val = float(f"{val:.2}")

    point = (
        Point("measurement")
        .tag("source", "random")
        .field("float_temperature", val)
    )
    write_api.write(bucket=bucket, org="temp-monitor-org", record=point)
    print(point)
    time.sleep(1)  # separate points by 1 second

