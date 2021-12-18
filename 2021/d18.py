
def isa(x):
    return type(x) == list


class Snail():

    def __init__(self, parent, depth):
        self.left = None
        self.right = None
        self.depth = depth
        self.parent = parent

    def child_depth(self):
        if isa(self.left):
            return self.left.child_depth()

    def inc_depth(self):
        self.depth += 1
        if type(self.left) == Snail:
            self.left.inc_depth()
        if type(self.right) == Snail:
            self.right.inc_depth()

    def depth(self):
        return self.depth

    def add_right(self, value):
        if isinstance(self.left, Snail):
            self.left.add_left(value)
        else:
            print('adding', value, 'to', self.left)
            self.left += value

    def add_left(self, value):
        if isinstance(self.right, Snail):
            self.right.add_right(value)
        else:
            print('adding', value, 'to', self.right)
            self.right += value

    def __str__(self):
        return str([self.left.__str__(), self.right.__str__()])

    def explode(self):
        hasExploded = False
        l = r = None
        if self.depth < 4:
            if isinstance(self.left, Snail):
                [l, r] = self.left.explode()
                if l is not None and r is not None:
                    self.left = 0
                    hasExploded = True
                if isinstance(self.right, Snail) and r:
                    self.add_right(r)
                elif r:
                    self.right += r
                    r = None
            if isinstance(self.right, Snail) and not hasExploded:
                [l, r] = self.right.explode()
                if l is not None and r is not None:
                    self.right = 0
                if isinstance(self.left, Snail) and l:
                    self.add_left(l)
                    return [None, r]
                elif l:
                    self.left += l
                return [None, r]
            else:
                return [l, r]
        else:
            _left = self.left
            _right = self.left
            return [_left, _right]


def parse(line):
    ns = eval(line)

    def create(parent, depth):
        left, right = parent
        n = Snail(parent, depth)
        if isa(left):
            n.left = create(left, depth+1)
        else:
            n.left = left
        if isa(right):
            n.right = create(right, depth+1)
        else:
            n.right = right
        return n

    root = create(ns, 0)

    return root


def part1(lines):
    form = lines[0]
    for line in lines:
        pass


def part2(lines):
    for line in lines:
        pass


with open('./d18.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    # root = parse('[[[[[9,8],1],2],3],4]')
    root = parse('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
    root.explode()
    print(root)
    # part1(lines)
    # part2(lines)
