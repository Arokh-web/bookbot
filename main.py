from stats import get_char_count, get_character_Count, sorted_list
import sys


def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print('Welcome to BOOKBOT!')
    print('I can analyze the text of a book for you.')
    print('Usage: python3 main.py <path_to_book>')
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    length = get_char_count(text)
    charCount = get_character_Count(text)
    charCountSorted = sorted_list(charCount)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {length} total words')
    print('--------- Character Count -------')
    for char in charCountSorted:
        print(f'{char[0]}: {char[1]}')
    print('============= END ===============')


main()
