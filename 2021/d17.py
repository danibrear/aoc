from datetime import datetime
testX = [20, 30]
testY = [-10, -5]

realX = [207, 263]
realY = [-115, -63]


def parts1and2():

    X = realX
    Y = realY
    maxoverall = 0

    vs = 0

    for x in range(0, X[1] + 1):
        for y in range(-abs(Y[0]), abs(Y[0])):
            vx = x
            vy = y
            mh = 0
            px = 0
            py = 0
            hit = False
            while py >= Y[0] and px <= X[1]:
                px += vx
                py += vy
                vx -= 1 if vx > 0 else 0
                vy -= 1
                mh = max(mh, py)
                if X[0] <= px <= X[1] and Y[0] <= py <= Y[1]:
                    hit = True
                    # print("HIT:", counter, pos, mh)
                    break
            if hit:
                vs += 1
                maxoverall = max(maxoverall, mh)

    print('Part 1: [6555]', maxoverall)
    print('Part 2: [4973]', vs)


start = datetime.now()
parts1and2()
print(datetime.now() - start)
