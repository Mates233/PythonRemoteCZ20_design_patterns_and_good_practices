"""
Úkol 0 - SRP

Představte si systém pro malé internetové knihkupectví. Zpočátku je v kódu jediná třída,
která má na starosti několik úkolů: správu zásob knih, zpracování prodejních transakcí a generování prodejních zpráv.
Tato třída porušuje zásadu jedné odpovědnosti, protože má více než jeden důvod ke změně.

Přepracujte následující třídu Pythonu tak, aby dodržovala princip jediné odpovědnosti.
Třída v současné době zpracovává správu zásob, prodejní transakce a vykazování,
které by měly být odděleny do samostatných tříd.
"""


class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_book(self, title, quantity):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def remove_book(self, title, quantity):
        if title in self.inventory and self.inventory[title] >= quantity:
            self.inventory[title] -= quantity
            return True
        else:
            return False

    def get_inventory(self):
        return self.inventory


class SalesManager:
    def __init__(self):
        self.sales = []

    def sell_book(self, title, quantity, inventory_manager):        # Dependency Injection
        if inventory_manager.remove_book(title, quantity):
            self.sales.append((title, quantity))
        else:
            print("Book out of stock or not enough quantity.")

    def get_sales(self):
        return self.sales


class SalesReport:
    @staticmethod
    def generate_report(sales):
        report = "Sales Report:\n"
        for sale in sales:
            report += f"Title: {sale[0]}, Quantity: {sale[1]}\n"
        return report


# Usage Example
inventory_manager = InventoryManager()
sales_manager = SalesManager()
sales_report = SalesReport()

# Add books to inventory
inventory_manager.add_book("The Great Gatsby", 10)
inventory_manager.add_book("1984", 5)
inventory_manager.add_book("Bible", 8)

# Sell books
sales_manager.sell_book("The Great Gatsby", 2, inventory_manager)
sales_manager.sell_book("1984", 1, inventory_manager)
sales_manager.sell_book("Bible", 3, inventory_manager)

# Get inventory
print("Current Inventory:")
print(inventory_manager.get_inventory())

# Generate sales report
print(sales_report.generate_report(sales_manager.get_sales()))
