products = {}

# Main loop for the billing system
while True:
    print("\n1. Add Product")
    print("2. Create Invoice")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        # Adding a product
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        gst_rate = float(input("Enter GST rate (%): "))
        products[name] = {'price': price, 'gst_rate': gst_rate}
        print(f"Product '{name}' added.")

    elif choice == "2":
        # Creating an invoice
        if not products:
            print("No products available. Please add products first.")
            continue
        
        invoice = []
        print("Available Products:")
        
        for product_name, details in products.items():
            print(f"{product_name} - Price: {details['price']}, GST Rate: {details['gst_rate']}%")

        while True:
            product_choice = input("Select product by name to add to invoice (or 'done' to finish): ")
            if product_choice.lower() == 'done':
                break
            if product_choice in products:
                quantity = int(input("Enter quantity: "))
                invoice.append((product_choice, quantity))
                print(f"Added {quantity} x {product_choice} to the invoice.")
            else:
                print("Product not found. Please try again.")

        # Displaying the invoice
        print("\nInvoice Summary:")
        total_amount = 0

        for product_name, quantity in invoice:
            price = products[product_name]['price']
            gst_rate = products[product_name]['gst_rate']
            gst_amount = (price * gst_rate / 100) * quantity
            total_price = (price + gst_amount) * quantity
            total_amount += total_price
            print(f"{product_name} - Quantity: {quantity}, Total (incl. GST): {total_price:.2f}")

        print(f"Total Amount Due: {total_amount:.2f}")

    elif choice == "3":
        print("Exiting the system.")
        break

    else:
        print("Invalid option. Please try again.")