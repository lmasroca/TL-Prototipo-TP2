#!/usr/bin/env python3
from lexer import tokenize_and_print
from parser import parse_and_print, ParseError
import optparse
import sys

usage = "usage: %prog [options] [expression]"

opt_parser = optparse.OptionParser(usage=usage)
opt_parser.add_option("-l", "--lexer", dest="lexer",
                      action="store_true", default=False,
                      help="only perform lexical analysis")
opt_parser.add_option("-i", "--interactive", dest="interactive",
                      action="store_true", default=False,
                      help="use interactive prompt")

options, args = opt_parser.parse_args()


def input_expression(prompt="", exit_command=None):
    try:
        exp_str = input(prompt)
    except EOFError:
        return None
    return exp_str if exit_command is None or exp_str != exit_command else None


def process_expression(expression):
    # try:
    if (options.lexer):
        tokenize_and_print(expression)
    else:
        try:
            parse_and_print(expression)
        except ParseError as error:
            print(f'ERROR: {error}', file=sys.stderr)
            return False
    return True


if options.interactive:
    try:
        while True:
            expression = input_expression(
                prompt="expression> ", exit_command=":q")
            if expression is not None:
                process_expression(expression)
            else:
                break
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit(0)
else:
    expression = input_expression()
    if expression is not None:
        status = process_expression(expression)
        if status:
            exit(0)
    exit(1)
