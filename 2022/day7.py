from utils import aslist, splitlines, ingroups
from collections import defaultdict as dd


class Dir():
    def __init__(self, parent, name, files, size):
        if (parent):
            self.name = parent.name + '/' + name
        else:
            self.name = ''
        self.files = files
        self.size = size
        self.parent = parent
        self.dirs = {}

    def addfile(self, file):
        [size, name] = file.split(' ')
        self.files.append([name, size])
        self.size += int(size)


def part1(lines):
    cwd = Dir(None, '', [], 0)
    root = cwd
    lineIdx = 0
    while lineIdx < len(lines):
        line = lines[lineIdx]
        if line.startswith('$ cd'):
            dir = line.split(' ')[-1].strip()
            if (dir == '..'):
                cwd = cwd.parent
            else:
                if dir not in cwd.dirs:
                    cwd.dirs[dir] = Dir(cwd, dir, [], 0)
                cwd = cwd.dirs[dir]
            lineIdx += 1

        elif line.startswith('$ ls'):
            lineIdx = lineIdx + 1
            at = cwd
            while (lineIdx < len(lines) and
                   not lines[lineIdx].startswith('$')):
                line = lines[lineIdx]
                if line.startswith('d'):
                    dir = line.split(' ')[-1]
                    if (dir not in cwd.dirs):
                        cwd.dirs[dir] = Dir(cwd, dir, [], 0)
                else:
                    cwd.addfile(line)
                lineIdx = lineIdx + 1
        else:
            print('skipping', line)
            lineIdx = lineIdx + 1

    total = 0

    def printDirs(dir):
        size = 0
        nonlocal total
        for f in dir.files:
            size += int(f[1])
        for d in dir.dirs.keys():
            size += printDirs(dir.dirs[d])
        # print('dir', (dir.name or '/'), 'size', size)
        if (size < 100000):
            total += size
        return size
    printDirs(root)

    print(total)


def part2(lines):
    cwd = Dir(None, '', [], 0)
    root = cwd
    lineIdx = 0
    while lineIdx < len(lines):
        line = lines[lineIdx]
        if line.startswith('$ cd'):
            dir = line.split(' ')[-1].strip()
            if (dir == '..'):
                cwd = cwd.parent
            else:
                if dir not in cwd.dirs:
                    cwd.dirs[dir] = Dir(cwd, dir, [], 0)
                cwd = cwd.dirs[dir]
            lineIdx += 1

        elif line.startswith('$ ls'):
            lineIdx = lineIdx + 1
            while (lineIdx < len(lines) and
                   not lines[lineIdx].startswith('$')):
                line = lines[lineIdx]
                if line.startswith('d'):
                    dir = line.split(' ')[-1]
                    if (dir not in cwd.dirs):
                        cwd.dirs[dir] = Dir(cwd, dir, [], 0)
                else:
                    cwd.addfile(line)
                lineIdx = lineIdx + 1

    smallestToDelete = 10**10
    total = 0

    def gettotal(dir):
        size = 0
        nonlocal total
        for f in dir.files:
            total += int(f[1])
        for d in dir.dirs.keys():
            gettotal(dir.dirs[d])

    gettotal(root)

    USED = 70000000
    NEEDED = 30000000
    totalunused = USED - total

    def printDirs(dir):
        size = 0
        nonlocal smallestToDelete
        for f in dir.files:
            size += int(f[1])
        for d in dir.dirs.keys():
            size += printDirs(dir.dirs[d])

        if (totalunused + size >= NEEDED and size < smallestToDelete):
            smallestToDelete = size
        return size
    printDirs(root)

    print(smallestToDelete)


with open('day7.txt', 'r') as f:

    lines = f.readlines()

    lines = aslist(lines)

    part1(lines)
    part2(lines)
    print('GO FUCK YOURSELF ADVENT OF CODE')
