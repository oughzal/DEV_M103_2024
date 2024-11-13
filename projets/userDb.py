import sqlite3

class User:
    id = 0
    def __init__(self,nom,prenom):
        User.id += 1
        self.id = User.id
        self.nom = nom
        self.prenom = prenom

class UserDB:
    filename = "users.db"
    def __init__(self):
        self.users = []
        self.load()
    def load(self):
        def load(self):
            conn = sqlite3.connect(self.filename)
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT)")
            cursor.execute("SELECT id, nom, prenom FROM user")
            rows = cursor.fetchall()
            for row in rows:
                user = User(row[1], row[2])
                user.id = row[0]
                self.users.append(user)
            conn.close()

    
        