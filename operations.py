from datetime import datetime
def display(a):
    """
    Summary:
        Displays the current inventory in a formatted table including calculated selling prices.

    Parameters:
        a (dict): Dictionary containing product details. Each key maps to a list with item attributes.

    Returns:
        None

    Raises:
        None

    Examples:
        >>> inventory = read()
        >>> display(inventory)
    """
    
    print("*" * 70)
    print("ID \t Name \t\t brand \t\t qty \t price \t origin")
    print("*" * 70)
    for key, value in a.items():
        print(key, end="\t")
        for i, each in enumerate(value):
            if i == 3: 
                price = int(each) * 2  # Multiply the price by 2 for selling price
                print(price, end="\t")
            else:
                print(each, end="\t")
        print()
    print("*" * 70)

def purchase(a):
    """
    Summary:
        Handles customer purchase interactions, applies 'Buy 3 Get 1 Free' policy, 
        calculates billing totals, updates stock, and generates a printed bill and invoice file.

    Parameters:
        a (dict): Dictionary containing current inventory where keys are product IDs and 
                  values are lists of [name, brand, quantity, cost, origin].

    Returns:
        bool: True if the purchase was successful, False if an exception occurred.

    Raises:
        ValueError: If input for product ID or quantity is invalid.
        Exception: For any unexpected runtime errors.

    Examples:
        >>> inventory = read()
        >>> success = purchase(inventory)
        >>> if success:
        ...     print("Purchase completed!")
    """

    from write import update,save_bill

    print("------------------------------------------------------------------------------------------")
    print("To generate the bill, you need to enter the customer details:")
    print("------------------------------------------------------------------------------------------")
    print("\n")
        
    # Wrap customer input in try-except for possible input errors
    try:
        customer_name = input("Enter the customer's name: ")
        customer_phone = input("Enter the customer's phone number: ")
        print("\n")
        print("-----------------------------------------------------------------------------------------")
        print("\n")

        purchased_items = []  # List to store purchased items by the customer
        subtotal = 0  # Total bill before shipping
        total_amount = 0  # Final total after shipping
        shipping_fee = 0  # Shipping cost
        shopping_continue = True

        while shopping_continue:
            # Displaying available products
            print("*"*70)
            print("id \t name \t\t brand \t\t qty \t price \t origin")
            print("*"*70)

            for product_id, product_details in a.items():
                print(product_id, end="\t")
                for i in range(len(product_details)):
                    if i == 3:
                        print(int(product_details[3]) * 2, end="\t")  # Selling price (double the cost)
                    else:
                        print(product_details[i], end="\t")
                print()
            print("*" * 70)

            try:
                 # Getting product ID from customer
                product_id = int(input("Enter the product ID you wish to buy: "))
                while product_id <= 0 or product_id > len(a):
                      print("Invalid product ID! Please try again.")
                      product_id = int(input("Enter the product ID you wish to buy: "))
                    
                 # Getting quantity
                quantity = int(input("Enter the quantity you want to buy: "))
            except ValueError:
                   print("Invalid input! Please enter a number for product ID and quantity.")
                   continue

            available_stock = int(a[product_id][2])

            # If the stock is 0, prompt the user to select another product
            if available_stock == 0:
                print("Sorry, this product is out of stock.")
                shopping_continue = input("Would you like to continue shopping? (Select Y/N): ").lower()
                if shopping_continue == "n":
                    break  # This will break out of the loop, allowing the user to select another product
                elif shopping_continue == "y":
                    shopping_continue = True  # Continue shopping for more products
                else:
                    print("Invalid option. Returning to shopping cart.")
                    break  # Exit the shopping process if an invalid option is entered
            else:
                  # Buy 3 Get 1 Free offer logic
                free_items = quantity // 3
                total_deducted_quantity = quantity + free_items

                while total_deducted_quantity > available_stock or quantity <= 0:
                    if quantity <= 0:
                        print("Quantity must be a positive number.")
                    else: total_deducted_quantity > available_stock
                    print("Sorry, we only have " + str(available_stock) + " units of this product.")
                            
                    try:
                        quantity = int(input("Enter the quantity you want to buy: "))
                        free_items = quantity // 3
                        total_deducted_quantity = quantity + free_items
                    except ValueError:
                        print("Invalid input! Please enter a number for quantity.")
                        continue
                        
                     # After valid quantity, update the available stock
                available_stock -= total_deducted_quantity  # Subtract the deducted quantity from available stock
                a[product_id][2] = str(available_stock)  # Update stock in the data structure (must be string if a stores data as strings)
                print("Updated stock for product ID " + str(product_id) + ": " + str(available_stock))

                    # Ask if the customer wants to buy more
                shopping_continue = input("Would you like to buy more items? (Y/N): ").lower() in ['y', 'yes']

                 # Calculate bill for this item
                product_name = a[product_id][0]
                brand_name = a[product_id][1]
                unit_price = int(a[product_id][3]) * 2
                total_price = unit_price * quantity

                # Adding the item to the purchase list
                purchased_items.append([product_name, brand_name, quantity, unit_price, total_price, free_items])
                subtotal += total_price
         # Asking if customer wants shipping
        if purchased_items:
            shipping_input = input("Would you like to add shipping to your order? (Y/N): ").lower()
            if shipping_input == "y":
                shipping_fee = 500

         # Final total
            total_amount = subtotal + shipping_fee
            transaction_time = datetime.now()

            update(a)

            # Displaying the bill
            print("\t \t \t \t Product Shop Bill ")
            print("\n")
            print("\t \t Newroad, Kathmandu | Phone No: 9811112255 ")
            print("\n")
            print("-----------------------------------------------------------------------------------------")
            print("Customer Details:")
            print("-----------------------------------------------------------------------------------------")
            print("Name: " + customer_name)
            print("Phone: " + customer_phone)
            print("Date: " + str(transaction_time))
            print("-----------------------------------------------------------------------------------------")
            print("\n")
            print("Purchase Details:")
            print("-----------------------------------------------------------------------------------------")
            print("Item Name \t Brand \t\t Quantity \t Free \t Unit Price \t Total")
            print("-----------------------------------------------------------------------------------------")
            for item in purchased_items:
                print(item[0] + " \t " + str(item[1]) + " \t " + str(item[2]) + " \t\t " + str(item[5]) + " \t " + str(item[3]) + " \t\t $" + str(item[4]))
            print("-----------------------------------------------------------------------------------------")
            if shipping_fee > 0:
                print("Shipping Fee: $" + str(shipping_fee))
            print("Grand Total: $" + str(total_amount))
            print("\n")

            save_bill(customer_name, customer_phone, purchased_items, 
                          subtotal, shipping_fee, total_amount)
                          
            return True
    except Exception as e:
          print("An error occurred: " + str(e))
          return False

def restock(a):
    """
    Summary:
        Allows supplier to restock items in the inventory, modify prices if necessary, 
        updates the inventory, and generates a VAT invoice for the supplier.

    Parameters:
        a (dict): Dictionary representing current product inventory. Each value contains 
                  [name, brand, quantity, cost, origin].

    Returns:
        bool: True if restocking is successful and invoice is generated, False otherwise.

    Raises:
        ValueError: If non-numeric values are entered for ID or quantity.
        Exception: For unexpected errors during the restock process.

    Examples:
        >>> inventory = read()
        >>> success = restock(inventory)
        >>> if success:
        ...     print("Stock updated and invoice generated.")
    """
    from write import update,save_invoice
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("You have selected to restock inventory.\n")

    supplier_name = input("Enter the supplier/vendor name: ")
    if supplier_name == "":
        print("Supplier name is required to proceed.\n")
    else:
        restocked_items = []
        total_cost = 0
        continue_restock = True

        while continue_restock:
            # Display products
            print("Available products:\n")
            for key in a:
                print(str(key) + ". " + a[key][0] + " (" + a[key][1] + ") - Current Quantity: " + a[key][2] + ", Cost: " + a[key][3])
            print("\n")

            try:
                restock_id = int(input("Enter product ID to restock: "))
                if restock_id in a:
                     qty = int(input("Enter quantity to add: "))
                     if qty <= 0:
                        print("Quantity must be a positive number or more than 0.\n")
                        continue
                     new_price = input("Enter new cost price (press Enter to keep existing): ")

                        # Update quantity
                     prev_qty = int(a[restock_id][2])
                     a[restock_id][2] = str(prev_qty + qty)

                        # Update cost price
                     if new_price != "":
                        a[restock_id][3] = new_price
                     item_cost = int(a[restock_id][3]) * qty
                     total_cost += item_cost

                    # Store restocked item for invoice
                     restocked_items.append([a[restock_id][0], a[restock_id][1], str(qty), a[restock_id][3], str(item_cost)])
                     more= input("Add more products? (Y/N): ").lower() in ['y', 'yes']
                     if not more:
                        continue_restock = False
                else:
                        print("Invalid product ID.\n")
            except ValueError:
                    print("Please enter valid numbers for ID and quantity.\n")
            # Ask if user wants to restock more
        
        update(a)
          # Generate VAT invoice
        if len(restocked_items) > 0:
            now = datetime.now()
            timestamp = str(now).replace(":", "-").replace(".", "-").replace(" ", "_")
            filename = supplier_name.replace(" ", "_") + "_" + timestamp + ".txt"
                 #displaying the invoice
            print()
            print("\t\t Product Shop - VAT Invoice\n")
            print(" \t\tNewroad, Kathmandu | 01-4567898\n")
            print("---------------------------------------------------------------\n")
            print("Supplier Name: " + supplier_name + "\n")
            print("Date: " + str(now) + "\n")
            print("---------------------------------------------------------------\n")
            print("Product \t Brand \t\tQty \t Unit Cost \t Total\n")
            print("---------------------------------------------------------------\n")
            for item in restocked_items:
                line = item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3] + "\t\t" + item[4] + "\n"
                print(line)
            print("---------------------------------------------------------------\n")
            print("Total Amount: Rs. " + str(total_cost) + "\n")

            save_invoice(supplier_name, restocked_items, total_cost,a)
            return True 

