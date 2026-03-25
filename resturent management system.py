# Restaurant management system in python - @tech-rabi-7

food_menu = {
    "Veg": {
        1: {"name": "Veg Burger", "price": 100},
        2: {"name": "Veg Pizza", "price": 220},
        3: {"name": "Pasta Alfredo", "price": 180},
        4: {"name": "Paneer Butter Masala", "price": 200},
        5: {"name": "Dal Tadka", "price": 140},
        6: {"name": "Mix Veg Curry", "price": 150}
    },
    "Non-Veg": {
        1: {"name": "Chicken Burger", "price": 140},
        2: {"name": "Chicken Pizza", "price": 300},
        3: {"name": "Chicken Biryani", "price": 220},
        4: {"name": "Mutton Biryani", "price": 300},
        5: {"name": "Butter Chicken", "price": 260},
        6: {"name": "Chicken Curry", "price": 240}
    },
    "Desserts": {
        1: {"name": "Ice Cream", "price": 80},
        2: {"name": "Gulab Jamun", "price": 70}
    },
    "Drinks": {
        1: {"name": "Tea", "price": 40},
        2: {"name": "Coffee", "price": 80}
    }
}

def display_menu(menu):
    print("\n===== 🍴 RESTAURANT MENU 🍴 =====\n")
    for category, items in menu.items():
        print(f"--- {category} ---")
        for key, item in items.items():
            print(f"{key}. {item['name']} - ₹{item['price']}")
        print()

print("Welcome to Purnima's Cafe ☕")
display_menu(food_menu)

order_total = 0
cart = []

option = "yes"

while option == "yes":
    user_input = input("\nEnter items with quantity (e.g. 'tea 2' or 'pizza 1, ice cream 2'): ")
    
    items = user_input.split(",")

    for item in items:
        item = item.strip()
        parts = item.split()

        #  handle single word or multi-word item
        try:
            qty = int(parts[-1])
            item_name = " ".join(parts[:-1])
        except:
            print(f"Invalid format for '{item}' ❌ (use: item_name quantity)")
            continue

        found = False

        for category in food_menu:
            for key in food_menu[category]:
                if food_menu[category][key]["name"].lower() == item_name.lower():
                    price = food_menu[category][key]["price"]
                    total_price = price * qty
                    order_total += total_price

                    cart.append((item_name, qty, total_price))

                    print(f"{item_name} x{qty} added ✅ (₹{total_price})")
                    found = True

        if not found:
            print(f"Sorry we don't have {item_name} ❌")

    option = input("\nDo you want to order more? (yes/no): ").lower()

#  Final Bill
print("\n===== 🧾 FINAL BILL =====")
for item in cart:
    print(f"{item[0]} x{item[1]} = ₹{item[2]}")

print(f"\nTotal Amount to Pay: ₹{order_total}")
print("Thank you! Visit again 😊")