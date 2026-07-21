import sys


class AuthenticationError(Exception):
    pass


class SecurityError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.__username = "user1"
        self.__password = "securepassword"
        self.__failed_attempts = 0
        self.__locked = False

    def authenticate(self, username, password):

        if self.__locked:
            raise SecurityError(
                "Security Alert: Too many failed attempts! Account locked."
            )

        if username == "" or password == "":
            raise AuthenticationError(
                "Authentication Error: Username or password cannot be empty"
            )

        if username == self.__username and password == self.__password:
            return True

        self.__failed_attempts += 1
        print(f"Invalid credentials. Attempt: {self.__failed_attempts}")

        if self.__failed_attempts >= 3:
            self.__locked = True
            raise SecurityError(
                "Security Alert: Too many failed attempts! Account locked."
            )

        return False


n = int(input())
login_system = LoginSystem()

for _ in range(n):
    try:
        line = input()

        parts = line.split(" ", 1)

        username = parts[0] if len(parts) > 0 else ""
        password = parts[1] if len(parts) > 1 else ""

        if login_system.authenticate(username, password):
            print("Login successful!")
            break

    except AuthenticationError as e:
        print(e)

    except SecurityError as e:
        print(e)
        break