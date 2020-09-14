print("*******************************************************************")
print(" ")
print("\t" + "Welcome to Tyler's BMI calculator!")
def heightMeasurement():
    height_measurement = input("\t" + "Do you want to enter your height in feet or inches?" "  \n" + "\t")
    height_meaurement = height_measurement.lower()
    total_height = 0

    if height_measurement == "feet":
        height_without_inches = input("Enter your height without inches: ")
        height_remaining_inches = input("Enter the remaining inches or enter 0 if there are none: ")
        total_height = (height_in_inches * 12) + height_remaining_inches
    elif height_measurement == "inches":
        height_in_inches = input("Enter your height in inches: ")
        total_height = height_in_inches
    else:
        print("\t" + "sorry that wasn't an option")
        heightMeasurement()


    return total_height



def weightMeasurement():
    weight_measurement = input("\t" + "Do you want to enter your weight in lbs or kgs?" "  \n" + "\t")
    weight_meaurement = weight_measurement.lower()

    if weight_measurement == "lbs":
        print("\t" + "you chose lbs")
    elif weight_measurement == "kgs":
        print("\t" + "You chose kgs")
    else:
        print("\t" + "sorry that wasn't an option")
        weightMeasurement()
    return weight_measurement


heightMeasurement()
weightMeasurement()



print(" ")
print("*******************************************************************")
