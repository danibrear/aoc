from utils import aslist, splitlines, ingroups, getday, getpath


def parts(lines):
    y = [m for m, j in enumerate(lines) if "#" not in j]
    x = [n for n, i in enumerate(lines[0]) if "#" not in (j[n] for j in lines)]
    p = [(n, m) for m, j in enumerate(lines) for n, i in enumerate(j) if i == "#"]
    k = sum(abs(n - u) + abs(m - v) for n, m in p for u, v in p) // 2
    r = (
        sum(
            sum(n < t < u or u < t < n for t in x)
            + sum(m < t < v or v < t < m for t in y)
            for n, m in p
            for u, v in p
        )
        // 2
    )
    print(k + r, k + 999999 * r)


path = getpath(__file__)
with open("{}/day11.txt".format(path), "r") as f:
    lines = f.readlines()

    lines = aslist(lines)

    parts(lines)
