import threading
import time
from random import randint
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            beg = 50
            end = 500
            random_1 = randint(beg, end)
            self.balance += random_1
            print(f'Пополнение: {random_1}. Баланс: {self.balance}')
            if random_1 > 500:
                self.lock.acquire()
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                time.sleep(0.001)

    def take(self):
        for i in range(100):
            beg = 50
            end = 500
            random_2 = randint(beg, end)
            print(f'"Запрос на {random_2}"')
            if random_2 < self.balance:
                self.balance -= random_2
                print(f'Снятие: {random_2}. Баланс: {self.balance}')
                if random_2 > self.balance:
                    print(f"Запрос отклонён, недостаточно средств")
                time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')