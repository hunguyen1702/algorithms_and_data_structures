from stack import Stack


def is_higher_precedence(op1, op2):
    op_order = {
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        "(": 0
    }
    return op_order[op1] >= op_order[op2]


def infix_to_postfix(infix_str):
    infix_list = infix_str.split()
    op_stack = Stack()
    index =  0
    postfix_list = []
    while index < len(infix_list):
        token = infix_list[index]
        if token == '(':
            op_stack.push('(')
        elif token == ')':
            symbol = op_stack.pop()
            while symbol != '(':
                postfix_list.append(symbol)
                symbol = op_stack.pop()
        elif token in "*/+-":
            while not op_stack.is_empty() and is_higher_precedence(op_stack.peek(), token):
                symbol = op_stack.pop()
                postfix_list.append(symbol)
            op_stack.push(token)
        else:
            postfix_list.append(token)
        index += 1
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


print infix_to_postfix("A + B * C")
print infix_to_postfix("( A + B ) * C")
print infix_to_postfix("A * B + C * D")
print infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )")

