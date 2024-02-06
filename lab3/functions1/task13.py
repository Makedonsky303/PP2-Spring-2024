from random import randrange

def game():
    print("Hello! What is your name?")
    name = input()
    print("Well,", name, "I am thinking of a number between 1 and 20.")
    print("Take a guess")

    guess = int(input("\n"))

    random_num = randrange(1,21)
    num_of_guesses = 1

    while(guess!=random_num):
        if guess>random_num:
            print("Your guess is too big.")
        elif guess<random_num:
            print("Your guess is too low.")

        num_of_guesses+=1     

        guess = int(input("\n"))   

    print("Good job, {}! You guessed my number in {} guesses!".format(name,num_of_guesses))