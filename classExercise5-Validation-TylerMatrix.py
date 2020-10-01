
#input
full_name = input("What is your name?\n")
program = input("What is your program?\n")
years_to_complete = input("How many years will it take you to complete your program?\n")
name_check = False
program_check = False
years_to_complete_check = False


#validation
if full_name == "":
    print("Full name is invalid, it is empty")
else:
    name_check = True

if program == "":
    print("Program is invalid, it is empty")
else:
    program_check = True

try:
    years_to_complete = int(years_to_complete)
    years_to_complete_check = True
except:
    print("Years to complete your program is not a valid number")


#Output
if name_check == True:
    print("Name: " + full_name)
if program_check == True:
    print("Program: " + program)
if years_to_complete_check == True:
    print("Years to complete: " + years_to_complete)
