from datetime import datetime
# Update stock information in the file
def update(a):
    """
    Summary:
        Updates the stock information in 'stocks.txt' by overwriting it with current inventory details.

    Parameters:
        a (dict): Dictionary containing product details. Each value is a list [name, brand, quantity, price, origin].

    Returns:
        None

    Raises:
        IOError: If there is an error while writing to the file.

    Examples:
        >>> inventory = {'101': ['Cream', 'Dove', '20', '120', 'India']}
        >>> update(inventory)
    """
    try:
        with open("stocks.txt", "w") as file:
            for product_details in a.values():
                file.write(",".join(product_details) + "\n")
    except IOError:
        print("Error writing to the products file!")
    print()


 # Saving bill to a file
def save_bill(customer_name, customer_phone, purchased_items,subtotal, shipping_fee, total_amount):
    """
    Summary:
        Generates and saves a detailed bill for the customer including item-wise purchase details, 
        subtotal, shipping fee, and total amount.

    Parameters:
        customer_name (str): Name of the customer.
        customer_phone (str): Phone number of the customer.
        purchased_items (list): List of purchased item details; each item is a list 
                                [name, brand, quantity, total_price, unit_price, free_quantity].
        subtotal (float): Total cost before shipping.
        shipping_fee (float): Additional shipping cost (if any).
        total_amount (float): Final total cost including shipping.

    Returns:
        None

    Raises:
        IOError: If writing to the bill file fails.

    Examples:
        >>> save_bill("Asha", "9800000000", [["Cream", "Dove", 3, 360, 120, 1]], 360, 50, 410)
    """
    try:
        transaction_time = datetime.now()
        with open(customer_name + customer_phone + ".txt", "w") as bill_file:
            bill_file.write("\t \t \t \t Product Shop Bill\n")
            bill_file.write("\t \t Newroad, Kathmandu | Phone No: 9811112255\n")
            bill_file.write("-----------------------------------------------------------------------------------------\n")
            bill_file.write("Customer Details:\n")
            bill_file.write("-----------------------------------------------------------------------------------------\n")
            bill_file.write("Name: " + customer_name + "\n")
            bill_file.write("Phone: " + customer_phone + "\n")
            bill_file.write("Date: " + str(transaction_time) + "\n")
            bill_file.write("-----------------------------------------------------------------------------------------\n")
            bill_file.write("\n")
            bill_file.write("Purchase Details:\n")
            bill_file.write("------------------------------------------------------------------------------------------\n")
            bill_file.write("Item Name \t Brand \t\t Quantity \t Free \t Unit Price \t Total")
            bill_file.write("------------------------------------------------------------------------------------------\n")
            for item in purchased_items:
                bill_file.write(item[0] + " \t " + str(item[1]) + " \t " + str(item[2]) + " \t\t " + str(item[5]) + " \t " + str(item[4]) + " \t\t $" + str(item[3]) + "\n")
            bill_file.write("------------------------------------------------------------------------------------------\n")
            if shipping_fee > 0:
                 bill_file.write("Shipping Fee: $" + str(shipping_fee) + "\n")
            bill_file.write("Grand Total: $" + str(total_amount) + "\n")
            
    except IOError:
        print("Error saving the bill to a file!")

    



 #supplier invoice
def save_invoice(supplier_name, restocked_items, total_cost,a):
    """
    Summary:
        Updates 'stocks.txt' with new stock values and generates a VAT invoice for the supplier 
        including all restocked items and total cost.

    Parameters:
        supplier_name (str): Name of the supplier.
        restocked_items (list): List of items restocked. Each item is a list 
                                [name, brand, quantity, unit_price, total_price].
        total_cost (float): Total cost of all restocked items.

    Returns:
        None

    Raises:
        IOError: If updating the stock file or writing the invoice file fails.

    Examples:
        >>> save_invoice("Nisha Traders", [["Lotion", "Nivea", "50", "200", "10000"]], 10000)
    """
    try:
        file = open("stocks.txt", "w")
        for item in a.values():
            line = item[0] + "," + item[1] + "," + item[2] + "," + item[3] + "," + item[4] + "\n"
            file.write(line)
        file.close()
    except IOError:
        print("Failed to update product file.\n")

            # Generate VAT invoice
    if len(restocked_items) > 0:
        now = datetime.now()
        timestamp = str(now).replace(":", "-").replace(".", "-").replace(" ", "_")
        filename = supplier_name.replace(" ", "_") + "_" + timestamp + ".txt"
                  

    try:
        invoice = open(filename, "w")
        invoice.write(" \t\tProduct Shop - VAT Invoice\n")
        invoice.write(" \t\tNewroad, Kathmandu | 01-4567898\n")
        invoice.write("---------------------------------------------------------------\n")
        invoice.write("Supplier Name: " + supplier_name + "\n")
        invoice.write("Date: " + str(now) + "\n")
        invoice.write("---------------------------------------------------------------\n")
        invoice.write("Product \t Brand \t\tQty \t Unit Cost \t Total\n")
        invoice.write("---------------------------------------------------------------\n")
        for item in restocked_items:
            line = item[0] + "\t" + item[1] + "\t" + item[2] + "\t" + item[3] + "\t\t" + item[4] + "\n"
            invoice.write(line)
        invoice.write("---------------------------------------------------------------\n")
        invoice.write("Total Amount: Rs. " + str(total_cost) + "\n")
        invoice.close()
        print("Restock complete. VAT invoice saved as '" + filename + "'\n")
    except IOError:
        print("Error writing invoice file.\n")
      
