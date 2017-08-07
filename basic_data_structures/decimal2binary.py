from stack import Stack


def decimal_to_binary(dec_num):
    remainder_stack = Stack()

    while dec_num > 0:
        remainder_stack.push(dec_num % 2)
        dec_num = dec_num / 2

    binary_string = ""
    while not remainder_stack.is_empty():
        binary_string += str(remainder_stack.pop())

    return binary_string

print decimal_to_binary(233)


def base_converter(dec_num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    remainder_stack = Stack()

    while dec_num > 0:
        remainder_stack.push(dec_num % base)
        dec_num = dec_num / base 

    binary_string = ""
    while not remainder_stack.is_empty():
        binary_string += digits[remainder_stack.pop()]

    return binary_string


print base_converter(25, 8)
print base_converter(256, 16)
print base_converter(26, 26)

