import random
from usercredentials import Usercredentials

"""
Import random to help us generate random passwords for our password locker
Random is a python package.A package is one or more modules that help us perfom a particular task.
"""
print("Hello 👋, Welcome to Password Locker 💪")
print("Password Suggestion:")
def password(length):
    """
    def - fuction
    """
    pl = str()
    """
    pl - password-locker
    """
    characters = "abcdefghijklmnopqrstuvwxyz1234567890/?|#!*%$@<>()"
    for i in range(length):
         pl = pl + random.choice(characters)

    print(pl)
    return pl

password(10)

print('Create password:')
password = input()
print('Create username:')
username = input()
print('Confirm password:')
confirm = input()

while confirm != password:
      print("Enter valid password! 😤 ")
      print("Enter Password")
      password = input()
      print("Confirm password")
      confirm = input()

else:
    print (f"Congratulations {username} Input was successful 🎉")

    print('Login To Your Account')
    print('Username:')
    username = input()
    print('Password:')
    password = input()
