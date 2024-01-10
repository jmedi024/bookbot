def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

    num_of_words = count_words(text)
    char_count = char_counts(text)
    print(f"There are {num_of_words} words in this text")
    
    char_list = []
    
    for char in char_count:
        if char.isalpha():
            char_list.append(char)

    char_list.sort()
    for char in char_list:
        print(f"The {char} character was found {char_count[char]} times in the text")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def char_counts(text):
    lowercase_text = text.lower()
    char_count = {}

    for char in lowercase_text:
        if not char in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count

if __name__ == '__main__':
    main()