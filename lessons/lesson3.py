class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self._balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        return 'wrong password'



Bekzhan = BankAccount('Bekzhan', 10000, 'qwerty')

print(Bekzhan.get_balance('qwerty'))
print(Bekzhan._BankAccount__password)
print(dir(Bekzhan))

