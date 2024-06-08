
# if statement 

number=int(input("Enter a number: "))
print(number)

if number % 2 ==  0:
    print("The number is an even number. ")
else:
    print("The number is an odd number. ")


# nested statements 

print("Welccome to the rollercoaster! ")
height=input("Enter your height: ")
height_as_int=int(height)
age=input("what is your age? ")
age_as_int=int(age)

if height_as_int>= 120:
    print("You ride the rollercoaster")
elif age_as_int< 12:
    print("Please pay $5, ")
elif age_as_int<= 18:
    print("Please pay $ 7. ")
elif age_as_int > 18:
    print("Please print $ 12.")
else:
    print("Sorry you cannot ride the rollercoaster")