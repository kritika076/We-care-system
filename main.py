from read import read
from write import update
from operations import display,purchase,restock

def main():
        
        """
            Summary:
                Launches the WeCare inventory management system and presents a menu-driven interface for
                processing customer purchases, restocking inventory, and exiting the system.

            Parameters:
                None

            Returns:
                None

            Raises:
                ValueError: If the user inputs a non-integer value when prompted for a menu option.

            Examples:
                >>> main()
                Displays product list and prompts the user to select one of the following:
                - Process a customer purchase
                - Restock inventory from supplier
                - Exit the system

                The function handles user input, invokes appropriate operations, and repeats until exit is selected.
        """
        a=read()  
        display(a)
 

        # Main loop for admin options
        continue_loop = True
        while continue_loop:
            print("------------------------------------------------------------------------------------------")
            print("Here are the available actions you can perform in the system:")
            print("------------------------------------------------------------------------------------------")
            print("\n")
            print("Select 1 to process a customer purchase.")
            print("Select 2 to purchase stock from the supplier.")
            print("Select 3 to exit the system.")
            print("\n")
            print("------------------------------------------------------------------------------------------")
            print("\n")
            
            # Wait for user input here
            option = input("Enter your choice to proceed: ")
            try:
                option = int(option)  # Convert the input to an integer
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue  # Skip the current iteration if invalid input
            
            if option == 1:
                purchase(a)
                
            elif option==2:
                restock(a)

            elif option==3:
                continue_loop= False
                print("Thank you for using the system!")
                print("\n")
        

            # Handling wrong input
            else:
                print("Your option", option, "does not match our requirement. Enter valid number.")
                print("\n")
if __name__ == "__main__":
    main()
