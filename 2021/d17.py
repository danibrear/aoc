testX = [20, 30]
testY = [-10, -5]

realX = [207, 263]
realY = [-115, -63]


def step(vel, pos):
    np = [pos[0] + vel[0], pos[1] + vel[1]]
    nv0 = vel[0]
    if nv0 > 0:
        nv0 -= 1
    if nv0 < 0:
        nv0 += 1
    nv1 = vel[1] - 1

    return [np, [nv0, nv1]]


def intarget(pos, targetX, targetY):
    inX = targetX[0] <= pos[0] <= targetX[1]
    inY = targetY[0] <= pos[1] <= targetY[1]
    return inX and inY


def missed(pos, targetX, targetY):
    intarg = intarget(pos, targetX, targetY)
    if pos[1] < targetY[0] and not intarg:
        return True


def part1():
    vel = [6, 9]
    pos = [0, 0]

    counter = 0
    maxoverall = float('-inf')

    X = realX
    Y = realY

    for x in range(0, X[0]):
        for y in range(0, abs(Y[0])):
            vel = [x, y]
            pos = [0, 0]
            mh = float('-inf')
            hit = False
            counter = 0
            while counter < 300:

                # print(start)
                # print(step(start[1], start[0]))
                (newpos, newvel) = step(vel, pos)
                vel = newvel
                pos = newpos
                mh = max(mh, pos[1])
                counter += 1
                if intarget(pos, X, Y):
                    hit = True
                    # print("HIT:", counter, pos, mh)
                    break
                if missed(pos, X, Y):
                    break
            if hit:
                maxoverall = max(maxoverall, mh)
    print('Max height:', maxoverall)


def part2():
    vel = [6, 9]
    pos = [0, 0]

    counter = 0
    vels = []

    X = realX
    Y = realY

    for x in range(0, X[1] + 1):
        for y in range(-abs(Y[0]), abs(Y[0])):
            vel = [x, y]
            iv = [x, y]
            pos = [0, 0]
            mh = float('-inf')
            hit = False
            counter = 0
            while counter < 300:

                # print(start)
                # print(step(start[1], start[0]))
                (newpos, newvel) = step(vel, pos)
                vel = newvel
                pos = newpos
                mh = max(mh, pos[1])
                counter += 1
                if intarget(pos, X, Y):
                    hit = True
                    # print("HIT:", counter, pos, mh)
                    break
                if missed(pos, X, Y):
                    break
            if hit:
                vels.append(iv)
    print('hits:', len(vels))


print('Part 1: [6555]')
part1()
print('Part 2: [4973]')
part2()
