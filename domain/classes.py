from pprint import pprint
from funcs import *
from bd import Data_Base as DB

class Present:

    def __init__(self, present_to, organizer, id=None):
        self.present_to = present_to
        self.organizer = organizer

        if id == None:
            id_lenght = 6
            id_chars = "0123456789abcdefghijklmnopqrstuvwxyz_"
            id = id_generaor(id_lenght, id_chars)
            while not check_id(id, DB.get_data("presents")):
                id = id_generaor(id_lenght, id_chars)

        self.id = id
        self.participants = []
        self.items = []

    def get_id(self):
        return self.id

    def get_anfitrion(self):
        return self.present_to
    
    def get_organizer(self):
        return self.organizer

    def get_items(self):
        return self.items

    def get_participants(self):
        return self.participants

    def add_item(self, item_id):
        self.items.append(item_id)

    def add_participant(self, user_id):
        self.participants.append(user_id)
    
    def del_item(self, item_id):
        for item in self.items:
            if item["id"] == item_id:
                self.items.remove(item)
                return True
                
        return False
    
    def del_participant(self, user_id):
        for user in self.participants:
            if user["id"] == user_id:
                self.participants.remove(user)
                return True
                
        return False
    
    def total_to_pay(self):
        items = []
        total = 0.0
        for item_id in self.items:
            items.append(DB.get_data("items", {"id" : item_id}))
        
        for item in items:
            item_obj = Item(item["name"], item["description"], item["price"], item["link"])
            total += item_obj.get_price()
        del item_obj

        return total
    
    def to_dict(self):
        data = {
            "participants" : self.get_participants(),
            "present_to" : self.get_anfitrion(),
            "items" : self.get_items(),
            "organizer" : self.get_organizer(),
            "id" : self.get_id()
        }
        return data

class Item:

    def __init__(self, name, description, price, link, id=None):
        self.name = name
        self.description = description
        self.price = price
        self.link = link

        if id == None:
            id_lenght = 10
            id_chars = "0123456789abcdefghijklmnopqrstuvwxyz_"
            id = id_generaor(id_lenght, id_chars)
            while not check_id(id, DB.get_data("items")):
                id = id_generaor(id_lenght, id_chars)

        self.id = id
    
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    def get_price(self):
        return self.price
    
    def get_link(self):
        return self.link

    def set_price(self, new_price):
        self.price = new_price

    def set_link(self, new_link):
        self.link = new_link

    def to_dict(self):
        data = {
            "name" : self.get_name(),
            "description" : self.get_description(),
            "price" : self.get_price(),
            "link" : self.get_link(),
            "id" : self.get_id()
        }

        return data

class User:

    def __init__(self, name, surname, phone, email, password, id=None, properties={"show_email" : False, "show_phone" : False}):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.password = password # Encrypted
        self.budget = {}
        self.properties = properties

        if id == None:
            id_lenght = 8
            id_chars = "0123456789abcdefghijklmnopqrstuvwxyz_"
            id = id_generaor(id_lenght, id_chars)
            while not check_id(id, DB.get_data("users")):
                id = id_generaor(id_lenght, id_chars)

        self.id = id
    
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
    
    def get_budget_list(self):
        return self.budget
    
    def add_budget(self, present_id, budget):
        self.budget[present_id] = budget

    def get_total_budget(self):
        total = 0.0
        for present_id in self.get_budget_list():
            total += self.get_budget_list()[present_id]

        return total
    
    def set_budget(self, present_id, new_budget):
        self.budget[present_id] = new_budget

    def del_budget(self, present_id):
        self.budget.pop(present_id)

    def get_properties(self):
        return self.properties
    
    def set_propertie(self, propertie, value):
        if propertie in self.get_properties():
            self.properties[propertie] = value

    def to_dict(self):
        data = {
            "name" : self.get_name(),
            "surname" : self.get_surname(),
            "phone" : self.get_phone(),
            "email" : self.get_email(),
            "password" : self.get_password(),
            "budget" : self.get_budget_list(),
            "properties" : self.get_properties(),
            "id" : self.get_id()
        }

        return data