# Prime Number Checker

## Overview
This Python script determines whether a given number is prime and finds prime numbers within a specified range. It includes functions to check divisibility and identify prime numbers efficiently.

## Features
- Checks if a number is prime.
- Finds prime numbers within a user-specified range.
- Uses helper functions for modularity and readability.
- Takes user input for range selection.

## Constants
```python
NUMBER_BEGIN_TO_CHECK = 2
```
Defines the starting point for checking divisibility.

## Functions
### `is_divisible_by(number: int, by: int) -> bool`
Checks if `number` is divisible by `by`.

### `is_prime(number: int) -> bool`
Determines if a number is prime.

### `is_number_divisible_by_itself_and_greater_than_one(number_to_check: int) -> bool`
Checks if a number is greater than one and divisible only by itself and 1.

### `is_number_divisible_by_other_number(number_to_check: int, end_range: int) -> bool`
Determines if `number_to_check` is divisible by any number in a given range.

### `primes_in_range(start_range: int, end_range: int) -> None`
Prints prime numbers within a specified range.

### `input_start_and_end_number() -> tuple`
Prompts the user to input the start and end range.

### `main() -> None`
Runs the script by gathering user input and printing prime numbers.

## Usage
Run the script in a Python environment:
```sh
python prime_checker.py
```
The script will prompt for input:
```sh
Enter start range: 10
Enter end range: 50
The number 11 is prime
The number 13 is prime
...
```
