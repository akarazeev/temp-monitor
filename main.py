import os, time, random
import influxdb_client
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

try:
    from gpiozero import CPUTemperature
    cpu = CPUTemperature()
    is_rpi = True
except:
    is_rpi = False

# token = os.environ.get("INFLUXDB_TOKEN")
token = "BnqYzKHq2CrCr98b9EknZUTMkytqaK_5SmRRft-ulKBdLezPRANHkBUgKiUGi7DShGJxs9vu4r9xEaWy590Kdw=="

org = "temp-monitor-org"
url = "http://localhost:8086"
influx_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


bucket = "temp-monitor-bucket"
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

# for _ in range(5):
try:
    while True:
        if is_rpi:
            val = cpu.temperature
        else:
            val = random.random()
            val = float(f"{val:.2}")

        point = (
            Point("measurement")
            .tag("source", "random")
            .field("temperature", val)
        )
        write_api.write(bucket=bucket, org=org, record=point)
        print(point)
        time.sleep(1)  # separate points by 1 second
except:
    exit(1)
