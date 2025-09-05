from stats import get_num_chars, get_num_words

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    full_text = get_book_text("./books/frankenstein.txt")
    print(get_num_words(full_text) , "words found in the document")
    print(get_num_chars(full_text))

main()