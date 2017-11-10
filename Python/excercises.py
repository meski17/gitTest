# defiene our recursive palindrome function


def isPalindrome(string):
    if len(string) <= 1:
        return True
    return string[0] == string[-1] and isPalindrome(string[1: -1])


print(isPalindrome("baabbbaab"))
