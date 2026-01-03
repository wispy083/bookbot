from stats import get_book_words

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return book_contents

def main():
    print(get_book_text(book_path))
    print(f"Found {get_book_words(get_book_text(book_path))} total words")

#def get_book_words(get_book_text):
#    book_words = len(get_book_text.split())
#    return book_words

book_path = "./books/frankenstein.txt"

main()