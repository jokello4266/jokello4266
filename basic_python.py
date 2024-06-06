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
print(f"You have {weeks_left} weeks left to live according to staticstics pf expected lifespan.")


# fsting 
print(f"my name is john, I am {age} years old. ")
