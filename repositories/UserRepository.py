from infraestructure.adapters.SQLiteAdapter import SQLiteAdapter

class UserRepository:
    def __init__(self):
        self.adapter = SQLiteAdapter()

    def saveUser(self, user):
        query = '''INSERT INTO users (name, email, password) VALUES (?,?,?)'''
        parameters = (user.name,user.email, user.password)
        try:
            self.adapter.excecuteQuery(query, parameters)
            return True
        except:
            return False
