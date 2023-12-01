from os.path import exists

with open('./_template.py', 'r') as f:
    template = ''.join(f.readlines())

for x in range(1, 32):
    day = 'day{0}'.format(x)
    if exists(day + '.py') or exists(day + '.txt'):
        print('skipping', day)
        continue
    with open('{0}.py'.format(day), 'w') as f:
        f.write(template)
    with open('{0}.txt'.format(day), 'w') as f:
        f.write('')