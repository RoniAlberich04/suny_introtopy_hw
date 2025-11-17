import json
import urllib.request

# Part 1: Order Class
class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = {}  # item_name: price
    
    def add_item(self, item_name, price):
        self.items[item_name] = price
    
    def calculate_total(self):
        return sum(self.items.values())
    
    def calculate_vat(self, vat_rate=0.15):
        return self.calculate_total() * vat_rate
    
    def total_to_pay(self):
        return self.calculate_total() + self.calculate_vat()
    
    def display_order(self):
        print(f"\nOrder ID: {self.order_id}")
        print(f"Customer: {self.customer_name}")
        print("Items:")
        for item, price in self.items.items():
            print(f"  - {item}: ${price:.2f}")
        print(f"Subtotal: ${self.calculate_total():.2f}")
        print(f"VAT (15%): ${self.calculate_vat():.2f}")
        print(f"Total to pay: ${self.total_to_pay():.2f}")

# Test the Order class
def test_orders():
    print("=== Testing Order Class ===")
    
    # Create first order
    order1 = Order(35, "John Doe")
    order1.add_item("Milk", 2.3)
    order1.add_item("Butter", 3.4)
    order1.add_item("Chocolate", 3.0)
    order1.add_item("Soap", 4.5)
    order1.display_order()
    
    # Create second order
    order2 = Order(36, "Jane Smith")
    order2.add_item("Bread", 1.5)
    order2.add_item("Cheese", 5.2)
    order2.add_item("Water", 1.0)
    order2.display_order()

# Part 2: Book ISBN Lookup
def lookup_book():
    print("\n=== Book ISBN Lookup ===")
    isbn = input("Enter ISBN: ").strip()
    
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            title = data.get('title', 'Title not found')
            print(f"Book Title: {title}")
    except Exception as e:
        print(f"Error: Could not retrieve book information. {e}")

# Main menu
def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Test Orders")
        print("2. Lookup Book by ISBN")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            test_orders()
        elif choice == '2':
            lookup_book()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()