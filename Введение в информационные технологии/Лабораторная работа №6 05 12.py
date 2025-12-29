'''class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        return self.password == password
    
user = UserAccount("Sasha", "@mail.ru", "parol123")

print(user.check_password("parol123"))
print(user.check_password("parol456"))

user.set_password("parol456")
print(user.check_password("parol456"))
print(user.check_password("parol123"))'''#1


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"{self.make} {self.model}"
    
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type   
    def get_info(self):
        return f"{super().get_info()},{self.fuel_type}"
    
machine = Vehicle("Machine", "Frame")
print(machine.get_info())  
modern = Car("Lightning", "Electro 1", "электричество")
print(modern.get_info())#2

