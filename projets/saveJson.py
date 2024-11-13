import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def toJson(self):
        return {"name":self.name,"age":self.age}
    @staticmethod
    def fromJson(d):
        return Person(d["name"],d["age"])
    
class PersonManager:
    def __init__(self):
        self.persons = []
        self.load()
    def addPerson(self,person):
        self.persons.append(person)
        self.save()

    def personList(self):
        for i,p in enumerate(self.persons):
            print(f"{i+1}. {p}")
        index = int(input("choose a person : "))
        return self.persons[index] if index<len(self.persons) else None   
    def removePerson(self):
        person = self.personList()
        if person:
            self.persons.remove(person)
            self.save()
    
    def __str__(self):
        return "\n".join([str(p) for p in self.persons])
    
    def save(self):
        data = [p.toJson() for p in self.persons]
        with open("persons.json","w") as f:
            json.dump(data,f)

    def load(self):
        with open("persons.json","r") as f:
            data = json.load(f)
            self.persons = [Person.fromJson(d) for d in data]
    
    def menu(self):
        while True:
            print("1. Add person")
            print("2. Remove person")
            print("3. List persons")
            print("4. Quit")
            choice = input("Enter your choice : ")
            if choice == "1":
                name = input("Enter name : ")
                age = int(input("Enter age : "))
                self.addPerson(Person(name,age))
            elif choice == "2":
                self.removePerson()
            elif choice == "3":
                print(self)
            elif choice == "4":
                break
            else:
                print("Invalid choice")
            

pm = PersonManager()
pm.menu()