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

    @pytest.mark.parametrize("number_to_check_if_prime",
                             [
                                 (11),
                                 (13),
                                 (17),
                                 (19)
                             ]
                             )

    def test_is_primer(self, number_to_check_if_prime):
        assert prime_number.is_prime(number_to_check_if_prime) == True

    @pytest.mark.parametrize("number_to_check_if_prime",
                             [
                                 (10),
                                 (12),
                                 (14),
                                 (15),
                                 (16),
                                 (18)
                             ]
                             )

    def test_is_not_prime(self, number_to_check_if_prime):
        assert prime_number.is_prime(number_to_check_if_prime) == False

    @pytest.mark.parametrize("number_to_check_if_prime, end_range",
                             [
                                 (10, 10)
                             ]
                             )

    def test_is_number_divisible_by_other_number(self, number_to_check_if_prime, end_range):
        assert prime_number.is_number_divisible_by_other_number(number_to_check_if_prime, end_range) == True