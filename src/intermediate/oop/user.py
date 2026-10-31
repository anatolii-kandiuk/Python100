class User:
    """A class representing a user with name, age, and password."""
    def __init__(self, name, age, password=None):
        self.name = name
        self.age = age
        self.password = password
    
    def change_password(self, new_password):
        self.password = new_password   
        
    def get_info(self):
        return f"User Name: {self.name}, Age: {self.age}, Password: {self.password}" 