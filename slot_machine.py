import random


MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
# symbol value - kaip multiplier laimejimui
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]  
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end = " | ")
            else:
                print(column[row], end ="")
        print()
        

def deposit():
    while True:
        ammount = input("deposit ammount? $")
        if ammount.isdigit():
            ammount = int(ammount)
            if ammount > 0:
                break
            else:
                print("Ammount must be over 0")
        else:
            print("please enter a number.")
    
    return ammount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("please enter a number.")
    
    return lines


def get_bet():
    while True:
        ammount = input("What would you like to bet on  each line? $")
        if ammount.isdigit():
            ammount = int(ammount)
            if MIN_BET <= ammount <= MAX_BET:
                break
            else:
                print(f"Ammount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a number.")
    
    return ammount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don not have enough money to bet that ammount, your current balance is ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. That is total of {total_bet}$")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer=="q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()