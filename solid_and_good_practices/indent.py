import enum


number_of_orders = 10


class Order:
    def __init__(self):
        pass

    def add_order(self, order_type: str, order_value: str) -> bool:
        """
        this method adds an order to the database

        :param order_type: type of order
        :param order_value: value of order

        output boolean value if order was added
        """
        pass
        return True


MAX_VALUE = 1000


class OrderType(enum.Enum):
    ONLINE = 1      # oder from website
    OFFLINE = 2     # order from phone
    PHONE = 3       # order from phone
    EMAIL = 4       # order from email


is_prime = True
my_list = []

if MAX_VALUE > 1000 and number_of_orders > 8:  # This is super long comment that should be split into multiple lines to
    # fit the 79 characters limit
    pass

if my_list is not None:
    pass
