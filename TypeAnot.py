from typing import Any, List, Dict, Union, Optional


def format_name(first_name: str, last_name: str) -> str:
    """Return a full name: "John JAMESEON"."""
    a = first_name.capitalize()
    b = last_name.upper()
    return f"{a} {b}"


def format_name_annotated(first_name: str, last_name: str) -> str:
    """Return a full name: "John JAMESEON"."""
    a = first_name.capitalize()
    b = last_name.upper()
    return f"{a} {b}"


def process_character(s: str) -> None:
    pass


def add_words_to_collection(string_to_process: str, collection: List[str]) -> str:
    for word in string_to_process.split():
        collection.append(word)
    return collection[0]


def add_words_to_collection_annotated(string_to_process: str, collection: List[str]) -> str:
    for word in string_to_process.split():
        collection.append(word)
    return collection[0]


def concatenate(s1: str, s2: str) -> str:
    return s1 + s2


def is_even(x: int) -> bool:
    return x % 2 == 0


def greet(name: str, greeting: Optional[str] = "Hello") -> str:
    return f"{greeting}, {name}!"


def parse_number(num: Union[int, float, str]) -> Union[int, float, None]:
    try:
        result = int(num)
    except ValueError:
        try:
            result = float(num)
        except ValueError:
            result = None
    return result


def get_evens(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 == 0]


def count_words(words: List[str]) -> Dict[str, int]:
    word_counts: Dict[str, int] = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def merge_dicts(fruits1: List[Dict[str, int]], fruits2: Dict[str, int]) -> Dict[str, int]:
    result = {k: v for d in fruits1 for k, v in d.items()}
    for key, value in fruits2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


def main() -> None:
    print(format_name("john", "jameson"))
    print(format_name_annotated("john", "jameson"))
    print(add_words_to_collection("new words", ["initial"]))
    print(add_words_to_collection_annotated("new words", ["initial"]))


if __name__ == "__main__":
    main()
