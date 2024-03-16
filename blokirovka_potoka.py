import threading


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit_task(self, account, amount):
        for i in range(5):
            account.deposit_task(amount)
        with self.lock:
            print(f'блок через функцию deposit {amount} ')
            self.balance += amount

    def withdraw_task(self, account, amount):
        for i in range(5):
            account.withdraw_task(amount)
        with self.lock:
            if self.balance >= amount:
                print(f'блок через функцию withdraw {amount}')
                self.balance -= amount
            else:
                print('block with')

    def bank_acc_operation(self, account, amount, is_deposit):
        if is_deposit:
            account.deposit_task(amount)
        else:
            account.withdraw_task(amount)



account = BankAccount(balance=100)
threads = []
for _ in range(5):
    thread = threading.Thread(args=(account, 10, True))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print(f'ваш баланс: {account.balance}')
