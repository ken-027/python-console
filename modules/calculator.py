from ast import operator
from calendar import c
from math import prod, remainder
from modules.system import *


class Calculator:
    app_name = 'Calculator'

    operation_msg = {
        "a": "Sum",
        "s": "Difference",
        "m": "Product",
        "d": "Division",
        "s": "Remainder"
    }

    def multiply(numbers):
        product = None
        for num in numbers:
            product = num if product == None else product * num
        return product

    def add(numbers):
        sum = 0
        for num in numbers:
            sum += num
        return sum

    def subtract(numbers):
        difference = None
        for num in numbers:
            difference = num if difference == None else difference - num
        return difference

    def divide(numbers):
        division = None
        for num in numbers:
            division = num if division == None else division / num
        return division

    def modulus(numbers):
        remainder = None
        for num in numbers:
            remainder = num if remainder == None else remainder / num
        return remainder

    def app():
        clear()
        cmd = ''

        cout('Calculator App')
        space()

        rows = int(cin('Enter numbers you want to operate'))

        num_to_operate = range(rows)
        entered_number = []

        for i in num_to_operate:
            entered_number.append(float(cin(f'Enter number {i + 1}')))

        space()
        cout('[A]Add', 'success')
        cout('[S]Subtract', 'success')
        cout('[M]Mutliply', 'success')
        cout('[D]Divide', 'success')
        cout('[O]Modulus', 'success')

        while cmd not in ['quit', '-q']:
            result = ''
            operator = ''

            while operator not in ['a', 's', 'm', 'd', 'o']:
                operator = cin(
                    'Select Operation from the command list').lower()

            match operator:
                case 'a':
                    result = Calculator.add(entered_number)
                case 's':
                    result = Calculator.subtract(entered_number)
                case 'm':
                    result = Calculator.multiply(entered_number)
                case 'd':
                    result = Calculator.divide(entered_number)
                case 'o':
                    result = Calculator.modulus(entered_number)
                case _:
                    continue

            cout(
                f'The {Calculator.operation_msg[operator]} of numbers is {result}')

            space()
            while cmd not in ['quit', '-q', 'restart', '-r']:
                cmd = cin(
                    f'please type [quit][-q] to exit or [restart][-r] to restart the {Calculator.app_name}').lower()

            space(2)

            if cmd in ['-r', 'restart']:
                Calculator.app()
