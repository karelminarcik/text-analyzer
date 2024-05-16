import re

# Check authentication based on the provided username and password
def check_authorization(username, password, auth_dict):
    """check authentication based on the provided username and password"""
    if username in auth_dict and auth_dict[username] == password:
        return True
    else:
        return False

# Number of words begining with title case     
def titlecase(words):
    """return list of titlecase words"""
    title_words = [word for word in words if word.istitle() ]
    print(f"There are {len(title_words)} titlecase words.")
    return title_words

# Number of words written only uppercase
def uppercase(words):
    """return list of uppercase words"""
    uppercase_words = [word for word in words if word.isupper()]
    print(f"There are {len(uppercase_words)} uppercase words.")        
    return uppercase_words

# Number of words begining with lowercase
def lower(words):
    # """return list of lowercase words"""
    lowercase_words = [word for word in words if word.islower()]
    print(f"There are {len(lowercase_words)} lowercase words.")
    return lowercase_words

# Number of numbers in the control text  
def number(words):
    """return list of all numbers"""
    number_words = [word for word in words if word.isnumeric()]
    return number_words

# Sum of all numbers
def sum_number(numbers):
    """count the sum of all numbers"""
    total_number = 0
    for num in number(numbers):
        num = int(num)
        total_number += num
    print(f"The sum of all the numbers {total_number}.")
    return total_number

# Function to find the longest word in the list of words 
def lenght_of_word(words):
        """find the longest word in the list of words"""
        longest_word = 0
        for word in words:
            if len(word) > longest_word:
                longest_word = len(word)
        return longest_word

def count_words_base_on_number_of_letters(text):
    """count amount of words according to number of charts in the word"""

    # Function to find the longest word
    lenght_of_word(text)
    longest_word = (lenght_of_word(text))  

    # Function to count occurrence of words according to amount of letters
    def word_counter(word_list, length_list):
        """count occurrence of words according to amount of letters"""
        word_counts = {length: 0 for length in length_list}     
        
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






