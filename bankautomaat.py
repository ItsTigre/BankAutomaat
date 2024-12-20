class bankaccount:
    def __init__(self, account_id, pin_code,holder_name, balance=0):
        self.account_id = account_id
        self.pin_code = pin_code
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Stort bedrag moet meer dan 0 zijn.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Onvoldoende Saldo")
        else:
            print("Afhaal bedrag moet meer dan 0 zijn.")