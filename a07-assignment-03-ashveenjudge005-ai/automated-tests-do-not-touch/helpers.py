from io import StringIO
import sys
from unittest.mock import patch
from unittest import mock
import difflib
import runpy

def run_file_with_patches(
        file_name,
        user_input_patches=None,
        random_choice_patches=None
    ):
    if user_input_patches is None:
        user_input_patches = []
    if random_choice_patches is None:
        random_choice_patches = [True]

    # Redirect stdout to a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate user input and run the file
    with patch("builtins.input", side_effect=user_input_patches):
        with mock.patch('random.choice', side_effect=random_choice_patches):
            runpy.run_path(file_name)
    # Get the value of the captured output
    output = captured_output.getvalue().strip().split("\n")
    # Reset stdout to its original value
    sys.stdout = sys.__stdout__
    return output

def run_module_with_patches(
        module_name,
        user_input_patches=None,
        random_choice_patches=None
    ):
    if user_input_patches is None:
        user_input_patches = []
    if random_choice_patches is None:
        random_choice_patches = [True]

    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    # Patch input and random.choice during module execution
    with patch("builtins.input", side_effect=user_input_patches):
        with mock.patch("random.choice", side_effect=random_choice_patches):
            runpy.run_module(module_name, run_name="__main__")

    # Get the output
    output = captured_output.getvalue().strip().split("\n")

    # Reset stdout
    sys.stdout = sys.__stdout__

    return output

def assert_line_includes(line, includes, message=None):
    if message is None:
        message = F"Line does not include '{includes}'"
    assert includes.lower() in line.lower(), message

def read_file_lines(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip().split("\n")

def assert_similar_string(a, b, threshold=0.91):
    similarity = difflib.SequenceMatcher(None, a, b).ratio()
    assert similarity >= threshold, f"Strings '{a}' and '{b}' are not similar enough!"

def get_output_string_than_starts_with(output, starts_with):
    for line in output:
        if line.lower().startswith(starts_with.lower()):
            return line
    raise ValueError(f"No line starts with '{starts_with}'")

def get_line_that_includes(output, includes):
    for line in output:
        if includes.lower() in line.lower():
            return line
    raise ValueError(f"No line includes '{includes}'")

def get_line_index_that_includes(output, includes):
    for index, line in enumerate(output):
        if includes.lower() in line.lower():
            return index
    raise ValueError(f"No line includes '{includes}'")

def get_index_of_line_starting_with(output, starts_with):
    for index, line in enumerate(output):
        if line.lower().startswith(starts_with.lower()):
            return index
    raise ValueError(f"No line starts with '{starts_with}'")

