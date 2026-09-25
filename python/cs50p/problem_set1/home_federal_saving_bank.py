#Marcus Ee
#home_federal_saving_bank
'''
If greeting starts with hello --> $0
If starts with h and not hello --> $20
else --> $100
'''
greeting = input("Greeting: ").casefold()
if greeting.join(greeting.split()) == "hello":
    print("$0")
    
elif greeting[0].join(greeting.split()) == "h":
    print("$20")

else:
    print("$100")