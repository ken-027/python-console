from os import stat
from modules.system import *
from modules.app import App
from random import randint


class RockPaperScissors(App):
    app_name = "Rock Paper Scissors"
    stats = {
        "computer": 0,
        "user": 0
    }
    rps_command = {
        "r": 0,
        "p": 1,
        "s": 2,
    }

    def who_is_winner():
        user = RockPaperScissors.stats['user']
        computer = RockPaperScissors.stats['computer']
        
        if user == computer:
            return cout('No one win the match', 'info')
        
        winner = 'You' if user > computer else 'Computer'
        cout(f'{winner} Won the match!',
             'success' if user > computer else 'fail')

    def round_match(user_command, ai_command):
        user_command = RockPaperScissors.rps_command.get(user_command)
        if (user_command == 0 and ai_command == 2) or (user_command == 1 and ai_command == 0) or (user_command == 2 and ai_command == 1):
            RockPaperScissors.stats['user'] += 1
            cout('you win!', 'success')
        elif user_command == ai_command:
            cout('No one win', 'info')
        else:
            RockPaperScissors.stats['computer'] += 1
            cout('try again!', 'fail')

    def start():
        clear()
        cmd = ''
        attempt = 10

        while cmd not in ['quit', '-q']:
            cout(f'Welcome {RockPaperScissors.app_name} App')
            space()
            cout('[R] Rock', 'success')
            cout('[P] Paper', 'success')
            cout('[S] Scissors', 'success')
            space()
            cout(f'Remaining attempt: {attempt}')
            cout('Standing')
            cout(
                f'User: {RockPaperScissors.stats["user"]} \t Computer: {RockPaperScissors.stats["computer"]}', 'info')
            attempt -= 1

            user_command = ''
            ai_command = randint(0, 2)

            while user_command not in ['r', 'p', 's']:
                user_command = cin('Select command from the list').lower()

            RockPaperScissors.round_match(user_command, ai_command)

            cin()
            space()

            if attempt > 0:
                clear()
                continue

            RockPaperScissors.who_is_winner()
            space()

            while cmd not in ['quit', '-q', 'restart', '-r']:
                cmd = cin(
                    f'please type [quit][-q] to exit or [restart][-r] to restart the {RockPaperScissors.app_name}').lower()

            space(2)

            if cmd in ['restart', '-r']:
                RockPaperScissors.start()
