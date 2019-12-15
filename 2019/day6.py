from collections import defaultdict as dd
with open('input6.txt', 'r') as f:
  orbits = ','.join(f.readlines()).replace('\n', '')

planets = dd(lambda: set())
points_to = {}

for orbit in orbits.split(','):
  planet,satelite = orbit.split(')')
  if satelite not in planets:
    planets[satelite] = set()
  planets[planet].add(satelite)
  points_to[satelite] = planet

def tree_from(node):
  count = 0
  visited = []

  if node not in planets:
    return 0
  
  queue = set(planets[node])

  while len(queue) > 0:
    curr = queue.pop()
    count += 1
    for p in planets[curr]:
      if p not in visited:
        queue.add(p)
    visited.append(curr)

  return count

def part1():
  return sum([tree_from(root) for root in planets.keys()])

print('Part1:', part1())

# find_ants finds all the ancestors of the given node 
def find_ants(node):
  ants = []
  curr = node
  while curr != 'COM':
    ants.append(points_to[curr])
    curr = points_to[curr]
  return ants

# from_to_common counts up the nodes until a node in the list is found
def from_to_common(node, them):
  curr = points_to[node]
  count = 0
  while curr not in them:
    count += 1
    curr = points_to[curr]
  return count

you_ants = find_ants('YOU')
san_ants = find_ants('SAN')

you_to_common = from_to_common('YOU', san_ants)
san_to_common = from_to_common('SAN', you_ants)
print('Part2:', you_to_common + san_to_common)