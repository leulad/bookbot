def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_sort_chars(char_dict):
    def sort_on(items):
        return items["num"]
    sorted_char_dict = []
    for char in char_dict:
        sorted_char_dict.append({ "char": char , "num": char_dict[char] })
    sorted_char_dict.sort(reverse=True, key=sort_on)
    return sorted_char_dict

def print_sorted(sorted_char_dict):
    for dict in sorted_char_dict:
        if dict["char"].isalpha():
            print(dict["char"], ": ", dict["num"], sep="")