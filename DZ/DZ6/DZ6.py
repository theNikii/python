#Нужно реализовать класс Account, который отражает абстракцию базового
#поведения банковского аккаунта:
#● создать банковский аккаунт с параметрами: имя; стартовый баланс с
#которым зарегистрирован аккаунт; история операций*;
#● реализовать два метода, которые позволяют положить деньги на счёт
#или снять деньги со счёта;
#● продумать, как можно хранить историю поступления или снятия
#денег, чтобы с ней было удобно работать*.
class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.history = []
        self.history.append(f"Баланс: {balance}")
    def take_off(self,take_off_money):
        self.balance -= take_off_money
        self.history.append(f"Cнято {take_off_money}")
    def put(self,put_money):
        self.balance += put_money
        self.history.append(f"Зачислено {put_money} ") 


person = Account("Nikita",100)
person.take_off(20)
person.put(50)
print(person.history)
