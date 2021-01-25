guess_word=""
hangman_word="AlphaOmega"
##Setting up the values to be one case since python is case sensitive
hangman_word=hangman_word.upper()
hangman_word_list=list(hangman_word)
letters_left_to_guess=-1;
number_of_guesses=0;

print (len(hangman_word))


#for i in range(len(dog)):

for x in range(len(hangman_word_list)):
    guess_word=guess_word + "_"



print ('Printing the 0 value: ' ,hangman_word_list[0])





print (len(guess_word))
print (guess_word)
guess_word_list=list(guess_word)


print ('printing the leng of the variable: ' , len(guess_word))








while letters_left_to_guess!=0:

    enter_letter=str(input("What do you want to input"))
    enter_letter=enter_letter.upper()
    number_of_guesses=number_of_guesses+1






    for x in range(len(hangman_word_list)):
        print('Character Position:', x)
        print (hangman_word_list[x])
        if hangman_word_list[x]==enter_letter:
            print ("You guessed letter: ",enter_letter, "and it exists a point ", x)
            guess_word_list[x]=str(enter_letter)

    letters_left_to_guess=0
    for x in range(len(guess_word_list)):
    
        if guess_word_list[x]=='_':
            letters_left_to_guess=letters_left_to_guess+1

#hangman_word_list[0]='X'

    print(hangman_word_list)
    print(guess_word)
    print(list(guess_word_list))
    print("You have: ", letters_left_to_guess , " letters left to guess")


