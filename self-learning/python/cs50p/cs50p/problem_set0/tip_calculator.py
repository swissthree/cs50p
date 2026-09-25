#Marcus Ee
#tip_calaculator
#calculate the tip along with the meal

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    dollars = round(float(d), 2)
    return dollars
def percent_to_float(p):
    percent = 1 + round(float(p), 2) / 100
    return percent

main()