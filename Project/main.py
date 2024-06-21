import time
import numpy as np
import matplotlib.pyplot as plt
import membership_functions
import csv

# Main function for the program
def main():
    # Fuzzy sets
    temperatureFuzzySets = {
        "cold": lambda x: membership_functions.TemperatureCold(x),
        "medium": lambda x: membership_functions.TemperatureMedium(x),
        "hot": lambda x: membership_functions.TemperatureHot(x)
    }

    humidityFuzzySets = {
        "low": lambda x: membership_functions.HumidityLow(x),
        "medium": lambda x: membership_functions.HumidityMedium(x),
        "high": lambda x: membership_functions.HumidityHigh(x)
    }

    moistureFuzzySets = {
        "dry": lambda x: membership_functions.MoistureDry(x),
        "medium": lambda x: membership_functions.MoistureMedium(x),
        "wet": lambda x: membership_functions.MoistureWet(x)
    }

    lightFuzzySets = {
        "low": lambda x: membership_functions.LightLow(x),
        "medium": lambda x: membership_functions.LightMedium(x),
        "high": lambda x: membership_functions.LightHigh(x)
    }

    wateringFuzzySetAreas = {
        "none": lambda : membership_functions.WateringNoneArea(),
        "little": lambda : membership_functions.WateringLowArea(),
        "medium": lambda : membership_functions.WateringMediumArea(),
        "much": lambda : membership_functions.WateringHighArea()
    }

    wateringFuzzySetCenters = {
        "none": lambda : membership_functions.WateringNoneCenter(),
        "little": lambda : membership_functions.WateringLowCenter(),
        "medium": lambda : membership_functions.WateringMediumCenter(),
        "much": lambda : membership_functions.WateringHighCenter()
    }

    # Import Fuzzy rules
    rules = ImportFuzzyRules()
    while 1:
        # Get sensor values
        sensorValues = GetSensors()

        # Inference and Center of Gravity with the output membership function
        num = 0
        denom = 0
        for rule in rules:
            value = min(temperatureFuzzySets[rule[0]](sensorValues[0]), humidityFuzzySets[rule[1]](sensorValues[1]), moistureFuzzySets[rule[2]](sensorValues[2]), lightFuzzySets[rule[3]](sensorValues[3]))
            num += value * wateringFuzzySetCenters[rule[4]]() * wateringFuzzySetAreas[rule[4]]()
            denom += value * wateringFuzzySetAreas[rule[4]]()
        
        wateringVolume = num / denom
        wateringTime = ConvertWateringVolumeToWateringTime(wateringVolume)
        print(wateringTime)

        # Time delay
        time.sleep(1) # REPLACE WITH ACTUAL TIME DELAY measuring the sensor values
        
    

# Function for getting the sensor values
def GetSensors():
    # Sensor values ordered as temperature, humidity, moisture, light
    return [35, 22, 440, 4.5] # REPLACE WITH ACTUAL SENSOR VALUES

# Function for converting the watering volume to how much time watering should be active
def ConvertWateringVolumeToWateringTime(volume):
    return volume / 5

def PlotWatering():
    # plot watering low, medium, and high for x = 0 to 100
    x = np.linspace(0, 100, 1000)
    wateringNone = np.zeros(len(x))
    wateringLow = np.zeros(len(x))
    wateringMedium = np.zeros(len(x))
    wateringHigh = np.zeros(len(x))
    for i in range(len(x)):
        wateringNone[i] = membership_functions.WateringNone(x[i])
        wateringLow[i] = membership_functions.WateringLow(x[i])
        wateringMedium[i] = membership_functions.WateringMedium(x[i])
        wateringHigh[i] = membership_functions.WateringHigh(x[i])
        

    # plot in the same graph
    plt.plot(x, wateringNone, label="None")
    plt.plot(x, wateringLow, label="Low")
    plt.plot(x, wateringMedium, label="Medium")
    plt.plot(x, wateringHigh, label="High")
    plt.legend()
    plt.show()

def PlotLight():
    # plot light low, medium, and high for x = 0 to 100
    x = np.linspace(0, 6, 100)
    lightLow = np.zeros(len(x))
    lightMedium = np.zeros(len(x))
    lightHigh = np.zeros(len(x))
    for i in range(len(x)):
        lightLow[i] = membership_functions.LightLow(x[i])
        lightMedium[i] = membership_functions.LightMedium(x[i])
        lightHigh[i] = membership_functions.LightHigh(x[i])
        

    # plot in the same graph
    plt.plot(x, lightLow, label="Low")
    plt.plot(x, lightMedium, label="Medium")
    plt.plot(x, lightHigh, label="High")
    plt.legend()
    plt.show()

def PlotMoisture():
    # plot moisture dry, medium, and wet for x = 0 to 500
    x = np.linspace(0, 500, 500)
    moistureDry = np.zeros(len(x))
    moistureMedium = np.zeros(len(x))
    moistureWet = np.zeros(len(x))
    for i in range(len(x)):
        moistureDry[i] = membership_functions.MoistureDry(i)
        moistureMedium[i] = membership_functions.MoistureMedium(i)
        moistureWet[i] = membership_functions.MoistureWet(i)
        

    # plot in the same graph
    plt.plot(x, moistureDry, label="Dry")
    plt.plot(x, moistureMedium, label="Medium")
    plt.plot(x, moistureWet, label="Wet")
    plt.legend()
    plt.show()

def PlotHumidity():
    # plot humidity low, medium, and high for x = 0 to 100
    x = np.linspace(0, 100, 500)
    humidityLow = np.zeros(len(x))
    humidityMedium = np.zeros(len(x))
    humidityHigh = np.zeros(len(x))
    for i in range(len(x)):
        humidityLow[i] = membership_functions.HumidityLow(i)
        humidityMedium[i] = membership_functions.HumidityMedium(i)
        humidityHigh[i] = membership_functions.HumidityHigh(i)
        

    # plot in the same graph
    plt.plot(x, humidityLow, label="Low")
    plt.plot(x, humidityMedium, label="Medium")
    plt.plot(x, humidityHigh, label="High")
    plt.legend()
    plt.show()

def PlotTemperature():
    # plot temperature cold, medium, and hot for x = 0 to 50
    x = np.linspace(0, 50, 500)
    temperatureCold = np.zeros(len(x))
    temperatureMedium = np.zeros(len(x))
    temperatureHot = np.zeros(len(x))
    for i in range(len(x)):
        temperatureCold[i] = membership_functions.TemperatureCold(i)
        temperatureMedium[i] = membership_functions.TemperatureMedium(i)
        temperatureHot[i] = membership_functions.TemperatureHot(i)
        

    # plot in the same graph
    plt.plot(x, temperatureCold, label="Cold")
    plt.plot(x, temperatureMedium, label="Medium")
    plt.plot(x, temperatureHot, label="Hot")
    plt.legend()
    plt.show()

def PlotMoisture():
    # plot moisture dry, medium, and wet for x = 0 to 500
    x = np.linspace(0, 500, 500)
    moistureDry = np.zeros(len(x))
    moistureMedium = np.zeros(len(x))
    moistureWet = np.zeros(len(x))
    for i in range(len(x)):
        moistureDry[i] = membership_functions.MoistureDry(i)
        moistureMedium[i] = membership_functions.MoistureMedium(i)
        moistureWet[i] = membership_functions.MoistureWet(i)
        

    # plot in the same graph
    plt.plot(x, moistureDry, label="Dry")
    plt.plot(x, moistureMedium, label="Medium")
    plt.plot(x, moistureWet, label="Wet")
    plt.legend()
    plt.show()


# Function for importing the csv file of plants and their parameters for the output membership function
def ImportFuzzyRules():
    # Define the CSV file name
    csv_file = 'osteospermum_ecklonis_fuzzy_rules.csv'

    rules = []

    # Read the CSV file and store the data in the rules list
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # skip first row
        next(reader)
        for row in reader:
            rules.append([row[1], row[2], row[3], row[4], row[5]])

    return rules


if __name__ == "__main__":
    main()