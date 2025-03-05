import random
print("Welcome to coin flip generator:")
random_flip = random.randint(0, 1)
if random_flip == 0:
    print("TAILS")
else:
    print("HEADS")
