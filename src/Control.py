print("-------------------")
print("| Theater control |")
print("-------------------")

array = []
ticket_price = 0

def start_session():
    global ticket_price
    ticket_price = float(input("Enter the ticket price: "))

    x = 0

    while (x == 0):
        print("\nMax capacity: 40 rows by 60 column (2400 people).\n")
        columns = int(input("Insert how many columns: "))
        rows = int(input("Insert how many rows: "))

        if (columns > 60) or (rows > 40):
            print("Room arrangement not supported.")
        elif (columns <= 0) or (rows <= 0):
            print("Insert numbers greater than zero.")
        elif (columns <= 60) and (rows <= 40):
            for i in range(columns):
                rows_in_columns = ["F"] * rows
                array.append(rows_in_columns)

            print("Status: Valid arrangement.")
            x = 1
        else:
            print("Insert a valid value.")

    print("\n**************************\n")

def reserve_armchair():
    print("\nReserve a seat! Select the desired row and column.")
    reserve_row = int(input("Insert the row: "))
    reserve_column = int(input("Insert the column: "))

    loop = True

    while (loop == True):
        if (reserve_row > len(array)) or (reserve_column > len(array[0])):
            print("Invalid command! Select an available seat in the session.")
            break
        else:
            print(f"\nYou selected the seat row {reserve_row} and column {reserve_column}.")
            loop = False

    reserve_row = reserve_row - 1
    reserve_column = reserve_column - 1

    loop = True

    while (loop == True):
        if (array[reserve_row][reserve_column] == 'F'):
            array[reserve_row][ reserve_column] = 'R'
            print("\nThe seat has been successfully reserved.")
            # 30%
            loop = False
        elif (array[reserve_row][reserve_column] == 'R'):
            print("\nSeat not available. Please, choose another seat.")
            break
        elif (array[reserve_row][reserve_column] == 'O'):
            print("\nSeat not available. Please, choose another seat.")
            break
            
    print("\n**************************\n")

def buy_armchair():
    print("\nBuy a seat! Select the desired row and column.")
    buy_row = int(input("Insert the row: "))
    buy_column = int(input("Insert the column: "))

    loop = True

    while (loop == True):
        if (buy_row > len(array)) or (buy_column > len(array[0])):
            print("\nInvalid command! Select an available seat in the session.\n")
            return
        else:
            print(f"\nYou selected the seat row {buy_row} and column {buy_column}.\n")
            loop = False

    buy_row = buy_row - 1
    buy_column = buy_column - 1

    loop = True

    while (loop == True):
        if (array[buy_row][buy_column] == 'F'):
            array[buy_row][ buy_column] = 'O'
            print("Purchase made successfully.")
            # 100%
            loop = False
        elif (array[buy_row][buy_column] == 'R'):
            confirmation = str(input("Seat already reserved. Do you want to confirm the purchase? (y/n): "))
            if (confirmation == 'y'):
                array[buy_row][ buy_column] = 'O'
                print("\nPurchase made successfully.")
                # 70%
                loop = False
            elif (confirmation == 'n'):
                print("\nCancelled purchase.")
                break
        elif (array[buy_row][buy_column] == 'O'):
            print("Seat not available. Please, choose another seat.")
            break
            
    print("\n**************************\n")

def free_armchair():
    print("\nFree up a seat! Select the desired row and column.")
    free_row = int(input("Insert the row: "))
    free_column = int(input("Insert the column: "))

    loop = True

    while (loop == True):
        if (free_row > len(array)) or (free_column > len(array[0])):
            print("\nInvalid command! Select an available seat in the session.\n")
            return
        else:
            print(f"\nYou selected the seat row {free_row} and column {free_column}.\n")
            loop = False

    free_row = free_row - 1
    free_column = free_column - 1

    loop = True

    while (loop == True):
        if (array[free_row][free_column] == 'O'):
            confirmation = str(input("Seat already occupied. Do you want to confirm the cancellation of the purchase? (y/n): "))
            if (confirmation == 'y'):
                array[free_row][ free_column] = 'F'
                print("\nSeat successfully vacated.")
                # - 100%
                loop = False
            elif (confirmation == 'n'):
                print("\nSeat still occupied.")
                break
        elif (array[free_row][free_column] == 'R'):
            confirmation = str(input("Seat already reserved. Do you want to confirm the cancellation of the reservation? (y/n): "))
            if (confirmation == 'y'):
                array[free_row][ free_column] = 'F'
                print("\nSeat successfully vacated.")
                # - 30%
                loop = False
            elif (confirmation == 'n'):
                print("\nSeat still reserved.")
                break
        elif (array[free_row][free_column] == 'F'):
            print("Seat already available. Please, choose another seat.")
            break
            
    print("\n**************************\n")

def list_armchairs(array):
    print("\nDisplaying the session.\n")
    print("[F] = free seat\n[R] = reserved seat\n[O] = occupied seat\n")

    for rows in array:
        print(rows)

    print("\n**************************\n")

def close_theater(ticket_price):
    total_seats = len(array) * len(array[0])
    free_seats = 0
    reserved_seats = 0
    occupied_seats = 0

    for rows in array:
        for i in rows:
            if i == 'F':
                free_seats +=1
            elif i == 'R':
                reserved_seats +=1
            elif i == 'O':
                occupied_seats +=1

    # print(free_seats)
    # print(reserved_seats)
    # print(occupied_seats)

    total_reservation = ticket_price * reserved_seats * 0.3
    total_revenue = (ticket_price * occupied_seats) + (total_reservation)
    total_waste = (ticket_price * free_seats) + (ticket_price * reserved_seats * 0.7)


    if ((occupied_seats) > (total_seats * 0.6 + 1)):
        print("-------------------------------------")
        print(f"Total number of seats: {total_seats}")
        print(f"Total number of empty seats: {free_seats}")
        print(f"Total number of reserved seats: {reserved_seats}")
        print(f"Total number of seats sold: {occupied_seats}")
        print(f"Total revenue: $ {total_revenue}")
        print(f"Total not received: $ {total_waste}")
        print(f"Total in reservations: $ {total_reservation}")
        print("-------------------------------------")

        print("Closing the session!")
    else:
        print("\nGoal not reached. Keep selling!")

    print("\n**************************\n")

def restart_theater():
    print("\nRestarting the system!")
    global array
    global ticket_price
    array = []
    ticket_price = 0

    print("Booting the system...\n")
    print("New session initialized!\n")

a = 0

print("Welcome! Select an option:\n")
while (a == 0):
    print("- Insert [1] to start the theater;")
    print("- Insert [2] to reserve the armchair;")
    print("- Insert [3] to buy armchair;")
    print("- Insert [4] to free armchair;")
    print("- Insert [5] to list armchairs;")
    print("- Insert [6] to close the theater;")
    print("- Insert [7] to restart the theater.\n")

    option = int(input("Selected option: "))

    if (option == 1):
        if (array == []):
            start_session()
        else:
            print("A session is already active. Restart the theater with option '7'.\n")
    elif (option == 2):
        reserve_armchair()
    elif (option == 3):
        buy_armchair()
    elif (option == 4):
        free_armchair()
    elif (option == 5):
        list_armchairs(array)
    elif (option == 6):
        close_theater(ticket_price)
    elif (option == 7):
        restart_theater()
    else:
        print("\nInsert a valid value.\n")
