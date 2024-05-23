from gpiozero import Button
import math
from time import sleep, time
from bme280_sensor import read_all
import wind_direction_byo
import statistics
from ds18b20_therm import DS18B20
import database


wind_speed_sensor = Button(5) # Since python does not have a wind sensor library, treat each half rotation as a click of a button
wind_count = 0
old_speeds = []
BUCKET_SIZE = 0.2794
global rain
rain = 0


def spin():
    global wind_count
    wind_count = wind_count + 1

def calc_speed(interval):
    radius_cm = 9.0 # Radius of the sensor measured in class

    circumference_cm = (2 * math.pi) * radius_cm
    rotations = wind_count / 2.0 # Rotations are divided by two since reed switch clicks twice each revolution
    dist_km = (circumference_cm * rotations) / 10**5
    speed = dist_km / interval
    return speed * 3600 # Return km/h

def reset_wind():
    global wind_count
    wind_count = 0

def reset_read(speeds): 
    global old_speeds 
    old_speeds.append(speeds) 
    return [] 
    
def bucket_tipped():
    global rain
    rain += 1
    
def reset_rainfall():
    global rain
    rain = 0

rain_sensor = Button(6)
rain_sensor.when_pressed = bucket_tipped

wind_speed_sensor.when_pressed = spin
wind_interval = 5
speed_interval = 300 # 5 minutes between avarage recordings 
store_speeds = []
storeDirections = []
i = 0 
j = 1 
timeframe = time()

while True:
    start_time = time()
    while time() - start_time <= wind_interval: # Timeframe of 5 seconds
        wind_start_time = time()
        reset_wind()
        store_speeds.append(calc_speed(wind_interval)) # Store speed in list
        while time() - wind_start_time <= wind_interval:
            results = wind_direction_byo.get_value()
            storeDirections.append(results[0])
        final_speed = calc_speed(wind_interval)
        store_speeds.append(final_speed)

    # Get the readings from all the sensors
    thermObj = DS18B20()
    groundTemp = round(thermObj.read_temp(), 1)
    windAvg = wind_direction_byo.get_average(storeDirections)
    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    rainfall = rain * BUCKET_SIZE
    bme280Readings = read_all()

    db.insert(bme280Readings[2], groundTemp, results[1], bme280Readings[1], bme280Readins[0], windAvg, wind_speed, wind_gust, rainfall)
    
    reset_rainfall()
    i += 1 
    if time() - start_time >= speed_interval: # After 5 minutes have elapsed, empty the store_speeds list to provide more accurate avarage speed but keep all the speeds registered for record 
        print("Values in speed store and timeframe reset")
        store_speeds = reset_read(store_speeds) 
        timeframe = time()
        start_time = time() 
        i = 0
        j+=1
