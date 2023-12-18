def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)

def print_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    chars_list = list(chars_dict)
    #chars_list.sort()
    for char in chars_list:
        if char.isalpha():
            print(f"The '{char}' character was found {chars_dict[char]} times")
    print("--- End report ---")

def get_num_words(text):
    return len(text.split())

#would it be better to individually change each character to lower?
def get_chars_dict(text):
    lower_text = text.lower()
    result = {}
    for char in lower_text:
        if not char in result:
            result[char] = 0
        result[char] += 1    
    return result


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()