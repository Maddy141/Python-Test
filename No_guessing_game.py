import random

print("Hi welcome to the game, This is a number guessing game.\nYou got  chances to guess the number between 1 and 50. Let's start the game")

number_to_guess = random.randrange(1000)

chances = 10

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input('Please Enter your Guess : '))

    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')

    elif my_guess > number_to_guess:
        print('Your guess is higher ')

    elif my_guess < number_to_guess:
        print('Your guess is lesser')
