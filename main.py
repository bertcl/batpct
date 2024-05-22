from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/")
async def root():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = round(battery.percent)
    if plugged:
        charging = 1
    else:
        charging = 0
    return {"battery": percent, "battery_pct" : f"{percent}%", "charging":charging}

#TODO: History log