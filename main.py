# main.py
from auth_system import AuthenticationSystem

def main():
    auth_system = AuthenticationSystem()

    # Registration
    auth_system.register("user1", "password1")

    # Login
    if auth_system.login("user1", "password1"):
        # Perform actions after successful login
        pass

    # Logout
    auth_system.logout()

if __name__ == "__main__":
    main()
