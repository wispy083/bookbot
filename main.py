from stats import get_book_words
from stats import get_book_chars

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return book_contents

def main():
# print the book text    
    print(get_book_text(book_path))
# print number of book words
    print(f"Found {get_book_words(get_book_text(book_path))} total words")
# print number of book characters
    print(get_book_chars(get_book_text(book_path)))

book_path = "./books/frankenstein.txt"

main()