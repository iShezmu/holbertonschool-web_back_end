#!/usr/bin/env python3
""" Type-annotated function sum_list which
takes a list input_list of floats as argument"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """"Function that takes a list of floats as
    argument and returns their sum as a float."""
    return sum(input_list)
