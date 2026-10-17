# ft_package

A sample Python package created for Exercise 09.

## Installation

Build the package:

```bash
python -m build
```

Install the generated package:

```bash
python -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
# Output: 2

print(count_in_list(["toto", "tata", "toto"], "tutu"))
# Output: 0
```

## Function

`count_in_list(lst, item)` returns the number of
times `item` appears in `lst`.