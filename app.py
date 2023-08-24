
from enum import Enum
class Actions (Enum):
    ADD =1
    PRINT =2
    DELETE =3
    SEARCH =4
    EXIT =5
    UPDATE =6
    INFO =6



DB = "cars.csv"
cars=[]
# add
# print
# delete
# search
# exit
# update
# info

# desplay menu for the user, return user selection.
def menu():
    while(True):
        for a in Actions:
            print (a.value,a.name)
        try:    
            res=int(input("please choose from the menu"))
            if res>6 or res<0:
                user_selection= Actions(res)
            if user_selection==Actions.ADD: add_car()
            if user_selection==Actions.EXIT: return
        except Exception as e: 
            print (e.mag)
            print("u r idiot - numbers only (0-6)")

def add_car():
    cars.append({"color":"red","model":"2010","type":"volvo"})


if __name__=='__main__':
    pass

