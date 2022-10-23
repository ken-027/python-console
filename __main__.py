from csv import excel_tab
from typing import final
from modules.calculator import Calculator
from modules.system import *

apps = [
    {
        "shortcut": "c",
        "name": Calculator.app_name,
        "app": Calculator
    },
]


def main():
    try:
        cmd = ''
        while cmd not in ['exit', '-e']:
            greet()
            cout(f'Avialable Apps: {len(apps)}')

            for app in apps:
                app_shortcut = str(app.get('shortcut')).upper()
                app_name = app.get('name')
                cout(f'[{app_shortcut}] {app_name}', 'success')

            space()

            if cmd == 'c':
                try:
                    Calculator.app()
                except ValueError:
                    cout('Please enter a valid number!', 'fail')
                    cin()
                    Calculator.app()

            cmd = cin(
                'please type to select from the apps or [exit][-e] to exit the app').lower()

    except ValueError:
        cout('Please enter a valid number!', 'fail')
        cin()
        main()
    except:
        cout('Error catch application exited!', 'fail')


main()
cout('Thank you for using my app 😊')
