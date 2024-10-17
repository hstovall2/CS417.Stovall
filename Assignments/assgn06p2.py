#Hudson Stovall
#Assignment 6 Refactoring #2

class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item['price'] * item['quantity']
        return total_price

    def apply_discount(self, total_price):
        if total_price > 100:
            print("Discount applied")
            return total_price * 0.9
        return total_price

    def calculate_shipping(self, total_price):
        return 10 if total_price < 50 else 0

    def process_order(self):
        total_price = self.calculate_total_price()
        print(f"Total price: {total_price}")
        
        final_price = self.apply_discount(total_price)
        print(f"Final price: {final_price}")
        
        shipping_cost = self.calculate_shipping(final_price)
        print(f"Shipping cost: {shipping_cost}")
        
        final_amount = final_price + shipping_cost
        print(f"Amount to be paid: {final_amount}")

items = [
    {'price': 20, 'quantity': 2},
    {'price': 50, 'quantity': 1},
]

order = Order(items)
order.process_order()
