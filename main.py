def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2
def power(n1, n2):
  return n1 ** n2
  
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
  "^" : power,
}

def calculator():
  first_num = float(input("What's the first number?: "))
  
  def calculate(num1):
    for entry in operations:
      print(entry)
    operation_symbol = input("Pick an operation: ")
    second_num = float(input("What's the next number?: "))
    function = operations[operation_symbol]
    answer = function(num1, second_num)
    print(f"{num1} {operation_symbol} {second_num} = {answer}")
    return answer
  
  answer = calculate(first_num)
  
  again = True
  while again:
    continue_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if continue_operation == 'n':
      again = False
      calculator()
    else: 
      first_num = answer
      answer = calculate(first_num)

calculator()