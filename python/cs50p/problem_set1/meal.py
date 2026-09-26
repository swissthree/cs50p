#Marcus
#meal_time
#user inputs a time and comupter judges wheither it's meal time or not

def main():
    time = input("What time is it? ").split(":")
    try: 
        if time[1].split("p")[1] == "m":
            convertTime(int(time[0]))
    except IndexError:    
        checkMealTime(int(time[0]))

def convertTime(time):
    checkMealTime(time + 12)
    
def checkMealTime(hour):
    if hour >= 7 and hour <= 8:
        print("Breakfast time!")
    elif hour >= 12 and hour <= 13:
        print("Lunch time!")
    elif hour >= 18 and hour <= 19:
        print("Dinner time!") 
    else:
        print("Not meal time!")
main()