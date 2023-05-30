from settings import *
class User:
    def __init__(self):
        self.balance=0.00
        self.bet=0.00

    def place_bet(self):
        bet = self.bet_size
        self.balance -= bet
    def get_data(self):
        user_data={}
        user_data['balance'] = "{:.2f}".format(self.balance)

        return user_data