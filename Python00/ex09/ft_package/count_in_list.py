def count_in_list(lst, item):
    """Count how many times an item appears in a list."""
    return lst.count(item)


def main():
    """Run basic tests for count_in_list."""
    try:
        print(count_in_list(["toto", "tata", "toto"], "toto"))
        print(count_in_list(["toto", "tata", "toto"], "tutu"))
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
