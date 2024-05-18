"""
„Řetěz odpovědnosti“ je vzor, který popisuje, jak vytvořit řetězec objektů,
které jsou schopny zpracovat konkrétní požadavek.
Takový požadavek obvykle odešle klient a poté přechází k prvnímu prvku řetězce.
Pokud je první prvek schopen správně zpracovat požadavek, řetězec opustí, což také neznamená žádný "kontakt" se
zbytkem řetězce (často nazývaným "handlery"). Na druhou stranu, pokud prvek řetězce není schopen požadavek zpracovat,
pak – pokud nejde o poslední prvek řetězce – se snaží přesunout odpovědnost za jeho vyřízení na další prvek.
"""


import random


# Base class for credentials
class Credentials:
    def get_credentials(self, user_id):
        pass


# Concrete implementations of Credentials
class AWSSignature(Credentials):
    def get_credentials(self, user_id):
        return "98f92d42-66c7-4ce4-a834-087a783133e7"


class BearerToken(Credentials):
    def get_credentials(self, user_id):
        return "1/mZ1edKKACtPAb7zGlwSzvs72PvhAbGmB8K1ZrGxpcNM"


class UserNameAndPasswordCredentials(Credentials):
    def get_credentials(self, user_id):
        return "andrew:Andrew_123"


# Base class for authentication handlers
class AuthenticationHandler:
    def authenticate(self, credentials):
        pass

    def supports(self, credentials):
        pass


# Concrete implementations of AuthenticationHandler
class AWSAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.authenticate_in_aws(credentials)
        return False


    def supports(self, credentials):
        return isinstance(credentials, AWSSignature)

    def authenticate_in_aws(self, credentials):
        return random.randint(1, 3) == 1


class BearerTokenAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.is_token_valid(credentials)
        return False

    def supports(self, credentials):
        return isinstance(credentials, BearerToken)

    def is_token_valid(self, credentials):
        return random.randint(1, 3) == 2


class UserNameAndPasswordAuthenticationHandler(AuthenticationHandler):
    def authenticate(self, credentials):
        if self.supports(credentials):
            return self.is_password_valid(credentials)
        return False

    def supports(self, credentials):
        return isinstance(credentials, UserNameAndPasswordCredentials)

    def is_password_valid(self, credentials):
        return random.randint(1, 3) == 3


# Chain element for authentication
class ChainAuthenticationElement:
    def __init__(self, authentication_handler, next_element=None):
        self._authentication_handler = authentication_handler
        self._next_element = next_element

    def authenticate(self, credentials):
        if self._authentication_handler.authenticate(credentials):
            print(f"Authentication succeeded using {self._authentication_handler.__class__.__name__}")
            return True
        elif self._next_element:
            return self._next_element.authenticate(credentials)
        else:
            print(f"Authentication failed using {credentials.__class__.__name__}")
            return False


def main():
    # Create authentication handlers
    username_password_handler = UserNameAndPasswordAuthenticationHandler()
    bearer_token_handler = BearerTokenAuthenticationHandler()
    aws_signature_handler = AWSAuthenticationHandler()

    # Create the chain of responsibility
    last_element = ChainAuthenticationElement(aws_signature_handler)
    middle_element = ChainAuthenticationElement(bearer_token_handler, last_element)
    first_element = ChainAuthenticationElement(username_password_handler, middle_element)

    # Authenticate using different credentials
    first_element.authenticate(AWSSignature())
    first_element.authenticate(UserNameAndPasswordCredentials())
    first_element.authenticate(BearerToken())

if __name__ == '__main__':
    main()
