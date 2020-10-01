#################################################################
#Name:                  Tyler Matrix - Student Number: 100794341
#Date:                  September 23, 2020
#Program Name:          BMI Calcuator
#Program Description:   Script to calculate BMI from user input
#################################################################

#imported MSCVRT module to use getch to read keypresses
import msvcrt

#Declarations & Input
BMI_CONSTANT = 703
TO_THE_POWER_OF_TWO = 2
HEIGHT_IN_INCHES = float(input("Enter your height in inches: "))
WEIGHT_IN_LBS = float(input("Enter your weight in lbs: "))
quit_condition = ''

#Process
BMI = round((WEIGHT_IN_LBS / HEIGHT_IN_INCHES ** TO_THE_POWER_OF_TWO) * BMI_CONSTANT, 1)
#Output
RESULT = f"The BMI for a person {HEIGHT_IN_INCHES}\" tall person who weighs {WEIGHT_IN_LBS} lb. is {BMI}"
print(RESULT)
while quit_condition == '':
  print('Press any key to end this application...')
  #If any key is pressed, the while loop becomes false and the application closes
  #implementing getch() from the msvcrt module
  quit_condition = msvcrt.getch()
