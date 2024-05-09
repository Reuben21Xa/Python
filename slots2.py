import random

# Constants defining the maximum number of lines to bet on and the betting range
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Constants defining the dimensions of the slot machine
ROWS = 3
COLS = 3

# Dictionary specifying how many of each symbol should appear in the slot machine
symbol_count = {
    "A": 2, # Symbol A appears 2 times
    "B": 4, # Symbol B appears 4 times
    "C": 6, # Symbol C appears 6 times
    "D": 8  # Symbol D appears 8 times
}

# Dictionary specifying the value of each symbol when matched in a line
symbol_value = {
    "A": 5, # Value of symbol A
    "B": 4, # Value of symbol B
    "C": 3, # Value of symbol C
    "D": 2  # Value of symbol D
}

# Function to check winnings based on the columns of symbols, lines bet on, bet amount, and symbol values
def check_winnings(columns, lines, bet, values):
    winnings = 0  # Initialize winnings
    winning_lines = []  # List to store winning line numbers

    # Loop through each line
    for line in range(lines):
        # Get the symbol at the current line in the first column
        symbol = columns[0][line]
        
        # Check if the current line in all columns has the same symbol
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                # If the symbols don't match, break the inner loop
                break
        else:
            # If all symbols in the line match, calculate winnings
            winnings += values[symbol] * bet
            # Add the winning line number (1-indexed) to the list
            winning_lines.append(line + 1)

    # Return total winnings and list of winning lines
    return winnings, winning_lines

# Function to randomly generate a slot machine spin with specified rows, columns, and symbols
def get_slot_machine_spin(rows, cols, symbols):
    # List to hold all possible symbols based on their counts
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # Add each symbol to the list the specified number of times
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # List to hold the columns of symbols
    columns = []
    for _ in range(cols):
        # List to hold the current column
        column = []
        # Copy the list of all symbols to use for the current column
        current_symbols = all_symbols[:]
        
        # Randomly select symbols to fill the column
        for _ in range(rows):
            # Choose a random symbol from the list of current symbols
            value = random.choice(current_symbols)
            # Remove the selected symbol from the list
            current_symbols.remove(value)
            # Add the selected symbol to the column
            column.append(value)
        
        # Add the completed column to the columns list
        columns.append(column)

    # Return the list of columns representing the slot machine spin
    return columns

# Function to print the slot machine grid of symbols
def print_slot_machine(columns):
    # Loop through each row
    for row in range(len(columns[0])):
        # Loop through each column
        for i, column in enumerate(columns):
            # Print the symbol at the current row and column
            # Use "|" as a separator between columns
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                # Don't add a separator at the end of the row
                print(column[row], end="")
        
        # Move to the next line after each row is printed
        print()

# Function to handle the deposit process
def deposit():
    while True:
        # Prompt the user to input the deposit amount
        amount = input("What would you like to deposit? $")
        # Check if the input is a valid number
        if amount.isdigit():
            amount = int(amount)  # Convert to integer
            # Check if the amount is greater than zero
            if amount > 0:
                break  # Exit the loop if valid
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    # Return the deposit amount
    return amount

# Function to handle the number of lines to bet on
def get_number_of_lines():
    while True:
        # Prompt the user to input the number of lines to bet on
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # Check if the input is a valid number
        if lines.isdigit():
            lines = int(lines)
            # Check if the number of lines is within the valid range
            if 1 <= lines <= MAX_LINES:
                break  # Exit the loop if valid
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    # Return the number of lines to bet on
    return lines

# Function to handle the bet amount per line
def get_bet():
    while True:
        # Prompt the user to input the bet amount per line
        amount = input("What would you like to bet on each line? $")
        # Check if the input is a valid number
        if amount.isdigit():
            amount = int(amount)
            # Check if the bet amount is within the valid range
            if MIN_BET <= amount <= MAX_BET:
                break  # Exit the loop if valid
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    # Return the bet amount per line
    return amount

# Function to handle a spin of the slot machine
def spin(balance):
    # Get the number of lines to bet on
    lines = get_number_of_lines()
    while True:
        # Get the bet amount per line
        bet = get_bet()
        # Calculate the total bet (bet per line times number of lines)
        total_bet = bet * lines

        # Check if the total bet is more than the current balance
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            # Break the loop if the total bet is within the balance
            break

    # Display the total bet and lines chosen
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    # Generate the slot machine spin
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    # Print the slot machine grid
    print_slot_machine(slots)
    # Check winnings from the spin
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    # Display the total winnings and the winning lines
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    
    # Return the net amount (winnings minus total bet)
    return winnings - total_bet

# Main function to control the game flow
def main():
    # Get the initial deposit from the user
    balance = deposit()
    while True:
        # Display the current balance
        print(f"Current balance is ${balance}")
        # Ask the user if they want to play or quit
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            # Exit the loop if the user wants to quit
            break
        # Call the spin function and update the balance
        balance += spin(balance)

    # Display the final balance when the user leaves the game
    print(f"You left with ${balance}")

# Call the main function to start the game
main()
