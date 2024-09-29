import pytest

from primenumber import prime_number


class TestPrimeNumber:

    @pytest.mark.parametrize("number_to_check",
                             [
                                 (11)
                             ]
                             )

    def test_is_number_divisible_by_itself_and_greater_than_one(self, number_to_check):
        assert prime_number.is_number_divisible_by_itself_and_greater_than_one(number_to_check) == True

    @pytest.mark.parametrize("number_to_check_if_prime, end_range",
                             [
                                 (11, 10),
                                 (13, 10),
                                 (17, 10),
                                 (19, 10)
                             ]
                             )

    def test_is_prime_number(self, number_to_check_if_prime, end_range):
        assert prime_number.is_prime_number(number_to_check_if_prime, end_range) == True

    @pytest.mark.parametrize("number_to_check_if_prime, end_range",
                             [
                                 (10, 10),
                                 (12, 10),
                                 (14, 10),
                                 (15, 10),
                                 (16, 10),
                                 (18, 10)
                             ]
                             )

    def test_is_not_prime_number(self, number_to_check_if_prime, end_range):
        assert prime_number.is_prime_number(number_to_check_if_prime, end_range) == False
