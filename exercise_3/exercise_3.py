import json

class Exercise3:
    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            self.data = json.load(file)

    def get_username(self):
        return self.data['username']

    def get_time_remaining(self):
        return self.data['time_remaining']

    def add_hour(self):
        self.data['time_remaining'] += 60

    def get_items(self):
        return list(self.data['shopping_cart'].keys())

    def get_total(self):
        return sum(self.data['shopping_cart'].values())
