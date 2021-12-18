def isa(x):
    return type(x) == list


def magnitude(x):
    a = eval(x)

    def m(x):
        left, right = x
        lsum = 0
        rsum = 0
        if isa(left):
            lsum += 3 * m(left)
        else:
            lsum += 3 * left
        if isa(right):
            rsum += 2 * m(right)
        else:
            rsum += 2 * right
        return lsum + rsum
    return m(a)


assert(magnitude('[[1,2],[[3,4],5]]') == 143)
assert(magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]') == 1384)
assert(
    magnitude('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]') == 3488)


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

    def add_right_val(self, value):
        if isinstance(self.left, Snail):
            self.left.add_right_val(value)
        else:
            self.left += value

    def add_left_val(self, value):
        if isinstance(self.right, Snail):
            self.right.add_left_val(value)
        else:
            self.right += value

    def __str__(self):
        return str([self.left.__str__(), self.right.__str__()]).replace('\\', '').replace("'", '').replace('"', '')

    def explode(self):
        hasExploded = False
        l = r = None
        if self.depth < 4:
            if isinstance(self.left, Snail) and not hasExploded:
                [l, r, hasExploded] = self.left.explode()
                if (self.left.depth == 4):
                    self.left = 0
                if r is not None:
                    if isinstance(self.right, Snail):
                        self.right.add_right_val(r)
                    else:
                        self.right += r
                    r = None
            if isinstance(self.right, Snail) and not hasExploded:
                [l, r, hasExploded] = self.right.explode()
                if self.right.depth == 4:
                    self.right = 0
                if l is not None:
                    if isinstance(self.left, Snail):
                        self.left.add_left_val(l)
                    else:
                        self.left += l
                    l = None
            return [l, r, hasExploded]
        elif not hasExploded:
            _left = self.left
            _right = self.right
            return [_left, _right, True]

    def split(self):
        hassplit = False
        if isinstance(self.left, Snail):
            hassplit = self.left.split()
        elif type(self.left) == int and self.left >= 10 and not hassplit:
            n = Snail(self, self.depth + 1)
            n.left = self.left // 2
            n.right = (self.left + 1) // 2
            self.left = n
            return True
        if isinstance(self.right, Snail) and not hassplit:
            hassplit = self.right.split()
        elif self.right >= 10 and not hassplit:
            n = Snail(self, self.depth + 1)
            n.left = self.right // 2
            n.right = (self.right + 1) // 2
            self.right = n
            return True
        return hassplit


def parse(line):
    ns = eval(line)

    def create(parent, ns, depth):
        left, right = ns
        n = Snail(parent, depth)
        if isa(left):
            n.left = create(n, left, depth+1)
        else:
            n.left = left
        if isa(right):
            n.right = create(n, right, depth+1)
        else:
            n.right = right
        return n
    root = create(None, ns, 0)
    return root


def part1(lines):
    form = lines[0]
    for line in lines[1:]:
        form = "[" + form + "," + line + "]"
        root = parse(form)
        he = True
        while he:
            while he:
                [left, right, he] = root.explode()
            he = root.split()
        form = str(root)
    print('Part 1: [3665]: ', magnitude(form))


def part2(lines):
    maxMags = 0
    i = j = 0
    while i < len(lines) - 1:
        j = i+1
        while j < len(lines):
            form = "[" + lines[i] + "," + lines[j] + "]"
            root = parse(form)
            he = True
            while he:
                while he:
                    [left, right, he] = root.explode()
                he = root.split()
            form = str(root)
            maxMags = max(magnitude(form), maxMags)
            form = "[" + lines[j] + "," + lines[i] + "]"
            root = parse(form)
            he = True
            while he:
                while he:
                    [left, right, he] = root.explode()
                he = root.split()
            form = str(root)
            maxMags = max(magnitude(form), maxMags)
            j += 1
        i += 1
    print('Part 2: [4775]: ', maxMags)


with open('./d18.txt', 'r') as f:

    lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    # root = parse('[[[[[9,8],1],2],3],4]')
    # root = parse('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
    # root = parse('[[3,[2,[[7,3],1]]],[6,[5,[4,[3,2]]]]]')
    # root = parse('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')

    part1(lines)
    part2(lines)


def test():
    root = parse(
        '[[[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]')
    he = True
    while he:
        while he:
            print(str(root))
            [_, _, he] = root.explode()
            print('exploded')
            print(str(root))
            print('-' * 20)
        he = root.split()
    form = str(root)
    print(form)
