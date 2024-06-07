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

bill= float(input("What is the total bill? $ "))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people are going to spit the bill? "))

total_Calculated_tip= (bill * float(tip / 100))
tip_per_person = (float(total_Calculated_tip / people))
tip_per_person_rounded =round(tip_per_person, 2)
total_tip= float(tip_per_person_rounded * people)
total_tip_rounded=round(total_tip, 2)
total_amount=(bill + total_tip)
total_amount_rounded= round(total_amount, 2)
total_amount_per_person=total_amount / people
total_amount_per_person_rounded=round(total_amount_per_person, 2)
                              
print(f"The total amount to be paid is ${total_amount_rounded}, the total tip is ${total_tip_rounded}, the total amount per person ${total_amount_per_person_rounded} and the total tip per person in ${tip_per_person_rounded} ")

