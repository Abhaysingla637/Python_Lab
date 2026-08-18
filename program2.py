import string

def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra whitespace
    text = " ".join(text.split())

    return text


def word_frequency(text):
    words = text.split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def find_palindromes(words):
    palindromes = []

    for word in words:
        if len(word) > 1 and word == word[::-1]:
            if word not in palindromes:
                palindromes.append(word)

    return palindromes


def analyze_text(text):
    # Clean the text
    cleaned = clean_text(text)

    # Split into words
    words = cleaned.split()

    # Total word count
    total_words = len(words)

    # Frequency table
    frequency = word_frequency(cleaned)

    # Find palindromes
    palindromes = find_palindromes(words)

    # Generate report
    print("\n----- TEXT ANALYSIS REPORT -----")
    print("Total words:", total_words)

    print("\nWord Frequency:")
    for word, count in frequency.items():
        print(word, ":", count)

    print("\nPalindrome Words:")
    if palindromes:
        print(", ".join(palindromes))
    else:
        print("No palindromes found.")

    print("\nCleaned Text:")
    print(cleaned)


# Input text
text = input("Enter your text:\n")

# Analyze the text
analyze_text(text)