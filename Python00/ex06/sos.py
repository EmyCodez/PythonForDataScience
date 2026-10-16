import sys


def build_morse_dictionary():
    """Return a dictionary mapping supported characters to Morse code."""
    return {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ",
        "D": "-.. ", "E": ". ", "F": "..-. ",
        "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ",
        "P": ".--. ", "Q": "--.- ", "R": ".-. ",
        "S": "... ", "T": "- ", "U": "..- ",
        "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ",
        "3": "...-- ", "4": "....- ", "5": "..... ",
        "6": "-.... ", "7": "--... ", "8": "---.. ",
        "9": "----. "
    }


def encode_morse(text, morse):
    """Encode a string into Morse code."""
    result = ""

    for char in text.upper():
        if char not in morse:
            raise AssertionError("the arguments are bad")
        result += morse[char]

    return result.rstrip()


def main():
    """Validate arguments and print the Morse code translation."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        morse = build_morse_dictionary()
        print(encode_morse(sys.argv[1], morse))

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
