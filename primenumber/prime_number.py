NUMBER_BEGIN_TO_CHECK = 2

def is_number_divisible_by_itself_and_greater_than_one(number_to_check):
    return True if (number_to_check > 1
                    and number_to_check % 1 == 0
                    and number_to_check % number_to_check == 0) else False

def is_prime_number(number_to_check, end_range):
    for num in range(NUMBER_BEGIN_TO_CHECK, end_range):
        if number_to_check % num == 0 and is_number_divisible_by_itself_and_greater_than_one(
                number_to_check):
            return False
    return True

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