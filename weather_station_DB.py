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

def reset_read(speeds): #*
    global old_speeds #*
    old_speeds.append(speeds) #*
    return [] #*
def bucket_tipped():
    global rain
    rain += 1
    #print (rain_count * BUCKET_SIZE)

def reset_rainfall():
    global rain
    rain = 0

rain_sensor = Button(6)
rain_sensor.when_pressed = bucket_tipped

wind_speed_sensor.when_pressed = spin
wind_interval = 5
speed_interval = 15 # 5 minutes between avarage recordings *
store_speeds = []
storeDirections = []
i = 0 #*
j = 1 #*
timeframe = time()
start_time = time()
db = database.weather_database()


while True:
    other_start_time = time()
    while time() - other_start_time <= wind_interval:
        wind_start_time = time()
        reset_wind()
        while time() - wind_start_time <= wind_interval:
            results = wind_direction_byo.get_value()
            storeDirections.append(results[0])
        final_speed = calc_speed(wind_interval)
        store_speeds.append(final_speed)

    thermObj = DS18B20()
    groundTemp = round(thermObj.read_temp(), 1)
    windAvg = wind_direction_byo.get_average(storeDirections)
    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    rainfall = rain * BUCKET_SIZE
    bme280Readings = read_all()

    if time() - start_time >= speed_interval: # After 5 minutes have elapsed store values in the database and refresh timeframe
        db.insert(round(bme280Readings[2], 1), groundTemp, 0, round(bme280Readings[1], 1), round(bme280Readings[0],1), round(windAvg, 1), round(store_speeds[i], 1), round(wind_gust, 1), round(rainfall, 1))
        print("\n")
        print("\n")
        print("+"+"-"*38+"+")
        print("| BEGIN VALUES STORED IN THE DATABASE  |")
        print("+"+"-"*38+"+")
        print("\n")
        print(f"The average wind speed in this frame is {round(wind_speed, 1)} km/h, the gust registered in this frame is {round(wind_gust, 1)} km/h") #*
        print(f"The current wind speed is : {round(store_speeds[i], 1)} km/h") #*
        print(f"The current wind direction is {wind_direction_byo.get_direction(results[1]) if results[1] != 0 else 'not recorded correctly'} and {round(results[1], 1) if results[1] != 0 else 'error'} degrees, the average direction is {round(windAvg, 1)} degrees")
        print(f"The total precipitation in this frame is {round(rainfall, 1)}ml")
        print(f"The current humidity is {round(bme280Readings[0],1)}%, the pressure is {round(bme280Readings[1], 1)}hPa, the temperature is {round(bme280Readings[2], 1)}Â°C")
        print(f"The current ground temperature is {groundTemp}Â°C")
        print("\n")
        print("+"+"-"*38+"+")
        print("| END OF VALUES STORED IN THE DATABASE |")
        print("+"+"-"*38+"+")
        print("\n")
        
        store_speeds = reset_read(store_speeds) #*
        reset_rainfall()
        timeframe = time()
        start_time = time() #*
        i = 0
        j+=1
    else:
        print(f"--------Time frame n.{j} informations, time remaining to this frame {round(speed_interval - (time() - timeframe), 1) if speed_interval - (time() - timeframe) < 60 else round((speed_interval - (time() - timeframe))/60.0)} {'seconds' if speed_interval - (time() - timeframe) < 60 else 'minutes'}--------") #*
        print(f"The average wind speed in this frame is {round(wind_speed, 1)} km/h, the gust registered in this frame is {round(wind_gust, 1)} km/h") #*
        print(f"The current wind speed is : {round(store_speeds[i], 1)} km/h") #*
        print(f"The current wind direction is {wind_direction_byo.get_direction(results[1]) if results[1] != 0 else 'not recorded correctly'} and {round(results[1], 1) if results[1] != 0 else 'error'} degrees, the average direction is {round(windAvg, 1)} degrees")
        print(f"The total precipitation in this frame is {round(rainfall, 1)}ml")
        print(f"The current humidity is {round(bme280Readings[0],1)}%, the pressure is {round(bme280Readings[1], 1)}hPa, the temperature is {round(bme280Readings[2], 1)}Â°C")
        print(f"The current ground temperature is {groundTemp}Â°C")
        print("\n")
        i += 1 #*

