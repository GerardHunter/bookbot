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

