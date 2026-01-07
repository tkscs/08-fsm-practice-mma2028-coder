

IDLE = "idle"
DISPENSED = "dispensed "
UNLOCKED = "unlocked"

state = "idle"
payment = None

x=100

while True:
    print(f"{state = }")
    print(f"{payment = }")
    
    if state == IDLE:
        order = input("Enter command(insert quarter, insert dollar bill, exit):")
        if order == "insert quarter":
            print("you may now choose your item 4")
            payment = 25
            state = UNLOCKED
        elif order == "insert dollar bill":
            print("you may now choose item 1")
            payment = 100
            state = UNLOCKED


    elif state == UNLOCKED:
        order = input("Enter command(press button item 1, press button item 4):")
        if order == "press button item 1":
            if payment == 25:
                print("you need 75 more cents for this item")
            if payment == 100:
                print("item 1 dispensed!")
                payment = 25
                state = UNLOCKED
        elif order == "press button item 4":
            if payment == 25:
                print("item 4 dispensed!")
                payment = None 
                state = UNLOCKED
            if payment == "dollar bill":
                print("You have 75 cents left")
                payment = 75
        elif order == "exit":
            print("leaving program")
            break

        else: 
            ("invalid put")



    elif order == "exit":
        print("Please insert money to start")
        break
    else:
        print("invalid")
            


    
        
        

