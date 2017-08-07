from stack import Stack


def is_match_type(open_sym, close_sym):
    opens = "([{"
    closes = ")]}"
    return opens.index(open_sym) == closes.index(close_sym)


def is_balanced_parentheses(par_str):
    s = Stack()
    balanced = True
    index = 0
    while index < len(par_str) and balanced:
        symbol = par_str[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                open_sym = s.pop()
                if not is_match_type(open_sym, symbol):
                    balanced = False
        index += 1

    if not s.is_empty():
        balanced = False
    return balanced


print is_balanced_parentheses("((()))")
print is_balanced_parentheses("(()")
print is_balanced_parentheses("{{([][])}()}")
print is_balanced_parentheses("(({)[)}]")
