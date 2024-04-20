from text import TEXTS
from authorization import user_data
from art import logo
from functions import count_words_base_on_number_of_letters
from functions import drawer
import re

# Check authentication based on the provided username and password
def check_authorization(username, password):
    """check authentication based on the provided username and password"""
    if username in user_data and user_data[username] == password:
        return True
    else:
        return False

username = input("username: ")
password = input("password: ")

if not check_authorization(username, password):
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

        # number of word begining with uppercase
        upper_words = []
        def titlecase(words):
            """return titlecase words"""
            for word in words:
                if re.match('^[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]', word):
                    upper_words.append(word)
            print(f"There are {len(upper_words)} titlecase words.")
            return upper_words

        titlecase(separated_text)

        # number of word written only uppercase
        def only_upper(words):
            """return uppercase words"""
            uppercase_words = []
            for word in words:
                if re.match('^[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+$', word):
                    uppercase_words.append(word)
            return uppercase_words
        print(f"There are {len(only_upper(upper_words))} uppercase words.")

        # number of word begining with lowercase
        lowercase_words = []
        def lower(words):
            """return lowercase words"""
            for word in words:
                if re.match('^[a-záčďéěíňóřšťúůýž]', word):
                    lowercase_words.append(word)
            print(f"There are {len(lowercase_words)} lowercase words.")
            return lowercase_words

        lower(separated_text)

        # number of numbers in the control text
        number_words = []
        def number(words):
            for word in words:
                if re.match('^[0-9]+$', word):
                    number_words.append(word)
            print(f"There are {len(number_words)} numeric strings.")
            return number_words

        number(separated_text)
        
        # Sum of all numbers
        total_number = 0
        for num in number_words:
            num = int(num)
            total_number += num

        print(f"The sum of all the numbers {total_number}.")
        print("-------------------------------------------")

        word_list =(count_words_base_on_number_of_letters(separated_text))    

        print("       LEN|  OCCURENCES    |NR.")
        print("-------------------------------------------")

        # formatted_words = [drawer(word) for word in word_list]

        # Print the table using a loop
        # for i in range(len(word_list)):
        #     print(f"{i+1:2}| {formatted_words[i]:<20}| {word_list[i]}")

        print(f"""
         1|{drawer(word_list[1])}         
         2|{drawer(word_list[2])}         
         3|{drawer(word_list[3])}         
         4|{drawer(word_list[4])}         
         5|{drawer(word_list[5])}         
         6|{drawer(word_list[6])}         
         7|{drawer(word_list[7])}         
         8|{drawer(word_list[8])}         
         9|{drawer(word_list[9])}         
        10|{drawer(word_list[10])}        
        11|{drawer(word_list[11])}        
            """)

