def math_operations(numbers: list[int]) -> None:
    print(f"Mean is {sum(numbers) / len(numbers)}")
    print(f"Max value is {max(numbers)}")


math_operations(numbers=[1, 2, 3, 4, 5])


def get_mean(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


def get_max(numbers: list[int]) -> int:
    return max(numbers)


def print_mean_and_max(numbers: list[int]) -> None:
    print(f"Mean is {get_mean(numbers)}")
    print(f"Max is {get_max(numbers)}")


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def update_email(self, new_email):
        self.email = new_email
        # Code to validate and update the email address


class UserAuthentication:
    def __init__(self, user):
        self.user = user

    def login(self, password):
        # Code to verify the user's password
        return True  # Simplified for example

# Example usage:
user = User("john_doe", "john@example.com")
auth = UserAuthentication(user)
auth.login("securepassword123")
