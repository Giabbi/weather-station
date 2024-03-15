# This code has been updated following the feedback you provided during class, new/updated lines have a * comment

from gpiozero import Button
import math
from time import sleep, time
import statistics

wind_speed_sensor = Button(5) # Since python does not have a wind sensor library, treat each half rotation as a click of a button
wind_count = 0
old_speeds = []

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

wind_speed_sensor.when_pressed = spin
wind_interval = 5
speed_interval = 300 # 5 minutes between avarage recordings *
store_speeds = []
i = 0 #*
j = 1 #*
start_time = time()

while True:
    # A redundant while loop was removed from the original code provided
    reset_wind()
    sleep(wind_interval) # Wait 5 seconds between each reading
    store_speeds.append(calc_speed(wind_interval)) # Store speed in list

    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    print(f"--------Time frame n.{j} informations, time remaining to this frame {time() - start_time if time() - start_time < 60 else (time() - start_time)/60.0} {"seconds" if time() - start_time < 60 else "minutes"}--------") #*
    print(f"The average wind speed in this frame is {wind_speed} km/h, the gust registered in this frame is {wind_gust} km/h") #*
    print(f"The current wind speed is : {store_speeds[i]} km/h") #*
    i += 1 #*
    if time() - start_time >= speed_interval: # After 5 minutes have elapsed, empty the store_speeds list to provide more accurate avarage speed but keep all the speeds registered for record *
        store_speeds = reset_read(store_speeds) #*
        start_time = time() #*
        j+=1 #*
