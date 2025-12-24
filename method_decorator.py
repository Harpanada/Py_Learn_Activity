
from functools import wraps
#Decorator
# def dec(func):
#     @wraps(func)#Tanpa ini fungsi input akan kehilangan docstring dan name bawaannya
#     def wrap():
#         print("Before")
#         func()
#         print("After")
#     return wrap

# @dec
# def oyy():
#     """Fungsi Oyy"""#Docstring
#     print("oyyy")#Name


# print(oyy.__name__)
# print(oyy.__doc__)

class user:
    def __init__(self,role):
        self.role=role
        

def require_admin(f):
    @wraps(f)
    def wrapper(user, *args, **kwargs):
        if user.role != "admin":
            raise PermissionError("Akses ditolak")
        return f(user, *args, **kwargs)
    return wrapper



@require_admin
def check_user(user):
    print("User dihapus")



admin=user("admin")
guest=user("guest")

check_user(admin)
check_user(guest)


