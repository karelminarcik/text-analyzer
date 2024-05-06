from text import TEXTS
from authorization import user_data
from art import logo
from functions import *

username = input("username: ")
password = input("password: ")

if not check_authorization(username, password, user_data):
    print("Unregistered user, terminating the program..")
else:

    print(logo)
    print("-------------------------------------------")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("-------------------------------------------")

    # Chose a text to be analysis
    choosen_text = (input("Enter a number btw. 1 and 3 to select: "))
    print("-------------------------------------------")
    if choosen_text not in ["1", "2", "3"]:
        print("You do not insert any of provided options, terminating the program..")
    else:
        text = TEXTS[int(choosen_text) - 1]

        # Separate each word in the text to the particular string
        separated_text = text.split()

        # number of word in the text
        num_of_words = len(separated_text)
        print(f"There are {num_of_words} words in the selected text.")
        titlecase(separated_text)
        uppercase(separated_text)
        lower(separated_text)
        number_amount = number(separated_text)
        print(f"There are {len(number_amount)} numeric strings.")

        sum_number(number(separated_text))
        

        print("-------------------------------------------")

        word_list =(count_words_base_on_number_of_letters(separated_text))    

        print("     LEN|  OCCURENCES    |NR.")
        print("-------------------------------------------")


        for i in range(1, (lenght_of_word(separated_text) + 1)):
            if i < 10:
                print(f"       {i}|{drawer(word_list[i], separated_text)}") 
            else:
                print(f"      {i}|{drawer(word_list[i], separated_text)}") 

        

