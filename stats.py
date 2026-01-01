# Get a count of words used
def word_count(file_contents):
    word_count = 0
    book_lines = file_contents.split()
    # print(book_lines)
    for word in book_lines:
        word_count += 1
    return f"Found {word_count} total words"


# Get a count of individual characters
def character_count(file_contents):
    character_dict = {}
    corrected_content = file_contents.lower()
    for character in corrected_content:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict


# Sort characters based on number of times used
def sorted_text(char_dict):
    def sorted_num(character_dict):
        return character_dict["num"]

    sorted_list = []
    for character in char_dict:
        if character.isalpha():
            sorted_list.append({"char": character, "num": char_dict[character]})
        else:
            continue
    sorted_list.sort(reverse=True, key=sorted_num)

    return sorted_list
