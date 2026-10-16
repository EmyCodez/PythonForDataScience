import sys


def filter_words(text: str, length: int) -> list:
    """Return words whose length is greater than the given length."""
    return [
        word for word in text.split()
        if (lambda w: len(w) > length)(word)
    ]


def main():
    """Validate arguments and display filtered words."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        text = sys.argv[1]
        assert all(
            char.isalnum() or char == " " for char in text
        ), "the arguments are bad"

        assert sys.argv[2].lstrip("-").isdigit(), \
            "the arguments are bad"

        length = int(sys.argv[2])

        print(filter_words(text, length))

    except (AssertionError, ValueError, TypeError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
