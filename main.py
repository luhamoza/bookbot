def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)
    word_count = get_word_count(book_content)
    letter_count_dict = letter_dict(book_content)
    print(f"{word_count} words found in the book")
    print(letter_count_dict)


def get_book_content(path):
    with open(path) as f:
        return f.read()

def get_word_count(str):
    return len(str.split())

def get_letter_count(letter, alphabet):
    return letter.lower().count(alphabet)

def letter_dict(text):
    letter_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    for (key, value) in letter_dict.items():
        if key in letter_dict:
            count = get_letter_count(text, key)
            letter_dict[key] = count
    return letter_dict


main()