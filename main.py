def Palindrome(s):
    return s == s[: : -1]
s = input()
slo= Palindrome(s)

if slo:
    print('true')
else:
    print('False')