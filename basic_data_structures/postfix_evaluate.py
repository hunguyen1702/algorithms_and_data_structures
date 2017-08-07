from stack import Stack


def do_math(first, second, op):
    if op == "+":
        return first + second
    if op == "-":
        return first - second
    if op == "/":
        return first / second
    if op == "*":
        return first * second


def postfix_eval(postfix_str):
    postfix_list = postfix_str.split()
    oprand_stack = Stack()
    for token in postfix_list:
        if token in "*/+-":
            second_op = oprand_stack.pop()
            first_op = oprand_stack.pop()
            oprand_stack.push(do_math(first_op, second_op, token))
        else:
            oprand_stack.push(int(token))
    return oprand_stack.pop()


print postfix_eval("7 8 + 3 2 + /")
print postfix_eval("17 10 + 3 * 9")
