
from dataclasses import replace
import math
def check_if_palindrome(word):
    """
        Based on argument passed, checks if given word is palindrome.
        Argument:
        word  
    """
    a=0
    word=''.join(filter(str.isalnum,(word.replace(' ', '')).lower()))
    for i in range(0,len(word)):
        if word[i]==word[len(word)-i-1]:
            a=a+1
    return a==len(word)
print(check_if_palindrome('0A to Kamela, ale ,,ma kota.0'))
