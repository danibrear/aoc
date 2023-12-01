from datetime import datetime
day = datetime.now().day

exec(open('day{0}.py'.format(day)).read())