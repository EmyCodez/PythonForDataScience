import sys
import string


def count_characters(text):
    """Count uppercase, lowercase, punctuation, spaces, and digits."""
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punctuation += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1

    return upper, lower, punctuation, spaces, digits


def display_counts(text):
    """Display the total characters and their categories."""
    upper, lower, punctuation, spaces, digits = (
        count_characters(text)
    )

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Read the input text and display character counts."""
    try:
        if len(sys.argv) > 2:
            raise AssertionError(
                "more than one argument is provided"
            )

        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("What is the text to count?")
            text = sys.stdin.read()

        display_counts(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except EOFError:
        pass


if __name__ == "__main__":
    main()
