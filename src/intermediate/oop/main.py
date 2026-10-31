from user import User 

user = User("Alice", 30, "qwerty")
print(user.get_info())
user.change_password("newpassword")
print(user.get_info())
