from itertools import groupby
potentialrange = range(134564, 585159 + 1)

def has_double(digits):
  for x in range(len(digits) - 1):
    if digits[x] == digits[x+1]:
      return True
  return False

def always_increasing(digits):
  for x in range(len(digits) - 1):
    if digits[x] > digits[x+1]:
      return False
  return True

def has_only_double(digits):
  groups = [list(g) for k, g in groupby(digits)]
  for group in groups:
    if len(group) == 2:
      return True
  return False

count = 0
for potential in potentialrange:
  digits = list(map(int, str(potential)))
  if has_double(digits) and always_increasing(digits):
    count += 1

print('Part1:', count)
  
count = 0
for potential in potentialrange:
  digits = list(map(int, str(potential)))
  if has_only_double(digits) and always_increasing(digits):
    count += 1

print('Part2:', count)