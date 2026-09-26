#Marcus Ee
#vowel_remover
#removes vowels from text

import re

def main():
    removeVowels()

def removeVowels():
    new_text = []
    vowels = {"a", "e", "i", "u", "o"}
    text = input("Enter message: ").casefold().split(" ")

    for i in range(len(text)):
        letters = list(text[i])
        filtered_text = [x for x in letters if x not in vowels]
        new_text.append("".join(filtered_text))

    for i in range(len(new_text)):
        print(f"{new_text[i]} ", end="")

main()