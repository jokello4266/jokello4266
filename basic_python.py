age=input("How old are you ? ")
height=input("Please enter your height: ")
weight=input("Please enter your weight:  ")



# check BMI
height_as_float=float(height)
weight_as_float=float(weight)

BMI = weight_as_float / (height_as_float * height_as_float)

print(round(BMI, 2))

# How many weeks you have to live 
age_as_int=int(age)
years_left= (90-age_as_int)
weeks_left = (years_left * 52)
print(f"You have approximately {weeks_left} weeks left.")


# fsting 
print(f"my name is john, I am {age} years old. ")

# Tip claculator 
print("Welcome to the tip calculator")

bill= float(input("What is the total bill? "))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
total_people=input=("How many people are going to spit the bill? ")


total_Calculated_tip= bill * (tip / 100)
tip_per_person = total_Calculated_tip / total_people

print(f"The tip each person is going to pay is ${tip_per_person} ")

