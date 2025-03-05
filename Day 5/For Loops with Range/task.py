#total = 0
#for number in range(1, 101):
    #total = total + number
#print(total)

print("Welcome to the FizzBuzz Game")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
        print(number)
    elif number % 3 == 0:
        number = "Fizz"
        print(number)
    elif number % 5 == 0:
        number = "Buzz"
        print(number)
    else:
        print(number)


