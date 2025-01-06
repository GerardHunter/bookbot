def main():
    path_to_file = "books/frankenstein.txt"
    text = get_text_from_book(path_to_file)
    num_words = get_number_of_words(text)
    characters = count_chars(text)
    num_chars = sorted_chars(characters)
    print_report(path_to_file, num_words, num_chars)

def get_text_from_book(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sorted_chars(chars_dict):
    def sort_on(dict):
        return dict["num"]
    chars_list = []
    for k, v in chars_dict.items():
        if k.isalpha():
            chars_list.append({"char": k, "num": v})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def print_report(path, n_words, n_chars):
    print(f"--- Begin report of {path} ---")
    print(f"{n_words} words found in the document\n")
    for item in n_chars:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print(f"--- End report ---")

main()
