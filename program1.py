text = input("Enter message: ")
shift = int(input("Enter shift: "))
choice = input("Enter e for encode or d for decode: ")

result = ""

for ch in text:
    if ch.isalpha():       # checking whether the element is an alphabet

        if choice == "e":
            s = shift
        else:
            s = -shift

        if ch.isupper():
            result += chr((ord(ch) - ord('A') + s) % 26 + ord('A'))
        else:
            result += chr((ord(ch) - ord('a') + s) % 26 + ord('a'))

    else:
        result += ch

print("Result:", result)