NUMBER_BEGIN_TO_CHECK = 2

def is_divisible_by(number: int, by: int) -> bool:
    """
    Check if a number is divisible by another number.

    Parameter:
        number (int): The number to be divided.
        by (int): The number by which to divide.

    Returns:
        bool: True if `number` is divisible by `by`, False otherwise.
    """
    return number % by == 0


def is_prime(number: int) -> bool:
    """
    Determine if a number is prime.

    Parameter:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    return not is_number_divisible_by_other_number(number, number)


def is_number_divisible_by_itself_and_greater_than_one(number_to_check: int) -> bool:
    """
    Check if a number is greater than one and divisible by itself and 1.

    Parameter:
        number_to_check (int): The number to check.

    Returns:
        bool: True if the number is greater than 1 and divisible by both itself and 1.
    """
    return True if (number_to_check > 1
                    and is_divisible_by(number_to_check, 1)
                    and is_divisible_by(number_to_check, number_to_check)) \
        else False


def is_number_divisible_by_other_number(number_to_check: int, end_range: int) -> bool:
    """
    Check if a number is divisible by any number within a given range.

    Parameter:
        number_to_check (int): The number to check.
        end_range (int): The end of the range to check divisibility.

    Returns:
        bool: True if `number_to_check` is divisible by any number in the range,
              False otherwise.
    """
    return any(num is None or num > 0
               for num in range(NUMBER_BEGIN_TO_CHECK, end_range)
               if (is_divisible_by(number_to_check, num)
                   and is_number_divisible_by_itself_and_greater_than_one(
                number_to_check)))


def primes_in_range(start_range: int, end_range: int) -> None:
    """
    Print prime numbers in a given range.

    Parameter:
        start_range (int): The starting number of the range.
        end_range (int): The ending number of the range.

    Returns:
        None
    """
    for num_to_check in range(start_range, end_range):
        if is_prime(num_to_check):
            print(f"The number {num_to_check} is prime")


def input_start_and_end_number() -> tuple:
    """
    Prompt the user to input the start and end of the range.

    Returns:
        tuple: A tuple containing the start and end numbers as integers.
    """
    return int(input("Enter start range: ")), int(input("Enter end range: "))


def main() -> None:
    """
    Main function that gets user input and prints prime numbers in the specified range.

    Returns:
        None
    """
    start_range, end_range = input_start_and_end_number()

    primes_in_range(start_range, end_range)


if __name__ == "__main__":

    main()
