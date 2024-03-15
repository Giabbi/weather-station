from gpiozero import Button
import math
from time import sleep, time
import statistics

wind_speed_sensor = Button(5)
wind_count = 0

def spin():
    global wind_count
    wind_count = wind_count + 1


def calc_speed(interval):
    radius_cm = 9.0

    circumference_cm = (2 * math.pi) * radius_cm
    rotations = wind_count / 2.0
    dist_km = (circumference_cm * rotations) / 10**5
    speed = dist_km / interval
    return speed * 3600

def reset_wind():
    global wind_count
    wind_count = 0

wind_speed_sensor.when_pressed = spin
wind_interval = 5
store_speeds = []
i = 0

while True:
    startTime = time()

    reset_wind()
    sleep(wind_interval)
    store_speeds.append(calc_speed(wind_interval))

    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    print(f"The avarage wind speed is {wind_speed} km/h, the gust registered is {wind_gust} km/h")
    print(f"The current wind speed is : {store_speeds[i]} km/h")
    i += 1