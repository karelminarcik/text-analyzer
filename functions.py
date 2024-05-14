import re

# Check authentication based on the provided username and password
def check_authorization(username, password, auth_dict):
    """check authentication based on the provided username and password"""
    if username in auth_dict and auth_dict[username] == password:
        return True
    else:
        return False

# number of word begining with title case     
def titlecase(words):
    """return list of titlecase words"""
    title_words = []            
    for word in words:
        if word.istitle():
            title_words.append(word)
    print(f"There are {len(title_words)} titlecase words.")
    return title_words

# number of word written only uppercase
def uppercase(words):
    """return list of uppercase words"""
    uppercase_words = []
    for word in words:
        if word.isupper():
            uppercase_words.append(word)
    print(f"There are {len(uppercase_words)} uppercase words.")        
    return uppercase_words

# number of word begining with lowercase
def lower(words):
    """return list of lowercase words"""
    lowercase_words = []
    for word in words:
        if word.islower():
            lowercase_words.append(word)
    print(f"There are {len(lowercase_words)} lowercase words.")
    return lowercase_words

# number of numbers in the control text  
def number(words):
    """return list of all numbers"""
    number_words = []
    for word in words:
        if word.isnumeric():
            number_words.append(word)
    return number_words

# Sum of all numbers
def sum_number(numbers):
    total_number = 0
    for num in number(numbers):
        num = int(num)
        total_number += num
    print(f"The sum of all the numbers {total_number}.")
    return total_number

# find the longest word in the list of words 
def lenght_of_word(words):
        """find the longest word in the list of words"""
        longest_word = 0
        for word in words:
            if len(word) > longest_word:
                longest_word = len(word)
        return longest_word

def count_words_base_on_number_of_letters(text):
    # function to find the longest word
    lenght_of_word(text)
    longest_word = (lenght_of_word(text))  
    
    # function to count amount of words according to number of charts in the word.

    def word_counter(word_list, length_list):
        """count occurrence of words according to amount of letters"""
        # word_counts = {length: 0 for length in lengths}     ****shorter record****
        word_counts = {}
        for length in length_list:
            word_counts[length] = 0

        
        for word in word_list:
            for length in length_list:
                if len(word) == length:
                    word_counts[length] += 1
        

        return word_counts

    lengths_to_count = list(range(1, longest_word + 1)) 

    counts = word_counter(text, lengths_to_count)
    return(counts)

# function for creating string containing number of "*" according the inserted number.   
def drawer(num, most_often_count_of_letter):
    stars = '*' * num
    space_padding = ' ' * ((most_often_count_of_letter - len(stars)) +2)
    return f"{stars}{space_padding}|{num}"






