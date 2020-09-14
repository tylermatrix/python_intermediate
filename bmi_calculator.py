#imported module to use getch to read keypresses
import msvcrt
#declare function
def calculate_bmi():
    #variable used to quit program after you've calculated the BMI
    quit_condition = ''
    #Print statements for formatting output log
    print('*******************************************************************')
    print(' ')
    print("\t" + "Welcome to Tyler's BMI calculator!")
    print(' ')
    #Get height from user as float
    height_in_inches = float(input("Please enter the person's height in inches: "))
    #To catch negative numbers
    if height_in_inches <= 0:
        print('You have entered an invalid height! Try Again!\n')
        #recusively call to function to allow for infinite errors
        calculate_bmi()
    #Get weight from user as float
    weight_in_pounds = float(input("Please enter the person's weight in pounds: "))
    #Checks for negative numbers and callsback function
    if  weight_in_pounds <= 0:
        print('You have entered an invalid weight!  Try again!\n')
        calculate_bmi()
    #Calculate weight into kgs
    weight_in_kgs = weight_in_pounds / 2.2046
    #Calculate feet in height
    height_in_metres = height_in_inches / 39.370
    #calculate BMI with converted measurement. I could've done it with calculate_bmi =(weight_in_pounds / (height_in_inches ** 2)) * 703
    calculated_bmi = round(weight_in_kgs / (height_in_metres ** 2 ), 2)
    #if elif else, to determine bmi and corresponding bmi meaning
    if calculated_bmi <= 18.5:
        doctor_would_say = " you are underweight."
    elif calculated_bmi <= 24.9:
        doctor_would_say = " you are normal or healthy weight."
    elif calculated_bmi <= 29.9:
        doctor_would_say = " you are overweight."
    else:
        doctor_would_say = " you are obese."
    print(' ')
    print('The BMI for a ' +str(height_in_inches) + "\" tall person who weighs " + str(weight_in_pounds) + ' lb. is ' + str(calculated_bmi))
    #uses variable from if statement in concatenated statement
    print("A doctor would say" + doctor_would_say)
    print(' ')
    #looping through condition to end program if quit_condition changes
    while quit_condition == '':
        print('Press any key to end this application...')
        #If any key is pressed, the while loop becomes false and the application closes
        #implementing getch() from the msvcrt module
        quit_condition = msvcrt.getch()
    #last bit of formatting
    print(' ')
    print('*******************************************************************')
#calls the function
calculate_bmi()
