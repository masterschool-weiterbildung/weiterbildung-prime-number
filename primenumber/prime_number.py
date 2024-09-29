NUMBER_BEGIN_TO_CHECK = 2

def is_number_divisible_by_itself_and_greater_than_one(number_to_check):
    """
    Check if a given number is greater than one and divisible by itself.

    A number is considered valid if it meets the following criteria:
    - It is greater than one.
    - It is an integer (divisible by 1).
    - It is divisible by itself.

    Parameter:
        number_to_check (int or float): The number to check for the conditions.

    Returns:
        bool: True if the number is greater than one and divisible by itself,
              False otherwise.
    """
    return True if (number_to_check > 1
                    and number_to_check % 1 == 0
                    and number_to_check % number_to_check == 0) \
                else False

def is_number_divisible_by_other_number(number_to_check, end_range):
    """
    Check if a given number is divisible by any number in a specified range.

    This function evaluates whether `number_to_check` is divisible by any integer
    within the range starting from `NUMBER_BEGIN_TO_CHECK` to `end_range` (exclusive).
    It also checks if `number_to_check` is greater than one and divisible by itself.

    Args:
        number_to_check (int): The number to check for divisibility.
        end_range (int): The exclusive upper limit of the range to check against.

    Returns:
        bool: True if `number_to_check` is divisible by any number in the range
              and meets the self-divisibility condition, False otherwise.

    Note:
        NUMBER_BEGIN_TO_CHECK is 2 declared globally.
    """
    return any(num is None or num > 0
               for num in range(NUMBER_BEGIN_TO_CHECK, end_range)
               if (number_to_check % num == 0
                   and is_number_divisible_by_itself_and_greater_than_one(
            number_to_check)))

def is_prime_number(number_to_check, end_range):
    """
    Determine if a given number is prime.

    A prime number is defined as a natural number greater than 1 that cannot
    be formed by multiplying two smaller natural numbers. This function checks
    whether `number_to_check` is not divisible by any number in the range from
    `NUMBER_BEGIN_TO_CHECK` to `end_range`.

    Parameter:
        number_to_check (int): The number to check for primality.
        end_range (int): The exclusive upper limit of the range to check against.

    Returns:
        bool: True if `number_to_check` is prime (not divisible by any number
              in the specified range), False otherwise.

    Note:
        NUMBER_BEGIN_TO_CHECK is 2 declared globally.
    """
    return not is_number_divisible_by_other_number(number_to_check, end_range)

def input_start_and_end_number():
    return int(input("Enter start range: ")), int(input("Enter end range: "))

def display_the_prime_numbers(start_range, end_range):
    for num_to_check in range(start_range, end_range):
        if is_prime_number(num_to_check, start_range):
            print(f"The number {num_to_check} is prime")

def main():
    start_range, end_range = input_start_and_end_number()

    display_the_prime_numbers(start_range, end_range)

if __name__ == "__main__":
    main()