#Marcus Ee
#camel_case
#converts camel case to snake case
import re

def main():
    text = input("camelCase: ")
    convertToSnake(text)

def convertToSnake(text):
    seperated_text = re.findall(r'[A-Z][a-z]*', text)
    converted_text = "_".join(seperated_text)
    print(f"snake_case: {converted_text}")

main() 