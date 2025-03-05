print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Your bill without picture is $5.")
    elif age <= 18:
        bill = 7
        print("Your bill without picture is $7.")
    else:
        bill = 12
        print("Your bill without picture is $12.")

    wants_picture = input("Type Y if you need a picture and Type N if you don't need a picture")
    if wants_picture == "Y":
        bill = bill + 3
        print(f"The total bill is = {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
