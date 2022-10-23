import os
from modules.colors import Colors


def cout(context='', colors='normal'):
    Colors.validate_colors(colors)

    print(f"{Colors.select_colors.get(colors)}>> {context}")


def space(num=1):
    total_space = range(0, num)
    for space in total_space:
        cout()


def cin(context='', colors='normal'):
    Colors.validate_colors(colors)

    return input(f"{Colors.select_colors.get(colors)}>> {context}{'' if context == '' else ':'} ")


def clear():
    os.system('cls')
    os.system('clear')


def greet():
    clear()
    cout('Welcome to my Console app by @ken_27')
