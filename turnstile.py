# write code to implement a turnstile
LOCKED = "locked"
UNLOCKED = "unlocked"

state=LOCKED




while True:
    order = input("Enter command (insertcoin, push, exit): ")
    if state == LOCKED:
        if order == "insertcoin":
            print("Coin inserted. You can now push the turnstile.")
            state == UNLOCKED
        elif order == "push":
            print("locked insert a coin first")
        else:
            print("invalid")


    elif state == UNLOCKED:
        if order == "insertcoin": 
            print("already unlocked, dont need coin")
        elif order == "push":
            print("you went through because you pushed. ")
        
    
    elif order == "exit":
        print("Exiting turnstile.")
        break
    else:
        print("invalid order,try again.")
        