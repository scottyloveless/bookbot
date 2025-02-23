from stats import get_word_count, retrieve_book_text, get_character_count, make_book_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    whole_text = retrieve_book_text(book_path)
    word_count = get_word_count(whole_text)
    character_count = get_character_count(whole_text)
    book_report = make_book_report(book_path, character_count, word_count)

    print(book_report)



main()
