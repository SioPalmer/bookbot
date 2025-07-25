from stats import character_count, word_count, prepare_dic, sort_characters
import sys

if len(sys.argv) <2:
    print("Bookbot Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_text(sys.argv[1])
    charas = character_count(text)
    prepare_chars = prepare_dic(charas)
    prepare_chars.sort(key=sort_characters, reverse=True)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", sys.argv[1])
    print("----------- Word Count ----------")
    print("Found", word_count(text), "total words")
    print("--------- Character Count -------")
    for char_dict in prepare_chars:
        if char_dict["char"].isalpha():
            print(f'{char_dict["char"]}: {char_dict["num"]}')
    print("============= END ===============")

main()