print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age= int(input("What is your age?"))
    if age <= 12:
        print("The ticket price is 5 dollars")
    elif age > 18:
        print("The ticket price is 12 dollars")
    else:
        print("The ticket price is 7 dollars")
else:
    print("Sorry you have to grow taller before you can ride.")
