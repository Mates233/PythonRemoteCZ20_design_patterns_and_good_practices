"""
Úkol 0 - SRP

Představte si systém pro malé internetové knihkupectví. Zpočátku je v kódu jediná třída,
která má na starosti několik úkolů: správu zásob knih, zpracování prodejních transakcí a generování prodejních zpráv.
Tato třída porušuje zásadu jedné odpovědnosti, protože má více než jeden důvod ke změně.

Přepracujte následující třídu Pythonu tak, aby dodržovala princip jediné odpovědnosti.
Třída v současné době zpracovává správu zásob, prodejní transakce a vykazování,
které by měly být odděleny do samostatných tříd.
"""

class BookStore:
    def __init__(self):
        self.inventory = {}
        self.sales = []

    def add_book(self, title, quantity):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def sell_book(self, title, quantity):
        if title in self.inventory and self.inventory[title] >= quantity:
            self.inventory[title] -= quantity
            self.sales.append((title, quantity))
        else:
            print("Book out of stock or not enough quantity.")

    def get_inventory(self):
        return self.inventory

    def get_sales_report(self):
        report = "Sales Report:\n"
        for sale in self.sales:
            report += f"Title: {sale[0]}, Quantity: {sale[1]}\n"
        return report


"""
Idealne definujte samostatné třídy, které budou
1 - starat se o inventuru (přidávání, odebírání)
2 - starat se o proces prodeje (prodej knih, vedení údajů o prodeji).
3 - starat se o vykazování prodeje (generování výkazu o prodeji).
"""