def remove_white(s):
    return "".join(ch for ch in list(s) if ch.isalnum())


def palindrome_checker(s):
    s = remove_white(s)
    slist = list(s)
    if len(s) <= 1:
        return True
    else:
        return slist.pop() == slist.pop(0) and palindrome_checker("".join(slist))

print palindrome_checker("kayak")
print palindrome_checker("aibohiphobia")
print palindrome_checker("kanakanak")
print palindrome_checker("wassamassaw")
print palindrome_checker("madam i'm adam")


