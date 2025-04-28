"""
License: Apache
Organization: UNIR

This script reads a list of words from a file, optionally removes duplicates, sorts them, 
and prints the final list.

Usage:
    python script.py <filename> <remove_duplicates>

Arguments:
    filename (str): Name of the file to read the words from.
    remove_duplicates (str): "yes" to remove duplicates, "no" to keep them.
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    """
    Sorts a list in ascending or descending order.

    Args:
        items (list): List of items to sort.
        ascending (bool, optional): Sort order. Defaults to True (ascending).

    Returns:
        list: Sorted list.

    Raises:
        RuntimeError: If the input is not a list.
    """
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    """
    Removes duplicate elements from a list.

    Args:
        items (list): List of items.

    Returns:
        list: List without duplicates.
    """
    return list(set(items))


if __name__ == "__main__":
    """
    Main program logic:
    - Reads the filename and duplicate removal option from command-line arguments.
    - Reads words from the specified file, or uses a default list if the file does not exist.
    - Optionally removes duplicates.
    - Sorts and prints the list.
    """
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES

    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("The file must be indicated as the first argument.")
        print("The second argument indicates whether duplicates should be removed.")
        sys.exit(1)

    print(f"Words will be read from the file {filename}")
    file_path = os.path.join(".", filename)

    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist.")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))