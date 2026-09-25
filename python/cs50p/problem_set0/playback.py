#Marcus Ee
#play_back_speed
#Repeats what user types slowly

#puts input into list
text = input("Enter text to play back: ").split()
for i in range(len(text)):
    print(f"{text[i]}...", end="")
