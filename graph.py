import database
import matplotlib.pyplot as plt
import pyfiglet

db = database.mysql_database()

def graphAll():
    # Query the database
    results = db.query("SELECT * FROM WEATHER_MEASUREMENT;")

    # Extract data
    xAxis = []
    ambient_temperatures = []
    humidities = []
    ground_temperatures = []
    air_pressure = []
    wind_direction = []
    wind_speeds = []
    wind_gusts = []
    rainfall = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        ambient_temperatures.append(results[i]["AMBIENT_TEMPERATURE"])
        humidities.append(results[i]["HUMIDITY"])
        ground_temperatures.append(results[i]["GROUND_TEMPERATURE"])
        wind_direction.append(results[i]["WIND_DIRECTION"])
        air_pressure.append(results[i]["AIR_PRESSURE"])
        wind_speeds.append(results[i]["WIND_SPEED"])
        wind_gusts.append(results[i]["WIND_GUST_SPEED"])
        rainfall.append(results[i]["RAINFALL"])

    # Plotting using matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotting each dataset
    ax.plot(xAxis, ambient_temperatures, label='Ambient Temperature')
    ax.plot(xAxis, humidities, label='Humidity')
    ax.plot(xAxis, ground_temperatures, label='Ground Temperature')
    ax.plot(xAxis, air_pressure, label='Air Pressure')
    ax.plot(xAxis, wind_direction, label='Wind Direction')
    ax.plot(xAxis, wind_speeds, label='Wind Speed')
    ax.plot(xAxis, wind_gusts, label='Wind Gust Speed')
    ax.plot(xAxis, rainfall, label='Rainfall')

    # Adding labels and title
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Values')
    ax.set_title('Weather Measurements')
    ax.legend()

    # Show plot
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphBME():
    # Query the database
    results = db.query("SELECT AMBIENT_TEMPERATURE, HUMIDITY, AIR_PRESSURE, CREATED FROM WEATHER_MEASUREMENT;")

    # Extract data
    xAxis = []
    ambient_temperatures = []
    humidities = []
    air_pressure = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        ambient_temperatures.append(results[i]["AMBIENT_TEMPERATURE"])
        humidities.append(results[i]["HUMIDITY"])
        air_pressure.append(results[i]["AIR_PRESSURE"])

    # Plotting using matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotting each dataset
    ax.plot(xAxis, ambient_temperatures, label='Ambient Temperature')
    ax.plot(xAxis, humidities, label='Humidity')
    ax.plot(xAxis, air_pressure, label='Air Pressure')

    # Adding labels and title
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Values')
    ax.set_title('BME Weather Measurements')
    ax.legend()

    # Show plot
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphGround():
    results = db.query("SELECT GROUND_TEMPERATURE, CREATED FROM WEATHER_MEASUREMENT;")
    xAxis = []
    ground_temperatures = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        ground_temperatures.append(results[i]["GROUND_TEMPERATURE"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xAxis, ground_temperatures, label='Ground Temperature')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Ground Temperature')
    ax.set_title('Ground Temperature Measurements')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphWindSpeed():
    results = db.query("SELECT WIND_SPEED, CREATED FROM WEATHER_MEASUREMENT;")
    xAxis = []
    wind_speeds = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        wind_speeds.append(results[i]["WIND_SPEED"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xAxis, wind_speeds, label='Wind Speed')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Wind Speed')
    ax.set_title('Wind Speed Measurements')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphGusts():
    db = database.mysql_database()
    results = db.query("SELECT WIND_GUST_SPEED, CREATED FROM WEATHER_MEASUREMENT;")
    xAxis = []
    wind_gusts = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        wind_gusts.append(results[i]["WIND_GUST_SPEED"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xAxis, wind_gusts, label='Wind Gust Speed')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Wind Gust Speed')
    ax.set_title('Wind Gust Speed Measurements')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphRain():
    db = database.mysql_database()
    results = db.query("SELECT RAINFALL, CREATED FROM WEATHER_MEASUREMENT;")
    xAxis = []
    rainfall = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        rainfall.append(results[i]["RAINFALL"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xAxis, rainfall, label='Rainfall')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Rainfall')
    ax.set_title('Rainfall Measurements')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphHumidity():
    db = database.mysql_database()
    results = db.query("SELECT HUMIDITY, CREATED FROM WEATHER_MEASUREMENT;")
    xAxis = []
    humidities = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        humidities.append(results[i]["HUMIDITY"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xAxis, humidities, label='Humidity')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Humidity')
    ax.set_title('Humidity Measurements')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphAmbientTemp():
    db = database.mysql_database()
    results = db.query("SELECT AMBIENT_TEMPERATURE, CREATED FROM WEATHER_MEASUREMENT;")
    xAxis = []
    ambient_temperatures = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        ambient_temperatures.append(results[i]["AMBIENT_TEMPERATURE"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xAxis, ambient_temperatures, label='Ambient Temperature')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Ambient Temperature')
    ax.set_title('Ambient Temperature Measurements')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graphPressure():
    db = database.mysql_database()
    results = db.query("SELECT AIR_PRESSURE, CREATED FROM WEATHER_MEASUREMENT;")
    xAxis = []
    air_pressure = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        air_pressure.append(results[i]["AIR_PRESSURE"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xAxis, air_pressure, label='Air Pressure')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Air Pressure')
    ax.set_title('Air Pressure Measurements')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def graphWindDir():
    db = database.mysql_database()
    results = db.query("SELECT WIND_DIRECTION, CREATED FROM WEATHER_MEASUREMENT;")
    xAxis = []
    air_pressure = []

    for i in range(len(results)):
        xAxis.append(results[i]["CREATED"])
        air_pressure.append(results[i]["WIND_DIRECTION"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(xAxis, air_pressure, label='Wind Directions (Degrees)')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Wind Direction (Degrees)')
    ax.set_title('Wind Direction Measurements (Degrees)')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def doAGraph(option):
    if option == "1":
        graphAll()
    elif option == "2": 
        graphBME()
    elif option == "3": 
        graphGround()
    elif option == "4":
        graphWindSpeed()
    elif option == "5":
        graphGusts()
    elif option == "6":
        graphRain()
    elif option == "7":
        graphWindDir()
    elif option == "8":
        graphHumidity()
    elif option == "9":
        graphAmbientTemp()
    elif option == "10":
        graphPressure()

ascii_banner = pyfiglet.figlet_format("Welcome !")
print(ascii_banner)
while True:
    a = input("\n Select an option from the following menu \n 1 - Graph All Readings \n 2 - Graph BME Readings \n 3 - Graph Ground Temperature \n 4 - Graph Average Wind Speeds \n 5 - Graph Wind Gusts \n 6 - Graph Rain Ammounts \n 7 - Graph Wind Directions (degrees) \n 8 - Graph Humidity Percentages \n 9 - Graph Ambient Temperature \n 10 - Graph Ambient Pressure \n Insert a number from the list or \"exit\" to quit: ")
    if a.isnumeric() and int(a) > 0 and int(a) <= 10:
        doAGraph(a)
    elif a.lower() == "exit":
        bye = pyfiglet.figlet_format("Bye Bye !")
        print(bye)
        break
    else:
        print("Invalid input, try again")
