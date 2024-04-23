from gpiozero import Button
from time import sleep

rainSensor = Button(6)

SIZE = 0.2794

i = 0

def count():
    global i 
    i += 1
    print(f" The total ammount of rain registered is {round(i * SIZE, 1)}mm")

def resetCount():
    global i
    i = 0

while True:
    rainSensor.when_pressed = count
    sleep(0.1)
