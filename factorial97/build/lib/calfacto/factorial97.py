def factorial(num):

  if not isinstance(num, (int, float)):
    return "You have given input a Character/String"

  if num % 1 != 0:  # Check if the number is not an integer.
    return "You have given input a Float number"

  if num < 0:  # Check if the number is negative.
    return "You have given input a Negative number"

  result = 1
  for i in range(1, int(num) + 1):
    result *= i

  return result


