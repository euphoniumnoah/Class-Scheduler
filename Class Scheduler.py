import os
import json
import numpy as np
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir,"Classes.json")

current_day = datetime.now().strftime("%A")
current_time = datetime.now().strftime("%H%M")

Classes = {}

class Class:
    def __init__(self, name, loc, days=None, times=None):
        self.name = name
        self.loc = loc
        self.days = [] if days is None else list(days)
        self.times = [] if times is None else list (times)

    def add_class():

        print()

        name = input("Enter name of class: ")

        loc = input("Enter location of class: ")

        newclass = Class(name, loc)
        Classes[name] = newclass

        days = []
        while True:
            day = input("Add a day such as 'Monday', type continue when done: ")
            if day.lower() == "continue":
                break
            else:
                newclass.days.append(day)

        times = []
        while True:
            time1 = input("Add the start time in military format. (e.g. 1307 = 1:07): ")
            time2 = input("Add the end time in military format. (e.g. 1307 = 1:07): ")
            print()
            newclass.times.append(time1)
            newclass.times.append(time2)
            
    def remove_class(_dict, name):

        if name in _dict:
            del _dict[name]
            print()
            print(f"Class {name} removed.")
            print()
        else:
            print()
            print(f"Class {name} not found.")
            print()

    def show(self):
        print()
        print(f"{self.name}")
        print(f"is in {self.loc}")
        print(f"on {self.days}")
        print(f"from {self.times[0]} to {self.times[1]}")

    def time():

        names = []
        timez = []
        locations = []
        
        for on in Classes.values():
            for day in on.days:
                if day == current_day:
                    names.append(on.name)
                    timez.append(on.times[0])
                    locations.append(on.loc)

        index = 77
        want = "0"
        sort = np.sort(timez)
        check = False
        
        for seg in sort:
            if int(seg) > int(current_time) and int(seg) > int(want):
                want = seg
                check = True
            
        for ind, value in enumerate(timez):
            if want == value:
                index = ind

        if check == False:
            print()
            print("There are no more classes for the day.")
            print()
        else:
            i = datetime.strptime(timez[index],"%H%M")
            o = i.strftime("%I:%M %p")  
            print()
            print("Your next class is")
            print(names[index])
            print("and will be in the location")
            print(locations[index])
            print("at the time")
            print(o)
            print()

    def to_dict(self):
        return {
            "name": self.name,
            "loc": self.loc,
            "days": self.days,
            "times": self.times
            }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["loc"], days=list(data.get("days",[])), times=list(data.get("times",[])))

    @classmethod
    def save_classes(cls, Classes, filename="Classes.json"):
        data = {name: clas.to_dict() for name, clas in Classes.items()}
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_classes(cls):
        if not os.path.exists(json_path):
            with open(json_path, "w") as f:
                json.dump({}, f)
        with open(json_path, "r") as f:
            data = json.load(f)
        Classes = {name:cls.from_dict(clas_data) for name, clas_data in data.items()}
        return Classes

Classes = Class.load_classes()

while True:
    command = input("Welcome to the class scheduler,\n'add' to add a class\n'remove' to remove a class\n'list' to list classes\n'next' to see your next class\n'exit' to close the scheduler. ")

    if command.lower() == "add" or command.lower() == "'add'": # Adds a class to the list
        Class.add_class()

    elif command.lower() == "remove" or command.lower() == "'remove'": # Removes a class from the list
        print()
        text = input("What is the name of the class? ")
        Class.remove_class(Classes, text)
        
    elif command.lower() == "list" or command.lower() == "'list'": # Lists all classes
        for on in Classes.values():
            on.show()
        print()
        
    elif command.lower() == "next" or command.lower() == "'next'": # Shows your next class
        Class.time() 
        
    elif command.lower() == "exit" or command.lower() == "'exit'": # Save and exit
        Class.save_classes(Classes)
        break

exit()

    # Class Scheduler by Noah Palmer


