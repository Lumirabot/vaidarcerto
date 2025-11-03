class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.balance = 0

    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, balance={self.balance})"