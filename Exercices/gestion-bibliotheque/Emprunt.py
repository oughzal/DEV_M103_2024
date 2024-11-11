from datetime import date,timedelta
class Emprunte : 
    def __init__(self,a,l):
        self.adherent = a
        self.livre = l
        self.date_emprunt = date.today()
        self.date_retour = date().today()+timedelta(days=7)
    def islate (self):
        return self.date_retour < date.today()
    def duree (self):
        return self.date_retour - self.date_emprunt
    
     