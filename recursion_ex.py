import sys


def print_numbers(n: int) -> None:
    if n > 100: return None

    result: str = ""

    if n % 2 == 0:
        result += str(n)
        print(result)

    print_numbers(n + 1)


#print_numbers(0)


def reverse_text(text: str, n: int) -> None:
    if n > 100: return None

    result: str = ""

    if n >= 0:
        result += str(text[n])
        print(result)

        reverse_text(text, n - 1)


#reverse_text("boba", len("boba") - 1)


def check_the_biggest(array: list[int], n: int) -> None:
    if len(array) > 100:
        return None
    if n <= 0:
        print(array)
        return None

    if n < len(array) - 1 and array[n] > array[n + 1]:
        array[n], array[n + 1] = array[n + 1], array[n]

    check_the_biggest(array, n - 1)


_input = [int(x) for x in input("Enter a list of numbers: ").split()]
check_the_biggest(_input, len(_input) - 1)

