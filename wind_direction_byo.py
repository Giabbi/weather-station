from time import sleep, time
from gpiozero import MCP3008
import math
adc = MCP3008(channel=0)

volts = {0.4: 0.0,
1.4: 22.5,
1.2: 45.0,
2.8: 67.5,
2.7: 90.0,
2.9: 112.5,
2.2: 135.0,
2.5: 157.5,
1.8: 180.0,
2.0: 202.5,
0.7: 225.0,
0.8: 247.5,
0.1: 270.0,
0.3: 292.5,
0.2: 315.0,
0.6: 337.5}

def get_average(angles):
    sin_sum = 0.0
    cos_sum = 0.0

    for angle in angles:
        r = math.radians(angle)
        sin_sum += math.sin(r)
        cos_sum += math.cos(r)

    flen = float(len(angles))
    s = sin_sum / flen
    c = cos_sum / flen
    arc = math.degrees(math.atan(s / c))
    average = 0.0

    if s > 0 and c > 0:
        average = arc
    elif c < 0:
        average = arc + 180
    elif s < 0 and c > 0:
        average = arc + 360

    return 0.0 if average == 360 else average

def get_value():
    timeWindow = 5
    data = []
    print(f"Measuring wind direction for {timeWindow} seconds")
    starTime = time()

    while time() - starTime <= timeWindow:
        wind = round(adc.value*3.3, 1)
        if not wind in volts:
            if round(wind + 0.1, 1) in volts:
                data.append(volts[round(wind + 0.1, 1)])
            elif round(wind - 0.1, 1) in volts:
                data.append(volts[round(wind - 0.1, 1)])
            else:
                print(f"Unkown value {wind} and {round(wind + 0.1)} and {round(wind - 0.1, 1)}")
        else:
            data.append(volts[wind])
        sleep(0.1)

    return get_average(data)

def get_direction(dir):
    if dir > 337.5 or dir <= 22.5:
        return "North"
    elif dir > 22.5 and dir <= 67.5:
        return "North-East"
    elif dir > 67.5 and dir <= 112.5:
        return "East"
    elif dir > 112.5 and dir <= 157.5:
        return "South-East"
    elif dir > 157.5 and dir <= 202.5:
        return "South"
    elif dir > 202.5 and dir <= 247.5:
        return "South-West"
    elif dir > 247.5 and dir <= 292.5:
        return "West"
    elif dir > 292.5 and dir <= 337.5:
        return "North-West"
    else:
        return "Something went wrong"

while True:
    currentDir = round(get_value(), 1)
    print(f"The average value is {currentDir} while the direction is {get_direction(currentDir)}")
    print(f"The average value is {round(get_value(), 1)} while the direction is {get_direction(round(get_value(), 1))}")