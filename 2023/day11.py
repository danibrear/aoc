from utils import aslist, splitlines, ingroups, getday, getpath


def part1(lines):
    rows = [i for i, line in enumerate(lines) if "#" not in line]
    cols = [i for i, _ in enumerate(lines) if "#" not in [row[i] for row in lines]]

    gals = [
        (i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == "#"
    ]

    extraspaces = (
        sum(
            [
                sum([i < row < k or k < row < i for row in rows])
                + sum([j < col < l or l < col < j for col in cols])
                for i, j in gals
                for k, l in gals
            ]
        )
        // 2
    )

    distances = (sum([abs(i - j) + abs(k - l) for i, k in gals for j, l in gals])) // 2

    print("part1", extraspaces + distances)  # 9509330
    print("part2", (extraspaces * 999_999) + distances)  # 635832237682


path = getpath(__file__)
with open("{}/day11.txt".format(path), "r") as f:
    lines = f.readlines()

    lines = aslist(lines)

    part1(lines)
