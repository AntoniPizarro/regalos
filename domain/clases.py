from resources.funciones import *

ITEM = {
    "data_base" : "regalos",
    "host" : '"mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/" + DB + "?retryWrites=true&w=majority"',
    "collection" : "items"
}
USER = {
    "data_base" : "regalos",
    "host" : '"mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/" + DB + "?retryWrites=true&w=majority"',
    "collection" : "users"
}
PRESENT = {
    "data_base" : "regalos",
    "host" : '"mongodb+srv://m001-student:m001-mongodb-basics@sandbox.4uubd.mongodb.net/" + DB + "?retryWrites=true&w=majority"',
    "collection" : "presents"
}

class Item:

    def __init__(self, name, description, price, image, link):
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.link = link
        self.id = check_id(ITEM["data_base"], ITEM["host"], ITEM["collection"], id_coder('0123456789abcdef', 6))
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def set_price(self, new_price):
        self.price = new_price
    
    def get_descripton(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_image(self):
        return self.image
    
    def payment_person(self, person_num):
        payment = self.price / person_num
        return payment
    
    def to_string(self):
        return f"ID: {self.get_id()}\nProducto: {self.get_name()}\nDescriptión: {self.get_descripton()}\nPrecio: {self.get_price()}\nEnlace: {self.get_link()}\n"

class User:

    def __init__(self, name, surname, phone, email, password, image, budget):
        self.properties = {
            "show_phone" : False,
            "show_email" : False
        }
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.password = password
        self.image = image
        self.budget = budget
        self.id = check_id(USER["data_base"], USER["host"], USER["collection"], id_coder('0123456789abcdef', 6))
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_phone(self):
        return self.phone
        
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    def set_password(self, new_password):
        self.password = new_password
    
    def get_image(self):
        return self.image
    
    def get_budget(self):
        return self.budget
    
    def set_propertie(self, propertie, value):
        self.properties[propertie] = value
    
    def to_string(self):
        return f"ID: {self.get_id()}\nNombre completo: {self.get_name()} {self.get_surname()}\nEmail: {self.get_email()}\nTeléfono: {self.get_phone()}\nPresupuesto: {self.get_budget()}\n"

class Present:

    def __init__(self, participants, present_to, items):
        self.participants = participants
        self.present_to = present_to
        self.items = items
        self.id = check_id(PRESENT["data_base"], PRESENT["host"], PRESENT["collection"], id_coder('0123456789abcdef', 6))
    
    def get_id(self):
        return self.id
    
    def get_budget(self):
        budget = 0.0
        for participant in self.participants:
            budget += participant.get_budget()
        return budget
    
    def get_participants(self):
        return self.participants
    
    def add_participant(self, new_participant):
        self.participants.append(new_participant)
    
    def remove_participant(self, participant):
        self.participants.remove(participant)
    
    def get_present_to(self):
        return self.present_to
    
    def get_items(self):
        return self.items
    
    def add_item(self, new_item):
        self.items.append(new_item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def budget_rest(self):
        prices = 0.0
        for item in self.get_items():
            prices += item.get_price()

        return self.get_budget() - prices    
    
    def to_string(self):
        res = f"ID: {self.get_id()}\nPresupuesto: {self.get_budget()}\nParticipantes: \n"
        for participant in self.participants:
            res += f"\t{participant.get_id()}\n"
        res += f"Cumpleañero: {self.get_present_to()}\nRegalos: \n"
        for item in self.items:
            res += f"\t{item.get_name()} -> {item.get_price()}\n"
        
        if self.budget_rest() >= 0:
            res += f"Sobrante: {self.budget_rest()}"
        else:
            res += f"Faltante: {-self.budget_rest()}"
        return res