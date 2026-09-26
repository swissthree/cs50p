#Marcus Ee
#coke_machine
#user inserts coin to buy coke

def main():
    buyCoke()

def buyCoke():
    cost = 50
    print(f"Amount due: {cost}")
    pay = int(input("Insert coin: "))
    payment(cost, pay)

def payment(cost, pay):
    owed = abs(cost - pay)
    if pay >= cost:
        print(f"Change owed {owed}")
    elif pay < cost:
        print(f"Amount due: {owed}")
        new_pay = int(input("Insert coin: "))
        payment(owed, new_pay)


main()

