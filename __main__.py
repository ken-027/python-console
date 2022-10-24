from ast import Try
from modules.system import *
# import apps
from app.calculator import Calculator
from app.rock_paper_scissors import RockPaperScissors

apps = [
    {
        "shortcut": "c",
        "name": Calculator.app_name,
        "app": Calculator
    },
    {
        "shortcut": "rps",
        "name": RockPaperScissors.app_name,
        "app": RockPaperScissors
    }
]


def main():
    try:
        cmd = ''
        clear()
        while cmd not in ['exit', '-e']:
            greet()
            cout(f'Avialable Apps: {len(apps)}')

            for app in apps:
                app_shortcut = str(app.get('shortcut')).upper()
                app_name = app.get('name')
                cout(f'[{app_shortcut}] {app_name}', 'success')

            space()

            cmd = cin(
                'please type to select from the apps or [exit][-e] to exit the app').lower()

            for app in apps:
                if cmd == app.get('shortcut'):
                    try:
                        app.get("app").start()
                    except ValueError:
                        cout('Please enter a valid number!', 'fail')
                        cin()
                        app.get("app").start()
                    

    except ValueError:
        cout('Please enter a valid number!', 'fail')
        cin()
        main()
    except:
        cout('Error catch application exited!', 'fail')


main()
cout('Thank you for using my app 😊')
