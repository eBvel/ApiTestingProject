

class ValueValidation:
    @staticmethod
    def compare_values(value_name, current_value, expected_value):
        print(f"\n{value_name}\n{current_value=}\n{expected_value=}")
        assert current_value == expected_value, f"Incorrect value {current_value}"
        print(f"PASSED: Value '{current_value}' is correct!")