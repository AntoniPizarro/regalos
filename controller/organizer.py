from bd import Data_Base as DB
from funcs import *
from classes import *

class Organizer:

    def __init__(self):
        '''self.presents = []
        self.users = []
        self.items = []

        for present in DB.get_data("presents"):
            present_obj = Present(present["present_to"], present["id"])

            for user in present["participantes"]:
                present_obj.add_user(user)

            for item in present["items"]:
                present_obj.add_item(item)
            
            self.presents.append(present_obj)

        for user in DB.get_data("users"):
            user_obj = User(user["name"], user["surname"], user["phone"], user["email"], user["password"], user["id"], user["properties"])
            
            for key in user["budget"]:
                user_obj.add_budget(key, user["budget"][key])
                
                self.users.append(user_obj)

        for item in DB.get_data("items"):
            item_obj = Item(item["name"], item["description"], item["price"], item["link"], item["id"])
            
            self.items.append(item_obj)'''

        self.refresh_data()
    
    def get_presents(self):
        return self.presents
    
    def get_users(self):
        return self.users
    
    def get_items(self):
        return self.items
    
    def refresh_data(self):
        self.presents = []
        self.users = []
        self.items = []

        for present in DB.get_data("presents"):
            present_obj = Present(present["present_to"], present["organizer"], present["id"])
            for user in present["participants"]:
                present_obj.add_participant(user)

            for item in present["items"]:
                present_obj.add_item(item)
            
            self.presents.append(present_obj)

        for user in DB.get_data("users"):
            user_obj = User(user["name"], user["surname"], user["phone"], user["email"], user["password"], user["id"], user["properties"])
            
            for key in user["budget"]:
                user_obj.add_budget(key, user["budget"][key])
                
            self.users.append(user_obj)

        for item in DB.get_data("items"):
            item_obj = Item(item["name"], item["description"], item["price"], item["link"], item["id"])
            
            self.items.append(item_obj)
    
    def new_present(self, present_to, user_id):
        present = Present(present_to, user_id)
        present.add_participant(user_id)
        DB.add_data("presents", present.to_dict())
        checked = DB.get_data("presents", {"id" : present.get_id()})
        if not checked:
            print("Error when adding new present!")
        
        self.refresh_data()
    
    def get_present(self, present_id) -> Present:
        for present in self.get_presents():
            if present.get_id() == present_id:
                return present
    
    def del_present(self, present_id):
        for present in self.get_present():
            if present.get_id() == present_id:
                DB.delete_data("presents", {"id" : present.get_id()})

        self.refresh_data()
    
    def new_user(self, name, surname, phone, email, password):
        user = User(name, surname, phone, email, encrypt_password(password))
        DB.add_data("users", user.to_dict())
        checked = DB.get_data("users", {"id" : user.get_id()})
        if not checked:
            print("Error when adding new user!")

        self.refresh_data()
    
    def get_user(self, user_id) -> User:
        for user in self.get_users():
            if user.get_id() == user_id:
                return user
    
    def del_user(self, user_id):
        for user in self.get_users():
            if user.get_id() == user_id:
                DB.delete_data("users", {"id" : user.get_id()})

        self.refresh_data()

    def new_item(self, name, description, price, link):
        item = Item(name, description, price, link)
        DB.add_data("items", item.to_dict())
        checked = DB.get_data("items", {"id" : item.get_id()})
        if not checked:
            print("Error when adding new item!")

        self.refresh_data()
    
    def get_item(self, item_id) -> Item:
        for item in self.get_items():
            if item.get_id() == item_id:
                return item
    
    def del_item(self, item_id):
        for item in self.get_items():
            if item.get_id() == item_id:
                DB.delete_data("items", {"id" : item.get_id()})

        self.refresh_data()
    
    def new_user_budget(self, user_id, present_id, budget):
        user = self.get_participant(user_id)
        present = self.get_present(present_id)
        user.add_budget(present_id, budget)
        present.add_user(user.get_id())

        self.db_refresh_user(user)
        self.db_refresh_present(present)
    
    def configure_user(self, user_id, propertie, value):
        user = self.get_participant(user_id)
        user.set_propertie(propertie, value)

        self.db_refresh_user(user)
    
    def add_participant(self, user_id, present_id):
        present = self.get_present(present_id)
        present.add_participant(user_id)
        self.db_refresh_present(present)
        
    def eliminate_participant(self, user_id, present_id):
        present = self.get_present(present_id)
        present.del_participant(user_id)
        self.db_refresh_present(present)

    def add_item(self, item_id, present_id):
        present = self.get_present(present_id)
        present.add_item(item_id)
        self.db_refresh_present(present)

    def eliminate_item(self, item_id, present_id):
        present = self.get_present(present_id)
        present.del_item(item_id)
        self.db_refresh_present(present)

    def get_present_with_participant(self, user_id):
        res = []
        for present in self.get_presents():
            for id in present.get_participants():
                if id == user_id and present not in res:
                    res.append(present)
        
        return res

    @staticmethod
    def db_refresh_user(user: User):
        DB.update_data("users", user.to_dict(), {"id", user.get_id()})
    
    @staticmethod
    def db_refresh_present(present: Present):
        DB.update_data("presents", present.to_dict(), {"id", present.get_id()})
    
    @staticmethod
    def db_refresh_item(item: Item):
        DB.update_data("items", item.to_dict(), {"id", item.get_id()})