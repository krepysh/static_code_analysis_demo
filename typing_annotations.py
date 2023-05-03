def format_name(first_name, last_name):
    """Return a full name: "John JAMESEON"."""

    a = first_name  # Add here a proper method to have the first name capitalized.
    b = last_name  # Add here a proper method to have the last name uppercased.
    return f"{a} {b}"


def format_name_annotated(first_name: str, last_name: str) -> str:
    """Return a full name: "John JAMESEON"."""

    a = first_name  # Add here a proper method to have the first name capitalized.
    b = last_name  # Add here a proper method to have the last name uppercased.
    return f"{a} {b}"


def process_character(s):
    ...


def add_words_to_collection(string_to_process, collection):
    for word in string_to_process:  # fix here:
        # add word to collection here (it is a list)
        pass
    return collection[0]


def add_words_to_collection_annotated(
    string_to_process: str, collection: list[str]
) -> list[str]:
    for word in string_to_process:  # fix here: add proper method to iterate over words
        # add word to collection here (it is a list)
        pass
    #  remove "type: ignore" from the next line after fixing the above
    return collection[0]  # type: ignore


def concatenate(s1, s2):
    # s1 and s2 are strings, and return value is a string as well
    # add typing annotations here: for s1, s2 and return value
    return s1 + s2


def is_even(x):
    # x is an integer, and return value is a boolean
    # add typing annotations here: for x and return value
    return x % 2 == 0


def greet(name, greeting=None):
    # add proper typing annotations here
    # use Optional for arguments which can be ommitted
    if greeting is None:
        greeting = "Hello"
    return f"{greeting}, {name}!"


def parse_number(num):
    # add proper typing annotations here
    # use Union for arguments which can be of different types
    try:
        result = int(num)
    except ValueError:
        try:
            result = float(num)
        except ValueError:
            result = None
    return result


def get_evens(numbers):
    # add proper typing annotations here
    # use List for lists with elements of the same type here
    # don't forget to import List from typing
    return [num for num in numbers if num % 2 == 0]


def count_words(words):
    """Return a dictionary with the count of each word."""
    # add proper typing annotations here
    # use Dict for dictionaries with elements of the same type here
    # don't forget to import Dict from typing
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def merge_dicts(fruits1, fruits2):
    # add proper typing annotations here
    result = fruits1.copy()
    for key, value in fruits2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


# Define two dictionaries
fruits1 = [{"apple": 3}, {"banana": 2}, {"orange": 1}]
fruits2 = {"banana": 1, "cherry": 4}

# Merge the dictionaries
merged_fruits = merge_dicts(fruits1, fruits2)


def main():
    print(format_name("john", "jameson"))
    print(format_name_annotated("john", "jameson"))
    print(add_words_to_collection("new words", ["initial"]))
    print(add_words_to_collection_annotated("new words", ["initial"]))


if __name__ == "__main__":
    main()
