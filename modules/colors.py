# HEADER = '\033[95m'
# OKBLUE = '\033[94m'
# OKGREEN = '\033[92m'
# WARNING = '\033[93m'
# FAIL = '\033[91m'
# ENDC = '\033[0m'
# BOLD = '\033[1m'
# UNDERLINE = '\033[4m'
class Colors:
    select_colors = {
        "success": '\033[92m',
        "normal": '\033[94m',
        "fail": '\033[91m',
        'info': '\033[93m'
    }

    def validate_colors(colors):
        avail_colors = ['normal', 'success', 'fail', 'info']

        if colors not in avail_colors:
            raise Exception(f'{colors} not in the {avail_colors}')
