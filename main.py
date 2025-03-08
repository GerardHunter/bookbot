import sys
from stats import (get_number_of_words, count_chars, sorted_chars)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_text_from_book(path_to_file)
    num_words = get_number_of_words(text)
    characters = count_chars(text)
    num_chars = sorted_chars(characters)
    print_report(path_to_file, num_words, num_chars)

def get_text_from_book(path):
    with open(path) as f:
        return f.read()

def print_report(path, n_words, n_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {n_words} total words")
    print("--------- Character Count -------")
    for item in n_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
