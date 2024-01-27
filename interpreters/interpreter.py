"""
This module holds the main logic of interpreters
"""
import argparse
from helpers import funcs
from configs import arg_templates, actions


class Interpreter:
    """
    Interpreter Class

    It holds the logic of the main interpreter which acts as a command line application
    """
    main_parser = argparse.ArgumentParser(prog="interpret")
    subparsers = main_parser.add_subparsers(
        title="subcategories", help="interpreters"
    )

    @classmethod
    def __create_number_interpreter(cls):
        """
        This method creates a subparser with the `number` argument as reference to use in cmd
        """
        number_parser = cls.subparsers.add_parser("number", help="interpret number to word equivalent")
        number_parser.add_argument(**arg_templates.num_arg_template,
                                   action=actions.LimitedRangeNumber, range_start=0, range_end=100)
        number_parser.set_defaults(func=funcs.interpret_num)

    @classmethod
    def __parse_args(cls):
        """
        This method parses and returns the arguments
        """
        args = cls.main_parser.parse_args()
        return args

    @classmethod
    def run(cls):
        """
        This is the main method that executes the whole logic
        """
        # Create the predefined interpreters
        cls.__create_number_interpreter()

        # Parse user argument inputs
        args = cls.__parse_args()

        # Run the passed parser keyword function's
        result = args.func(*args.input_num)
        print(result)
