"""
Představte si, že máte starší rozhraní REST API, které poskytuje informace o uživateli v určitém formátu.
Potřebujete toto rozhraní API upravit tak, aby vyhovovalo novému rozhraní požadovanému vaší aplikací.
Starší rozhraní API vrací údaje o uživateli jako prostý slovník, zatímco vaše nové rozhraní vyžaduje metody pro
získání konkrétních údajů o uživateli, jako je jméno, e-mail a adresa.
"""


class LegacyUserAPI:

    def __init__(self):
        pass # bonus pridat data o useroch

    def get_user(self, user_id):
        # Simulate a REST API call to get user data
        return {
            "id": user_id,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip": "12345"
            }
        }


# třída User je v nasom pripade target
class User:
    def get_name(self):
        pass

    def get_email(self):
        pass

    def get_address(self):
        pass


# Implementace adaptéru
class LegacyUserAdapter(User):
  def __init__(self, legacy_user_api, user_id):
    self.legacy_user_api = legacy_user_api
    self.user_data = self.legacy_user_api.get_user(user_id)

  def get_name(self):
    return self.user_data["name"]

  def get_email(self):
    return self.user_data["email"]

  def get_address(self):
    address = self.user_data["address"]
    return f'{address["street"]}, {address["city"]}, {address["state"]} {address["zip"]}'


# chceme mít možnost zavolat metody get_name, get_email a get_address našeho nového uživatele
def main():
    legacy_user_api = LegacyUserAPI()

    user_id = 1
    user_adapter = LegacyUserAdapter(legacy_user_api, user_id)

    # Use the adapter to get user details
    print("User Details:")
    print(f"Name: {user_adapter.get_name()}")
    print(f"Email: {user_adapter.get_email()}")
    print(f"Address: {user_adapter.get_address()}")


if __name__ == '__main__':
    main()
