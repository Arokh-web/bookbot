def get_char_count(text):
    words = text.split()

    return len(words)


def get_character_Count(text):
    charCount = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
    return charCount

def sorted_list(charCount):
    return sorted(charCount.items(), key=lambda item: item[1], reverse=True)