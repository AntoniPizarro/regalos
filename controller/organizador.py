class Organizer:

    def __init__(self):
        self.users = []
        self.presents = []
        self.items = []
    
    def get_data(self, users = [], presents = [], items=[]):
        for user in users:
            if user not in self.users:
                self.users.append(user)
        for present in presents:
            if user not in self.users:
                self.presents.append(present)
        for item in items:
            if user not in self.users:
                self.items.append(item)