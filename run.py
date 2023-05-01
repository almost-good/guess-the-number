import random

def guess_the_number(scope):
    rand_num = random.randint(1, 50)

    guess = 0
    while guess != rand_num:
        guess = int(input("Guess the number: "))

        if guess < rand_num:
            print("Nooo, you guessed too low! Try again.")
        elif guess > rand_num:
            print("Nooo, you guessed too high. Try again.")
        
    print(f"Gratzzzz! Your guess was correct! The number indeed is: {rand_num}.")


guess_the_number(50)