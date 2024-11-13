class Contact:
    cmp = 0
    def __init__(self,nom,tel):
        Contact.cmp +=  1
        self.id = Contact.cmp
        self.nom = nom
        self.tel = tel

    def __str__(self):
        return f"{self.nom} ({self.tel})"
    
    def toJson(self):
        return {
            "id" : self.id,
            "nom" : self.nom,
            "tel" : self.tel
        }
    
    @classmethod
    def fromJson(cls,data):
        contact = Contact(data["nom"],data["tel"])
        contact.id = data["id"]
        return contact