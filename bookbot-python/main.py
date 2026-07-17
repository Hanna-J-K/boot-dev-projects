from stats import get_number_of_words_in_book, get_number_of_unique_chars, chars_dict_to_sorted_list
from print_report import print_book_report 
import sys

def get_book_text(filepath:str) -> str:
    with open(filepath) as f:
        return f.read()
    return 1

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    book_filepath:str = sys.argv[1]
    book_contents:str = "" 

    book_contents = get_book_text(book_filepath)
    book_word_count = get_number_of_words_in_book(book_contents)
    book_unique_chars_number = get_number_of_unique_chars(book_contents)
    sorted_unique_chars = chars_dict_to_sorted_list(book_unique_chars_number)

    print(print_book_report(book_filepath, book_word_count, book_unique_chars_number, sorted_unique_chars))

    
    return 0
    
main()
