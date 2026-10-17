"""Tests for the ft_filter function."""

from ft_filter import ft_filter


def test_basic_filter():
    """Test filtering even numbers."""
    expected = [0, 2, 4, 6, 8]
    result = list(ft_filter(lambda x: x % 2 == 0, range(10)))
    assert result == expected
    print("Basic filter: OK")


def test_compare_builtin():
    """Compare ft_filter with the built-in filter."""
    cases = [
        (lambda x: x > 3, [1, 2, 3, 4, 5, 6]),
        (lambda x: x % 2 == 0, range(10)),
        (lambda x: len(x) > 3, ["cat", "tiger", "dog", "lion"]),
        (lambda x: x < 0, [1, 2, 3]),
    ]

    for function, iterable in cases:
        expected = list(filter(function, iterable))
        result = list(ft_filter(function, iterable))
        assert result == expected
    print("Comparison with built-in filter: OK")


def test_none_function():
    """Test filtering truthy values when function is None."""
    values = [0, 1, "", "hello", None, False, True, [], [1]]
    expected = list(filter(None, values))
    result = list(ft_filter(None, values))
    assert result == expected
    print("None function: OK")


def test_empty_iterable():
    """Test filtering an empty iterable."""
    assert list(ft_filter(lambda x: x, [])) == []
    print("Empty iterable: OK")


def test_generator():
    """Test ft_filter with a generator as input."""
    def numbers():
        """Yield numbers from zero to four."""
        yield from range(5)

    expected = [0, 2, 4]
    result = list(ft_filter(lambda x: x % 2 == 0, numbers()))
    assert result == expected
    print("Generator input: OK")


def test_lazy_evaluation():
    """Check that the predicate is called only during iteration."""
    calls = []

    def predicate(value):
        """Record calls and return whether the value is even."""
        calls.append(value)
        return value % 2 == 0

    result = ft_filter(predicate, [1, 2, 3])

    assert calls == []
    assert next(result) == 2
    assert calls == [1, 2]
    assert list(result) == []
    assert calls == [1, 2, 3]
    print("Lazy evaluation: OK")


def test_docstring():
    """Check that the docstring matches the built-in filter."""
    assert ft_filter.__doc__ == filter.__doc__
    print("Docstring: OK")


def main():
    """Run all tests and report failures."""
    tests = [
        test_basic_filter,
        test_compare_builtin,
        test_none_function,
        test_empty_iterable,
        test_generator,
        test_lazy_evaluation,
        test_docstring,
    ]

    failures = 0
    for test in tests:
        try:
            test()
        except Exception as error:
            failures += 1
            print(f"{test.__name__}: FAILED ({error})")

    if failures:
        print(f"\n{failures} test(s) failed.")
    else:
        print("\nAll tests passed.")


if __name__ == "__main__":
    main()
