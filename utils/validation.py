import json
from requests import  Response


class ValueValidation:
    @staticmethod
    def compare_values(value_name, current_value, expected_value):
        print(f"\n{value_name}\n{current_value=}\n{expected_value=}")
        assert current_value == expected_value, (f"Incorrect value "
                                                 f"{current_value}")
        print(f"PASSED: Value '{current_value}' is correct!")

    @staticmethod
    def compare_response_token(response: Response, expected_token):
        response_token = json.loads(response.text)
        assert list(response_token) == expected_token
        print(f"PASSED: Token is correct! All fields are included.")

    @staticmethod
    def search_word_in_text(value_name, text, word):
        print(f"\n{value_name}\ntext: {text}\nword: {word}")
        assert word in text, f"The text doesn't contains the word - '{word}'!"
        print(f"PASSED: The word '{word}' is present in the text!")