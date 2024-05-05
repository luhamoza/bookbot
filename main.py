def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)
    word_count = get_word_count(book_content)
    # print(book_content)
    print(f"{word_count} words found in the book")

def get_book_content(path):
    with open(path) as f:
        return f.read()

def get_word_count(str):
    return len(str.split())

main()