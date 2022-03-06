# This includes the concept of while loop, control flow and strings

secret_word = "roy"
guess = ""  # to enter the answer in the field.
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess!= secret_word and out_of_guesses is False:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count = guess_count + 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry, you have lost the guessing game.")
else:
    print("YOU WIN THE GUESSING GAME.")
