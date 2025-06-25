def read(data="stocks.txt"):
    """
    Summary:
        Reads stock data from a text file and stores it in a dictionary where each item is assigned a unique numeric ID.

    Parameters:
        data (str): The filename of the stock file to read from. Defaults to "stocks.txt".

    Returns:
        dict: A dictionary of stock items with the structure:
              {
                  1: [ProductName, Brand, Quantity, Cost],
                  2: [ProductName, Brand, Quantity, Cost],
                  ...
              }

    Raises:
        FileNotFoundError: If the specified stock file does not exist.
        IOError: If there is an error while reading the file.

    Examples:
        >>> read()
        {
            1: ["Shampoo", "Dove", "10", "150"],
            2: ["Soap", "Lux", "20", "50"]
        }

        >>> read("backup_stock.txt")
        {
            1: ["Cream", "Nivea", "5", "200"]
        }
    """
   
    a = {}  # Creating an empty dictionary to store stock items

    # Open the file stocks.txt in read mode
    with open(data, "r") as data: 
        name = data.readlines()  # Read all lines from the file into a list
   

    idd = 1  # Initialize ID starting from 1

    # Loop through each line in the file
    for line in name:
        line = line.replace("\n", "").split(",")  # Removes newline and split the line by comma
        a[idd] = line  # Stores the list as value in dictionary with key as idd
        idd += 1  # Increment ID for next item
    return a
