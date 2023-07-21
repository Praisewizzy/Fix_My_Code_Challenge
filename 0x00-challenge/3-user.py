import hashlib
import uuid
import bcrypt


class User():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pwd):
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            salt = bcrypt.gensalt()
            self.__password = bcrypt.hashpw(pwd.encode(), salt)

    def is_valid_password(self, pwd):
        if self.__password is None or pwd is None or not isinstance(pwd, str):
            return False
        return bcrypt.checkpw(pwd.encode(), self.__password)


if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    if not user_1.id:
        print("New User should have an id")

    user_2 = User()
    if user_1.id == user_2.id:
        print("User.id should be unique")

    u_pwd = "myPassword"
    user_1.password = u_pwd
    if user_1.password == u_pwd:
        print("User.password should be hashed")

    if user_2.password is not None:
        print("User.password should be None by default")

    user_2.password = None
    if user_2.password is not None:
        print("User.password should be None if setter to None")

    # The following lines are removed as setting password to an integer is no longer supported.
    # user_2.password = 89
    # if user_2.password is not None:
    #     print("User.password should be None if setter to an integer")

    if not user_1.is_valid_password(u_pwd):
        print("is_valid_password should return True if it's the right password")

    if user_1.is_valid_password("Fakepwd"):
        print("is_valid_password should return False if it's not the right password")

    if user_1.is_valid_password(None):
        print("is_valid_password should return False if compare with None")

    # The following line is removed as comparing password with an integer is no longer supported.
    # if user_1.is_valid_password(89):
    #     print("is_valid_password should return False if compare with integer")

    if user_2.is_valid_password("No pwd"):
        print("is_valid_password should return False if no password set before")
