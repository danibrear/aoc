from watchfiles import watch
from datetime import datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


DAY = datetime.now().day
print('{0}watching day{1}.py{2}\n'.format(bcolors.OKGREEN, DAY, bcolors.RESET))
last = None
count = 1
for changes in watch('./'):
    now = datetime.now()
    if last is not None and (now - last).total_seconds() < 1:
        continue
    last = now
    print(f'{bcolors.OKCYAN}({count}){bcolors.RESET}')
    day = datetime.now().day
    exec(open(f'day{day}.py').read())
    print(bcolors.OKBLUE, '-'*30, bcolors.RESET)
    count += 1
