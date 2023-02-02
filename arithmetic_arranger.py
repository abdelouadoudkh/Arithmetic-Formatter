def arithmetic_arranger(problems, answers=False):

  first = ""
  second = ""
  lines = ""
  sumx = ""
  arranged_problems = ""

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    firstNumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]
    operands = problem.split(" ")
    if len(operands) != 3:
      return "Error: Operator must be '+' or '-'."
    if operands[1] not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
    if not operands[0].isdigit() or not operands[2].isdigit():
      return "Error: Numbers must only contain digits."
    if len(operands[0]) > 4 or len(operands[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    sum = ""

    if (operator == "+"):
      sum = str(int(firstNumber) + int(secondNumber))
    elif (operator == "-"):
      sum = str(int(firstNumber) - int(secondNumber))

    length = max(len(firstNumber), len(secondNumber)) + 2
    top = str(firstNumber).rjust(length)
    bottom = operator + str(secondNumber).rjust(length - 1)
    line = ""
    result = str(sum).rjust(length)
    for dash in range(length):
      line += "-"

    if problem != problems[-1]:
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += result + '    '
    else:
      first += top
      second += bottom
      lines += line
      sumx += result

  if answers:
    arranged_problems = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    arranged_problems = first + "\n" + second + "\n" + lines
  return arranged_problems
