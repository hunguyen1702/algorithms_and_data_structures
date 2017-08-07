def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

print reverse("hello")
print reverse("l")
print reverse("follow")
print reverse("")

