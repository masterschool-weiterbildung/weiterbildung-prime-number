NUMBER_BEGIN_TO_CHECK = 2

"""
    start_range = int(input("Enter start range: "))
    end_range = int(input("Enter end range: "))
"""


#Check if a number is prime

def is_number_prime(number_to_check):
    pass

def is_number_divisible_by_itself_and_greater_than_one(number_to_check):
    if number_to_check > 1 and number_to_check % 1 == 0 and number_to_check % number_to_check == 0:
        return True
    return False

def is_number_not_prime(end_range, number_to_check):
    for num in range(NUMBER_BEGIN_TO_CHECK, end_range):
        if number_to_check % num == 0 and is_number_divisible_by_itself_and_greater_than_one(number_to_check):
            return True
    return False

def main():
    for num in range(10,20):
        print(f" {is_number_not_prime(10, num)}  - {num}")


if __name__ == "__main__":
    main()