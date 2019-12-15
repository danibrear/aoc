import copy

with open('input5.txt', 'r') as f:
  orig_program = list(map(int, f.readlines()[0].split(',')))

def find_answer(orig_program, inp):
  POS_ARG = 0

  program = copy.deepcopy(orig_program)

  def get_arg(mode, index, pos):
    if mode == POS_ARG:
      return program[program[index + pos]]
    return program[index + pos]

  index = 0

  input_index = 0
  ret_val = 0
  while index < len(program):
    opcode = program[index]
    instruction = opcode % 100

    mode1 = (opcode // 100) % 10
    mode2 = (opcode // 1000) % 10
    mode3 = (opcode // 10000) % 10

    # print(program)
    # print(index, program[index])
    # print('instruction:', instruction)
    # print('mode A', mode1)
    # print('mode B', mode2)
    # print('mode C', mode3)
    # return 0

    if (int(instruction) == 1):
      first = get_arg(mode1, index, 1)
      second = get_arg(mode2, index, 2)

      if mode3 == POS_ARG:
        pos = program[index + 3]
      else:
        pos = index + 3
      program[pos] = first + second
      inc = 4
    elif (int(instruction) == 2):
      first = get_arg(mode1, index, 1)
      second = get_arg(mode2, index, 2)

      if mode3 == POS_ARG:
        pos = program[index + 3]
      else:
        pos = index + 3
      program[pos] = first * second
      inc = 4
    elif (int(instruction) == 3):
      pos = program[index + 1]
      program[pos] = inp[input_index]
      input_index += 1
      inc = 2
    elif (int(instruction) == 4):
      # print('Output:', program[program[index + 1]])
      ret_val = program[program[index + 1]]
      inc = 2
    elif (int(instruction) == 5): # jump-if-true
      first = get_arg(mode1, index, 1)
      second = get_arg(mode2, index, 2)
      if (first != 0):
        index = second
        inc = 0
      else:
        inc = 3
    elif (int(instruction) == 6): # jump-if-false
      first = get_arg(mode1, index, 1)
      second = get_arg(mode2, index, 2)
      if (first == 0):
        index = second
        inc = 0
      else:
        inc = 3
    elif (int(instruction) == 7):
      first = get_arg(mode1, index, 1)
      second = get_arg(mode2, index, 2)
      if mode3 == POS_ARG:
        pos = program[index + 3]
      else:
        pos = index + 3

      if (first < second):
        program[pos] = 1
      else:
        program[pos] = 0
      inc = 4

    elif (int(instruction) == 8):
      first = get_arg(mode1, index, 1)
      second = get_arg(mode2, index, 2)
      if mode3 == POS_ARG:
        pos = program[index + 3]
      else:
        pos = index + 3

      if (first == second):
        program[pos] = 1
      else:
        program[pos] = 0

      inc = 4
    elif (int(instruction) == 99):
      return ret_val
    index += inc  

if __name__ == '__main__':
  print('Part1:', find_answer(orig_program, [1]))

  print('Part2:', find_answer(orig_program, [5]))