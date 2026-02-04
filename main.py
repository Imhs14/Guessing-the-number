import random
num_to_guess = random.randint(1, 10)
while True:
    try:
        num = int(input("enter the number you guessed"))
        if num_to_guess > num:
            print("number entered is too low")
        elif num_to_guess < num:
            print("number entered is too high")
        else:
            print("Congratulations you've guessed the number")
            break
    except ValueError:
        print("Enter a valid number")