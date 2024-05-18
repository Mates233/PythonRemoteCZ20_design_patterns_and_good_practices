"""
Bridge je vzor, který umožňuje oddělit abstrakce, které spolu souvisí pomocí dědičnosti.
Předpokládejme, že implementujeme jednoduchý obchod, který prodává nápoje - kávu nebo čaj. Každý z těchto nápojů lze
zakoupit zděděním odpovídajícího předmětu představujícího nákup. Implementace v tomto případě úzce souvisí s abstrakcí
(např. třída Coffee spolu s třídou PaymentMethod, která by mohla představovat platbu), což znamená četné změny v
mnoha třídách v případě změny konceptu. Lepší nápad je oddělit abstrakci od implementace a seskupit
stávající prvky do samostatných hierarchií tříd.

Komponenty:
1.	Abstraction:
Třída Beverage představuje abstrakci. Definuje obecné chování (nákup) a obsahuje odkaz na instanci rozhraní PaymentMethod.
2.	Refined Abstraction:
Třídy Tea a Coffee rozšiřují třídu Beverage a poskytují specifické implementace pro metodu nákupu.
3.	Implementor:
Rozhraní PaymentMethod definuje metody, které musí konkrétní platební metody implementovat (platit).
4.	Concrete Implementors:
Třídy CreditCard a PayPal implementují rozhraní PaymentMethod a poskytují konkrétní implementace metody pay.
"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self, payment_method):
        self.payment_method = payment_method

    @abstractmethod
    def purchase(self):
        pass


class Tea(Beverage):
    def __init__(self, payment_method, price):
        super().__init__(payment_method)
        self.price = price

    def purchase(self):
        print("Purchasing tea...")
        self.payment_method.pay(self.price)


class Coffee(Beverage):
    def __init__(self, payment_method, price):
        super().__init__(payment_method)
        self.price = price

    def purchase(self):
        print("Purchasing coffee...")
        self.payment_method.pay(self.price)


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")


class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} in cash.")


def main():
    credit_card = CreditCard()
    paypal = PayPal()
    cash = Cash()

    tea_with_credit = Tea(credit_card, 3.5)
    coffee_with_paypal = Coffee(paypal, 4.5)
    tea_with_cash = Tea(cash, 3.0)

    tea_with_credit.purchase()
    coffee_with_paypal.purchase()
    tea_with_cash.purchase()


if __name__ == "__main__":
    main()
