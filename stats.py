def get_book_words(book_text):
    book_words = len(book_text.split())
    return book_words

def get_book_chars(book_text):
    chars_count = {}
    lower_book_text = book_text.lower()
    for word in lower_book_text.split():
        for char in word:
            if char in chars_count:
                chars_count[char] += 1
            else:
                chars_count[char] = 1
    return  chars_count