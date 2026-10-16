from ft_package import count_in_list


def main():
    """Test the count_in_list function."""
    try:
        print(count_in_list(["toto", "tata", "toto"], "toto"))
        print(count_in_list(["toto", "tata", "toto"], "tutu"))
    except (TypeError, AttributeError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
