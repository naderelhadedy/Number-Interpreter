"""
This module holds the custom actions encapsulating validation logic
"""
import argparse


class LimitedRangeNumber(argparse.Action):
    """
    Limited Range Number Action Class

    It validates the input number falls within the defined range
    """
    def __init__(self, range_start, range_end, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.range_start = range_start
        self.range_end = range_end

    def __call__(self, parser, namespace, values, option_string=None):
        input_value = values[0]
        if input_value < self.range_start or input_value > self.range_end:
            raise argparse.ArgumentTypeError(
                f"{self.dest} must be between {self.range_start} and {self.range_end}"
            )
        setattr(namespace, self.dest, values)
