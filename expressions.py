"""
  ALGO:  stack
  create an expression validator to test if brackets are correctly matched

  e.g. [a] True
       {(ab)cd} True
       [b False
       {c] False
       d} False
       } False
"""

def isValidExpression(expr):

    opens = { '(':')',
              '[':']',
              '{':'}'
             }

    closes = { ')':'(',
               ']':'[',
               '}':'{'
             }

    expr_list = list(expr)
    top = -1
    stack = []
    print('Initialized stack:  ', top, stack)
    for char in expr_list:
        if char in opens:
            stack.append(char)
            top = top + 1
            print('Pushed stack:  ', top, stack)
        elif char in closes:
            open_match = closes[char]
            if (top != -1):
                top_stack = stack[top]
            else:
                # missing open bracket
                print('Error:  Missing lead open bracket')
                return False
            if (top_stack == open_match):
                stack.pop();
                top = top - 1;
                print('Popped stack:  ', open_match, top, stack)
            else:
                # wrong bracket matched
                print('Error:  Mismatched brackets')
                return False
    print('Final stack:  ', top, stack)
    if (len(stack) == 0):
        return True
    else:
        # missing match brackets
        print('Error:  Missing matched brackets')
        return False


# CMD LINE TESTING

# Test1: [a] True
expr1 = '[a]'
print('\n\nTEST1', expr1)
isValid = isValidExpression(expr1)
print('isValid', isValid)

# Test2: {(ab)cd} True
expr2 = '{(ab)cd}'
print('\n\nTEST2', expr2)
isValid = isValidExpression(expr2)
print('isValid', isValid)

# Test3: [b False
expr3 = '[b'
print('\n\nTEST3', expr3)
isValid = isValidExpression(expr3)
print('isValid', isValid)

# Test4: {c] False
expr4 = '{c]'
print('\n\nTEST4', expr4)
isValid = isValidExpression(expr4)
print('isValid', isValid)

# Test4: d}
expr5 = 'd}'
print('\n\nTEST5', expr5)
isValid = isValidExpression(expr5)
print('isValid', isValid)



