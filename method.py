#Decorator
from functools import wraps

def dec(func):
    @wraps(func)#Tanpa ini fungsi input akan kehilangan docstring dan name bawaannya
    def wrap():
        print("Before")
        func()
        print("After")
    return wrap

@dec
def oyy():
    """Fungsi Oyy"""#Docstring
    print("oyyy")#Name


print(oyy.__name__)
print(oyy.__doc__)
