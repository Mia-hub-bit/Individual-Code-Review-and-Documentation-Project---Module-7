def transform_integers(numbers):
    """
    Applies a transformation rule to a list of integers.

    - Even numbers are doubled ($n \times 2$).
    - Odd numbers are tripled ($n \times 3$).

    Args:
        numbers (list[int]): A list of integers to be processed.

    Returns:
        list[int]: A new list containing the transformed integers.
    """
    # Concise conditional transformation
    transformed_list = [
        num * 2  # Double if even.
        if num % 2 == 0
        else num * 3
        for num in numbers
    ]
    return transformed_list


def do_string_stuff(list_of_strings):
    x = ""
    for s in list_of_strings:
        if len(s) > 5:
            x += s.upper() + " "
        else:
            x += s.lower() + " "
    return x.strip()


def main():
    initial_numbers = [1, 2, 3, 4, 5, 6, 7]
    list2 = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_nums = transform_integers(initial_numbers)
    processed_strings = do_string_stuff(list2)

    print("Processed Numbers:", processed_nums)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()