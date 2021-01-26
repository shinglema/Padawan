import requests
import random

hangman_word="     "
webster_word_link="https://www.merriam-webster.com/dictionary/"

word_length=int(input("How many letters do you want in this word:"))


word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
number_of_words =len(WORDS);

while len(hangman_word)<=word_length:
  
    random_number = random.randint(1,number_of_words)
    hangman_word=str(WORDS[random_number])
    #print(hangman_word)


hangman_word=hangman_word[2:]
hangman_word=hangman_word[:-1:]
guess_word=""


##Setting up the values to be one case since python is case sensitive
hangman_word=hangman_word.upper()
hangman_word_list=list(hangman_word)
letters_left_to_guess=-1;
number_of_guesses=0;

for x in range(len(hangman_word_list)):
    guess_word=guess_word + "_"


guess_word_list=list(guess_word)


print ('printing the leng of the variable: ' , len(guess_word))

while letters_left_to_guess!=0:

    enter_letter=str(input("What do you want to input:"))
    enter_letter=enter_letter.upper()
    number_of_guesses=number_of_guesses+1

    for x in range(len(hangman_word_list)):
       # print('Character Position:', x)
       # print (hangman_word_list[x])
        #print(guess_word_list[x])
        if hangman_word_list[x]==enter_letter:
            print ("You guessed letter: ",enter_letter, "and it exists a point ", x)
            guess_word_list[x]=str(enter_letter)

    letters_left_to_guess=0
    for x in range(len(guess_word_list)):
    
        if guess_word_list[x]=='_':
            letters_left_to_guess=letters_left_to_guess+1

    print('')
    print(list(guess_word_list))
    print("You have: ", letters_left_to_guess , " letters left to guess")

print("The Word Was: ", hangman_word)
webster_word_link=webster_word_link+hangman_word
print("Visit This Link for the definition of the word: " ,webster_word_link)
