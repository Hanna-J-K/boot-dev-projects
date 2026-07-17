def get_number_of_words_in_book(book_content:str) -> int:
    word_counter:int = 0
    word_list:list[str] = book_content.split()
    word_counter = len(word_list)

    return word_counter

def get_number_of_unique_chars(book_content:str) -> dict[str, int]:
    char_counter_dictionary:dict[str, int] = {}
    book_content_normalized:list = list(book_content.lower())
    book_content_charset:set = set(book_content_normalized)

    for char in book_content_normalized:
        if char in book_content_charset:
            if char in char_counter_dictionary:
                char_counter_dictionary[char] += 1
            else:
                char_counter_dictionary[char] = 1

        

    return char_counter_dictionary


def sort_on(char_tuple:tuple[str, int]) -> int:
    return char_tuple[1]


def chars_dict_to_sorted_list(char_counter_dict:dict[str, int]) -> list[tuple[str, int]]:
    tuples_list:list = []
    
    for key in char_counter_dict:
        tuples_list.append((key, char_counter_dict[key]))

    sorted_chars = sorted(tuples_list, reverse=True, key=sort_on)

    return sorted_chars
