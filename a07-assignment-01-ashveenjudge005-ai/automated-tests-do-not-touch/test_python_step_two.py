import unittest
from io import StringIO
import sys
from unittest import mock
import runpy

CORRECT_VALUE = 1
INCORRECT_VALUE = 2
BET_AMOUNT = 90

ORIGINAL_INPUTS_FROM_PART_ONE = ["yes", BET_AMOUNT, CORRECT_VALUE]

def run_file_get_output_success():
    # Redirect stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate user input and run the file
    with mock.patch('builtins.input', side_effect=[
            *ORIGINAL_INPUTS_FROM_PART_ONE,
            "yes",
            CORRECT_VALUE
        ]):
        # patch random
        with mock.patch('random.randint', return_value=CORRECT_VALUE):
            runpy.run_path('dice_game_double_play.py')
    # Get the value of the captured output
    output = captured_output.getvalue().strip().split("\n")
    # Reset stdout to its original value
    sys.stdout = sys.__stdout__
    return output

def run_file_get_output_unsuccessful():
    # Redirect stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate user input and run the file
    with mock.patch('builtins.input', side_effect=[
            *ORIGINAL_INPUTS_FROM_PART_ONE,
            "yes",
            INCORRECT_VALUE
        ]):
        # patch random
        with mock.patch('random.randint', return_value=CORRECT_VALUE):
            runpy.run_path('dice_game_double_play.py')
    # Get the value of the captured output
    output = captured_output.getvalue().strip().split("\n")
    # Reset stdout to its original value
    sys.stdout = sys.__stdout__
    return output

# successful run.
def test_successful_run():
    # Simulate user input
    OUTPUT_INDEX = 2

    output = run_file_get_output_success()
    last_string_output = output[OUTPUT_INDEX]

    EXPECTED_SIMPLE_STRING = F"Wow! you won all {BET_AMOUNT*2 + BET_AMOUNT*4 } in total"


    if (EXPECTED_SIMPLE_STRING.lower() in last_string_output.lower()):

        return True
    else:
        return False

def test_unsuccessful_run():
    # Simulate user input
    OUTPUT_INDEX = 2

    output = run_file_get_output_unsuccessful()
    last_string_output = output[OUTPUT_INDEX]

    EXPECTED_SIMPLE_STRING = F"You lose all -{BET_AMOUNT*2} in total"

    if (EXPECTED_SIMPLE_STRING.lower() in last_string_output.lower()):

        return True
    else:
        return False

if __name__ == '__main__':
    run_success = test_successful_run()
    run_unsuccessful = test_unsuccessful_run()

    if run_success and run_unsuccessful:
        print("success python step")
    else:
        print("unsuccessful python step")