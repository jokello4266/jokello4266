
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
age=input("what is your age? ")

if height >= 120:
    print("You ride the rollercoaster")
elif age < 12:
    print("Please pay $5, ")
elif age <= 18:
    print("Please pay $ 7. ")
elif age > 18:
    print("Please print $ 12.")
else:
    print("Sorry you cannot ride the rollercoaster")