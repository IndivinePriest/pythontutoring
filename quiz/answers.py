from .questions import Questions


class Answers(Questions):
    def example_question(self):
        """
        This answer has already been completed to show how quiz should be structured in this file
        """

        return "example answer"

    def example_question_add_2(self, number):
        """
        This answer has already been completed to show how quiz should be structured in this file
        """

        return number + 2

    def get_and_capitalise_second_letter_of_string(self, string):
        """
        This function should receive a string at least 2 characters long,
        and return the capital of the second character
        """

        return string[1].upper()

    def get_third_and_fourth_letters_of_string(self, string):
        """
        This function should receive a string at least 4 characters long,
        and return the third and fourth characters joined together
        """

        return string[2] + string[3]

    def add_new_string_to_string(self, string):
        """
        This function should receive a string, and
        return that string with the string 'new' joined to the end
        """

        return string+str("new")

    def multiply_numbers(self, number_1, number_2):
        """
        This function should receive two numbers, and return
        the multiple of those numbers
        """

        return number_1*number_2

    def string_length_in_a_sentence(self, string):
        """
        This function should receive a string, and print the sentence:
        "Your string is X characters long!", replacing X with the length of the string
        """

        string_length_in_sentence = len(string)
        return "Your string is " + str(string_length_in_sentence) + " characters long!"

    def get_minutes_from_datetime(self, datetime_value):
        """
        This function should receive a datetime, and return just the minutes
        """

        return datetime_value.minute

    def is_all_uppercase(self, string):
        """
        This function should receive a string of letters, and return a boolean (True or False) indicating
        if all the letters in the string are uppercase
        """
        return string == string.upper()

    def both_numbers_are_even(self, number_1, number_2):
        """
        This function should receive two numbers, and return a boolean indicating
        whether they are both even numbers (have a remainder of 0 when divided by 2)
        """

        return number_1%2 == 0 and number_2%2 == 0

    def only_one_number_is_even(self, number_1, number_2):
        """
        This function should receive two numbers, and return a boolean indicating
        whether only one of them is even
        """

        return (number_1%2 == 0) != (number_2%2 == 0)

    def make_function_that_returns_object_type(self):
        """
        This function should return another new function.
        The new function should have one parameter, which will receive an object,
        and should return the type of that object
        """
        def type_function(value):
            return type(value)
        return type_function

    def count_matching_list_items(self, target_list, value_to_match):
        """
        This function should receive a list and another variable, and return how many times the value
        of that variable can be found in the list.
        For example, if target_list is ["k", "e", "k", "w"] and value_to_match is "k", this function should return 2
        """

        return target_list.count(value_to_match)

    def are_all_keys_in_dict(self, list_of_keys, target_dict):
        """
        This function should receive a list and a dictionary. For each item in the list, the function should check if
        that item exists as a key in the dictionary. If all items in the list are also keys in the dictionary,
        the function should return True. However, if any item in the list is missing from the dictionary,
        the function should return False.

        The typical way to solve this question uses the `in` keyword. If you are not familiar with this keyword,
        return to this question once you have learned how to use it
        """
        for variable in list_of_keys:
            if not (variable in target_dict):
                return False

        return True


