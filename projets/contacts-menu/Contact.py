class Contact:
    contactList = {}
    cmp = 0
    def __init__(self,name,tel):
        Contact.cmp += 1
        self.id = Contact.cmp
        self.name = name
        self.tel = tel
        Contact.contactList[self.id] = self

    def __del__(self):
        del Contact.contactList[self.id]

    @classmethod
    def fromJson(cls,json):
        contact = Contact(json["name"],json["tel"])
        contact.id = json["id"]
        return contact
    