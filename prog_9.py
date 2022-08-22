#exception handling
#eof error
"""n=int(input())
print(n*10)
try:
    print(n*10)
except EOFError as e:
    print(e)"""
#import error
"""try:
    from time import DateTime
except ImportError as e:
    print(e)"""
#index error
"""try:
    list=[7,5,46,8]
    print(list[7])
except IndexError as e:
    print(e)"""
#value error
"""try:
    num=int(input("enter a number"))
except ValueError :
    print("enter a number not astring")
print("the number",num)"""