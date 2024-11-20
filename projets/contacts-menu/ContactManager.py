import json

from Contact import Contact

class ContactManager:

    def __init__(self):
        self.contacts = {}
        self.load()

    def addContact(self, contact):
        self.contacts[contact.id] = contact
        self.save()
    
    def delContact(self, contact):
        del self.contacts[contact.id]
        self.save()

    def getContact(self, id):
        return self.contacts[id]
    
    def getContacts(self):
        return self.contacts
    
    def clearContacts(self):
        self.contacts = {}
        self.save()
    
    def __get__(self, id):
        return self.contacts[id]
    
    def __set__(self, id, contact):
        self.contacts[id] = contact

    def __len__(self):
        return len(self.contacts)
    
    def __iter__(self):
        return iter(self.contacts)
    
    def __next__(self):
        return next(self.contacts)
    
    def __contains__(self, id):
        return id in self.contacts
    
    def save(self):
        with open('contacts.json', 'w') as f:
            json.dump(self.contacts, f, indent=4)

    def load(self):
        with open('contacts.json', 'r') as f:
            
            self.contacts = {int(contact["id"]):Contact.fromJson(contact) for contact in json.load(f)}
    