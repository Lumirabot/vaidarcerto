import unittest
from src.cogs.economy.work import work
from src.cogs.economy.study import study
from src.cogs.economy.transfer import transfer
from src.cogs.economy.daily import daily
from src.cogs.economy.rob import rob
from src.cogs.economy.fish import fish
from src.models.user import User

class TestEconomyFunctions(unittest.TestCase):

    def setUp(self):
        self.user1 = User(id=1, name="User1", balance=100)
        self.user2 = User(id=2, name="User2", balance=50)

    def test_work(self):
        initial_balance = self.user1.balance
        work(self.user1)
        self.assertGreater(self.user1.balance, initial_balance)

    def test_study(self):
        initial_balance = self.user1.balance
        study(self.user1)
        self.assertGreater(self.user1.balance, initial_balance)

    def test_transfer(self):
        initial_balance_user1 = self.user1.balance
        initial_balance_user2 = self.user2.balance
        transfer(self.user1, self.user2, 20)
        self.assertEqual(self.user1.balance, initial_balance_user1 - 20)
        self.assertEqual(self.user2.balance, initial_balance_user2 + 20)

    def test_daily(self):
        initial_balance = self.user1.balance
        daily(self.user1)
        self.assertGreater(self.user1.balance, initial_balance)

    def test_rob(self):
        initial_balance_user1 = self.user1.balance
        initial_balance_user2 = self.user2.balance
        rob(self.user1, self.user2)
        self.assertGreater(self.user1.balance, initial_balance_user1)
        self.assertLess(self.user2.balance, initial_balance_user2)

    def test_fish(self):
        initial_balance = self.user1.balance
        fish(self.user1)
        self.assertGreater(self.user1.balance, initial_balance)

if __name__ == '__main__':
    unittest.main()