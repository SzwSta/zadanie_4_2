
import math
def check_if_palindrome(word):
    """
        Based on argument passed, checks if given word is palindrome.
        Argument:
        word  
    """
    a=0
    for i in range(0,math.floor(len(word)/2)):
        if word[i]==word[len(word)-i-1]:
            a=+1
    print(a==math.floor(len(word)/2))
check_if_palindrome('kaatak')
