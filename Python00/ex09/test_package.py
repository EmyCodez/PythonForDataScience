"""Test the public API of ft_package."""

from ft_package import count_in_list


def main():
    """Run tests for count_in_list."""
    try:
        assert count_in_list(
            ["toto", "tata", "toto"], "toto"
        ) == 2
        assert count_in_list(
            ["toto", "tata", "toto"], "tutu"
        ) == 0
        assert count_in_list([], "toto") == 0
        assert count_in_list(["a", "a", "a"], "a") == 3
        print("All tests passed.")
    except Exception as error:
        print(f"Test failed: {error}")


if __name__ == "__main__":
    main()
