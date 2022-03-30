
import math
def check_if_palindrom1(word):
    a=0
    for i in range(0,math.floor(len(word)/2)):
        if word[i]==word[len(word)-i-1]:
            a=+1
    print(a==math.floor(len(word)/2))
check_if_palindrom1('kaatak')

def check_if_palindrom(word):
    b=[]
    c=[]
    for i in range(0,len(word)):
        b.append(word[len(word)-i-1])
        c.append(word[i])
    print(b==c)
check_if_palindrom('katak')


