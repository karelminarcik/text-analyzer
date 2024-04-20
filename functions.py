def count_words_base_on_number_of_letters(text):
    # function to find the longest word
    def lenght_of_word(words):
        """find the longest word in the list of words"""
        longest_word = 0
        for word in words:
            if len(word) > longest_word:
                longest_word = len(word)
        return longest_word

    longest_word = (lenght_of_word(text))  
    
    # function to count amount of words according to number of charts in the word.

    def word_counter(word_list, lengths):
        # word_counts = {length: 0 for length in lengths}
        word_counts = {}
        for length in lengths:
            word_counts[length] = 0

        
        for word in word_list:
            for length in lengths:
                if len(word) == length:
                    word_counts[length] += 1
        
        return word_counts

    lengths_to_count = list(range(1, longest_word + 1))  # You can modify this list to count words of different lengths 

    counts = word_counter(text, lengths_to_count)
    return(counts)

# function for creating string containing number of "*" according the inserted number.
# def drawer(number):
#     """create string of '*' chart due to inserted number"""

#     number_of_stars = ""
#     for i in range(number):
#         number_of_stars += "*"
#     return number_of_stars
    

def drawer(num):
    stars = '*' * num
    space_padding = ' ' * (16 - len(stars))
    return f"{stars}{space_padding}|{num}"