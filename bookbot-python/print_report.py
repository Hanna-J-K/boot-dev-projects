def print_book_report(book_filepath:str, book_word_count:int, unique_chars_count:dict[str, int], chars_count_sorted:list[tuple[str,int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for element in chars_count_sorted:
        if element[0].isalpha():
            print(f"{element[0]}: {element[1]}")
    print("============= END ===============")
