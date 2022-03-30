
from dataclasses import replace
import math
def check_if_palindrome(word):
    """
        Based on argument passed, checks if given word is palindrome.
        Argument:
        word  
    """
    word=''.join(filter(str.isalnum,(word.replace(' ', '')).lower()))
    return word==word[::-1]
print(check_if_palindrome('0A to Kamela, ale ,,ma kota.0'))

