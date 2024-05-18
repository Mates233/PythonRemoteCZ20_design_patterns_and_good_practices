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

