def clean_text(text):
    return "".join(text.lower().split())


def are_anagrams(text1, text2):
    return sorted(clean_text(text1)) == sorted(clean_text(text2))


def character_frequency(text):
    frequency = {}
    for char in clean_text(text):
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def find_anagrams(word, words):
    key = tuple(sorted(clean_text(word)))
    return [
        item for item in words
        if tuple(sorted(clean_text(item))) == key
    ]


def main():
    first = input("Enter first word or phrase: ")
    second = input("Enter second word or phrase: ")

    if are_anagrams(first, second):
        print("The texts are anagrams.")
    else:
        print("The texts are not anagrams.")

    print("\nCharacter Frequency:", character_frequency(first))

    words = ["listen", "silent", "enlist", "hello", "inlets", "world"]
    matches = find_anagrams(first, words)

    print("Matching Words:", matches)


if __name__ == "__main__":
    main()
