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
        self.__failed_log = []
        self.__locked = False

    def authenticate(self, username, password):
        if self.__locked:
            raise SecurityError(
                "Security Alert: Too many failed attempts! Account locked."
            )

        if not username or not password:
            raise AuthenticationError(
                "Authentication Error: Username or password cannot be empty"
            )

        if username == self.__username and password == self.__password:
            return True

        self.__failed_attempts += 1
        self.__failed_log.append((username, self.__failed_attempts))

        print(f"Invalid credentials. Attempt: {self.__failed_attempts}")

        if self.__failed_attempts >= 3:
            self.__locked = True
            raise SecurityError(
                "Security Alert: Too many failed attempts! Account locked."
            )

        return False


lines = sys.stdin.readlines()

if lines:
    n = int(lines[0].strip())
    login_system = LoginSystem()

    for i in range(1, n + 1):
        if i < len(lines):
            parts = lines[i].strip().split()
        else:
            parts = []

        username = parts[0] if len(parts) > 0 else ""
        password = parts[1] if len(parts) > 1 else ""

        try:
            if login_system.authenticate(username, password):
                print("Login successful!")
                break

        except AuthenticationError as e:
            print(e)

        except SecurityError as e:
            print(e)
            break