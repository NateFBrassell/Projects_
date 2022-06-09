
secret_word = "frisby"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses): 
	if guess_count < guess_limit:
		guess = input("Enter guess: ")
		guess_count += 1
	else:
		out_of_guesses = True

if out_of_guesses:
	print("Out of Guesses, YOU LOSE!")
else:	   
	print("You win!")

	
#allows you to continually guess until you are right and you win!
#you can also set a limit of guesses user can have
