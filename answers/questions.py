from abc import ABC


class Questions(ABC):
    """
    These questions are structured around the Python 2 course on codecademy
    """

    # Example questions

    def example_question(self):
        """
        This function should return the string "example answer"
        """

        return NotImplemented

    def example_question_add_2(self, number):
        """
        This function should receive a number, and return the provided number with 2 added to it
        """

    # 1. Python Syntax

    def add_new_string_to_string(self, string):
        """
        This function should receive a string, and
        return that string with the string 'new' joined to the end
        """

        return NotImplemented

    def multiply_numbers(self, number_1, number_2):
        """
        This function should receive two numbers, and return
        the multiple of those numbers
        """

        return NotImplemented

    # 2.1. Strings and Console Output

    def get_and_capitalise_second_letter_of_string(self, string):
        """
        This function should receive a string at least 2 characters long,
        and return the capital of the second character
        """

        return NotImplemented

    def get_third_and_fourth_letters_of_string(self, string):
        """
        This function should receive a string at least 4 characters long,
        and return the third and fourth characters joined together
        """

        return NotImplemented

    def string_length_in_a_sentence(self, string):
        """
        This function should receive a string, and print the sentence:
        "Your string is X characters long!", replacing X with the length of the string
        """

        return NotImplemented

    # 2.2. Date and Time

    def get_minutes_from_datetime(self, datetime_value):
        """
        This function should receive a datetime, and return just the minutes
        """

        return NotImplemented
