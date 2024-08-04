def main():
    book_path = "books/frankenstein.txt"
    whole_text = retrieve_book_text(book_path)
    word_count = get_word_count(whole_text)
    

def retrieve_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    individual_words = text.split()
    return len(individual_words)

def get_character_count(text):
    lowercase_text = text.lower()
    character_dic = {}

    for each_letter in lowercase_text:



main()
