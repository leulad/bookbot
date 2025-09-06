from stats import get_num_chars, get_num_words, get_sort_chars, print_sorted
import sys 

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    if (len(sys.argv) == 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    full_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at ", sys.argv[1], "...", sep="")
    print("----------- Word Count ----------")
    print("Found", get_num_words(full_text), "total words")
    print("--------- Character Count -------")
    print_sorted(get_sort_chars(get_num_chars(full_text)))
    print("============= END ===============")
main()