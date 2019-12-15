from day5 import find_answer
import copy

with open('input7.txt', 'r') as f:
  orig_program = list(map(int, f.readlines()[0].split(',')))


def solve_amps(input_amps, main_input):
  output = main_input
  for amp in input_amps:
    output = find_answer(orig_program, [amp, output])
  return output

def find_max_signal(low, high, main_input=0):
  max_output = 0
  max_pattern = []

  for a1 in range(low, high):
    for a2 in range(low, high):
      if a2 == a1:
        continue
      for a3 in range(low, high):
        if a3 in [a1, a2]:
          continue
        for a4 in range(low, high):
          if a4 in [a1, a2, a3]:
            continue
          for a5 in range(low, high):
            if a5 in [a1, a2, a3, a4]:
              continue
            output = solve_amps([a1, a2, a3, a4, a5], main_input)
            if output > max_output:
              max_output = output
              max_pattern = [a1, a2, a3, a4, a5]
  return max_output, max_pattern

