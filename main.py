from stats import (
    get_num_words,
    get_num_chars_dict,
    get_num_chars_list
)


def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()


def print_report(book_path: str, num_words: int, num_chars_list: list) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in num_chars_list:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars_dict = get_num_chars_dict(text)
    num_chars_list = get_num_chars_list(num_chars_dict)
    print_report(book_path, num_words, num_chars_list)


main()
