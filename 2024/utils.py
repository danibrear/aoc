def ingroups(lines):
    groups = []
    for line in lines:
        group = []
        if line == '\n':
            groups.append(group)
            group = []
        else:
            group.append(line.replace('\n', ''))

    groups.append(group)
    return groups

def aslist(lines):
    return [line.replace('\n', '') for line in lines]

def splitlines(lines, delimiter=" "):
    newlines = [line.replace('\n', '') for line in lines]

    if (delimiter != None):
        return [line.split(delimiter) for line in newlines]
    return newlines

def getday(file):
    day = file.split('/')[-1].split('.')[0]
    return day

def getpath(file):
    return '/'.join(__file__.split('/')[:-1])
