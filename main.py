def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    generate_report(book_path, text)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    char_count = {}
    for ch in text.lower():
        char_count[ch] = char_count.get(ch, 0) + 1
    return char_count
def generate_report(book_path, text):
    char_count = get_char_count(text)
    sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True)) 
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_num_words(text)} words found in the document")
    for k,v in sorted_dict.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

main()
