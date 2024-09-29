import pytest



class TestPrimeNumber:

    @pytest.mark.parametrize("add_text_input, add_expected_output",
                             [
                                 ("2+2", 4),
                                 ("4+1", 5),
                                 ("9+7", 16)
                             ]
                             )
    def test_addition(self, add_text_input, add_expected_output):
        pass
