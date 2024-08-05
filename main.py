def main():
    book_path = "books/frankenstein.txt"
    whole_text = retrieve_book_text(book_path)
    word_count = get_word_count(whole_text)
    character_count = get_character_count(whole_text)
    book_report = make_book_report(book_path, character_count, word_count)

    print(book_report)

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
        if each_letter in character_dic:
            character_dic[each_letter] += 1
        else:
            character_dic[each_letter] = 1
    return character_dic

def make_book_report(book_path, char_dic, word_count):
    # Filter out non-alphabetical characters and convert to list of dictionaries
    list_of_characters = [{"char": key, "num": value} for key, value in char_dic.items() if key.isalpha()]
    
    # Sort the list by the number of occurrences, in descending order
    def sort_dic(entry):
        return entry["num"]
    
    list_of_characters.sort(reverse=True, key=sort_dic)
    
    # Construct the report string
    report = []
    report.append(f"--- Begin report of {book_path} ---")
    report.append(f"{word_count} words found in the document")
    
    for entry in list_of_characters:
        report.append(f"The '{entry['char']}' character was found {entry['num']} times")

    report.append("--- End report ---")
    
    return "\n".join(report)

main()
