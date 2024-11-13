from Contact import Contact
import json,os
class ContactManager:
    def save(self):
        contacts = []
        for c in self.contacts:
            contacts.append(c.toJson())
        with open("contacts.json","w") as file:
            json.dump(contacts,file)

    def load(self):
        if not os.path.exists("contacts.json"):
            return
        with open("contacts.json","r") as file:
            data = json.load(file)
            for c in data:
                self.contacts.append(Contact.fromJson(c))
    
    def __init__(self):
        self.contacts = []
        self.load()

    def add(self,contact):
        if isinstance(contact,Contact):
            self.contacts.append(contact)
            self.save()
    
    def remove(self,contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            self.save()
    
    def findByName(self,name):
        for c in self.contacts:
            if c.nom == name:
                return c
        # return None
    
    def findByTel(self,tel):
        for c in self.contacts:
            if c.tel == tel:
                return c
    
    def afficher(self):
        for c in self.contacts:
            print(c)
    
    