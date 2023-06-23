def Palindrome(s):
    return s == s[: : -1]
s = input()
slovo = Palindrome(s)

if slovo:
    print('true')
else:
    print('False')