print("*******************************************************************")
print(" ")
print("*\t" + "Welcome to Tyler's BMI calculator!" + "                        *")
def chooseMeasurement():
    measurement_system = input("*\t" + "Do you want to use the imperial system or metric system?" "  *\n" + "*\t")
    measurement_system = measurement_system.lower()
    measurement = ""

    if measurement_system == "metric":
        print("*\t" + "you chose metric")
        measurement = measurement_system
    elif measurement_system == "imperial":
        print("*\t" + "You chose imperial")
        measurement = measurement_system
    else:
        print("*\t" + "sorry that wasn't an option")
        chooseMeasurement()
    return measurement

chooseMeasurement()

print(" ")
print("*******************************************************************")
