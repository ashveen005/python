import unittest
from io import StringIO
import sys
from unittest import mock
import runpy

CORRECT_VALUE = 1
INCORRECT_VALUE = 2
BET_AMOUNT = 90

def run_file_get_output_success():
    # Redirect stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate user input and run the file
    with mock.patch('builtins.input', side_effect=["yes", BET_AMOUNT, CORRECT_VALUE]):
        # patch random
        with mock.patch('random.randint', return_value=CORRECT_VALUE):
            runpy.run_path('simple_dice_game.py')
    # Get the value of the captured output
    output = captured_output.getvalue().strip().split("\n")
    # Reset stdout to its original value
    sys.stdout = sys.__stdout__
    return output

def run_file_get_output_failed():
    # Redirect stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate user input and run the file
    # use incorrect value
    with mock.patch('builtins.input', side_effect=["yes", BET_AMOUNT, INCORRECT_VALUE]):
        # patch random
        with mock.patch('random.randint', return_value=CORRECT_VALUE):
            runpy.run_path('simple_dice_game.py')
    # Get the value of the captured output
    output = captured_output.getvalue().strip().split("\n")
    # Reset stdout to its original value
    sys.stdout = sys.__stdout__
    return output

def run_file_get_output_invalid():
    # Redirect stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate user input and run the file
    # invalid output
    with mock.patch('builtins.input', side_effect=["potato", BET_AMOUNT, INCORRECT_VALUE]):
        # patch random
        with mock.patch('random.randint', return_value=CORRECT_VALUE):
            runpy.run_path('simple_dice_game.py')
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

    EXPECTED_SIMPLE_STRING = F"Congratulations, you win {BET_AMOUNT*2}"

    if (EXPECTED_SIMPLE_STRING.lower() in last_string_output.lower()):

        return True
    else:
        return False

# successful run.
def test_unsuccessful_run():
    # Simulate user input
    OUTPUT_INDEX = 2

    output = run_file_get_output_failed()
    last_string_output = output[OUTPUT_INDEX]

    EXPECTED_SIMPLE_STRING = F"You lost your wager {BET_AMOUNT}"

    if (EXPECTED_SIMPLE_STRING.lower() in last_string_output.lower()):

        return True
    else:
        return False

def test_invalid_run():
    # Simulate user input
    OUTPUT_INDEX = 1

    output = run_file_get_output_invalid()
    last_string_output = output[OUTPUT_INDEX]

    EXPECTED_SIMPLE_STRING = F"Invalid input, Please try again"

    if (EXPECTED_SIMPLE_STRING.lower() in last_string_output.lower()):

        return True
    else:
        return False


if __name__ == '__main__':
    run_success = test_successful_run()
    run_unsuccess = test_unsuccessful_run()
    run_invalid = test_invalid_run()

    if run_success and run_unsuccess and run_invalid:
        print("success python step")
    else:
        print("unsuccessful python step")