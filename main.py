from letter_dictionary import letter_dict 

def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)
    word_count = get_word_count(book_content)
    print_report(book_path, book_content, word_count)

def get_book_content(path):
    with open(path) as f:
        return f.read()

def get_word_count(str):
    return len(str.split())

def get_letter_count(letter, alphabet):
    return letter.lower().count(alphabet)

def populate_letter_dict(text):
    for (key, value) in letter_dict.items():
        if key in letter_dict:
            count = get_letter_count(text, key)
            letter_dict[key] = count
    return letter_dict

def print_report(path, content, count):
    header = f"--- Begin report of {path} ---"
    footer = "--- End report ---"
    populated_letter_dict = populate_letter_dict(content)

    print(header)
    print(f"{count} words found in the book")
    print()
    for (key, value) in populated_letter_dict.items():
        print(f"The '{key}' character was found {value} times")
    print(footer)

main()