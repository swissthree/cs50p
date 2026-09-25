#Marcus Ee
#deep_thought
#Asks the user what the ultimate question to life is

text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold()
match text:
    case "42":
        print("yes")
        
    case "fortytwo":
        print("yes")

    case "forty two":
        print("yes")

    case "forty-two":
        print("yes")
        
    case _:
        print("no")
    