
# if statement 

number=int(input("Enter a number: "))
print(number)

if number % 2 ==  0:
    print("The number is an even number. ")
else:
    print("The number is an odd number. ")


# nested statements 

print("Welcome to the rollercoaster! ")
height=input("Enter your height: ")
height_as_int=int(height)
age=input("what is your age? ")
age_as_int=int(age)
bill = 0
Season_ticket = 0

if height_as_int>= 120:
    print("You can ride the rollercoaster.")
    if age_as_int < 12:
        bill = 5
        print("Please pay $5, ")
    elif age_as_int <= 18:
        bill = 7
        print("Please pay $7. ")
    else:
        bill = 12 
        print("Please Pay $12. ")


    wants_a_photo = input("do you want a photo? Y or N . ")
    if wants_a_photo == "Y":
        bill += 3

    print(f"your final bill is {bill}")

    want_seasonal_ticket = input("Do you want a seasonalticket? Y or N. ")
    if want_seasonal_ticket == "Y":
        Season_ticket = 200

    print(f"The final charge on seasonal ticket is {Season_ticket}")


else:
    print("Sorry you cannot ride the rollercoster")
