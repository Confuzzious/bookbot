import sys

from stats import character_count, sorted_text, word_count


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    with open(book_path) as f:
        file_contents = f.read()
    word_c = word_count(file_contents)
    # print(word_c)

    character_c = character_count(file_contents)
    # print(character_c)

    sorted_chars_list = sorted_text(character_count(file_contents))
    # print(sorted_chars_list)

    print_report(book_path, word_c, sorted_chars_list)


def print_report(book_path, word_c, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_c} total words")
    print("--------- Character Count -------")
    for item in sorted_chars_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
