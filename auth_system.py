# auth_system.py
from user import User

class AuthenticationSystem:
    def __init__(self):
        self.users = []

    def register(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)
        print("Registration successful.")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print("Login successful.")
                return True
        print("Invalid username or password.")
        return False

    def logout(self):
        print("Logout successful.")
