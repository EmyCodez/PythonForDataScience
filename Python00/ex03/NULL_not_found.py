from typing import Any

def NULL_not_found(object: Any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese:", object, type(object))
    elif object is False:
        print("Fake:", object, type(object))
    elif object == 0 and type(object) is int:
        print("Zero:", object, type(object))
    elif object == "":
        print("Empty:", type(object))
    else:
        print("Type not Found")
        return 1
    return 0
