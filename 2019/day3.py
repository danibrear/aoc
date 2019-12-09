with open('input3.txt', 'r') as f:
  [line1, line2] = f.readlines()

def right(row, col, count):
  return [(row, col+x) for x in range(1, count + 1)]

def left(row, col, count):
  return [(row, col-x) for x in range(1, count + 1)]

def up(row, col, count):
  return [(row-x, col) for x in range(1, count + 1)]

def down(row, col, count):
  return [(row+x, col) for x in range(1, count + 1)]

startrow, startcol = 0,0

line1pos = []
l1row, l1col = startrow, startcol
for instruction in line1.split(','):
  if instruction[0] == 'R':
    line1pos.extend(right(l1row, l1col, int(instruction[1:])))
  elif instruction[0] == 'L':
    line1pos.extend(left(l1row, l1col, int(instruction[1:])))
  elif instruction[0] == 'U':
    line1pos.extend(up(l1row, l1col, int(instruction[1:])))
  elif instruction[0] == 'D':
    line1pos.extend(down(l1row, l1col, int(instruction[1:])))
  l1row, l1col = line1pos[-1]

line2pos = []
l2row, l2col = startrow, startcol
for instruction in line2.split(','):
  if instruction[0] == 'R':
    line2pos.extend(right(l2row, l2col, int(instruction[1:])))
  elif instruction[0] == 'L':
    line2pos.extend(left(l2row, l2col, int(instruction[1:])))
  elif instruction[0] == 'U':
    line2pos.extend(up(l2row, l2col, int(instruction[1:])))
  elif instruction[0] == 'D':
    line2pos.extend(down(l2row, l2col, int(instruction[1:])))
  l2row, l2col = line2pos[-1]

## VERY SLOW
# line1pos = list(set(line1pos))
# line2pos = list(set(line2pos))
# maxdist = float('inf')
# for pos in line1pos:
#   if pos in line2pos:
#     [row, col] = pos
#     print(row, col)
#     if (abs(row - startrow) + abs(col - startcol) > 0) and (abs(row - startrow) + abs(col - startcol)) < maxdist:
#       maxdist = abs(row - startrow) + abs(col - startcol)
# print(maxdist)

line1posset = set(line1pos)
line2posset = set(line2pos)

crosses = line1posset.intersection(line2posset)
maxdist = float('inf')
for pos in crosses:
  [row, col] = pos
  if (abs(row - startrow) + abs(col - startcol) > 0) and (abs(row - startrow) + abs(col - startcol)) < maxdist:
    maxdist = abs(row - startrow) + abs(col - startcol)

print('Part1:', maxdist)


steps = 1
line1stepcounts = {}
for pos in line1pos:
  if pos in crosses and pos != (startrow, startcol):
    line1stepcounts[pos] = steps
  steps += 1

steps = 1
line2stepcounts = {}
for pos in line2pos:
  if pos in crosses and pos != (startrow, startcol):
    line2stepcounts[pos] = steps
  steps += 1

shortest = float('inf')
for (pos, step) in line1stepcounts.items():
  if step + line2stepcounts[pos] < shortest:
    shortest = step + line2stepcounts[pos]

print('Part2:', shortest)