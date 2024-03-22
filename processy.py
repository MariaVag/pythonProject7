import threading
import time
from queue import Queue



class Table:
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, table):
        self.table = table
        self.queue = Queue()

    def customer_arrival(self):
        print(f'Гость №{self.number} прибыл')
        while self.table.is_busy:
            time.sleep(1)
        print(f"Посетитель номер {self.number} сел за стол {self.table.number} (начало обслуживания)")
        time.sleep(5)
        print(f"Посетитель номер {self.number} покушал и ушёл (конец обслуживания)")
        self.table.is_busy = False

    def serve_customer(self, customer):
        self.table.is_busy = True
        print(f'Гость №{self.number} сел за стол №{self.table.number}')
        time.sleep(5)
        print(f'Гость №{self.number} обслужан и ушел')



class Customer(threading.Thread):
    def __init__(self, number, table):
        super().__init__()
        self.number = number
        self.table = table

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 10:
            free_table = None
            for table in self.tables:
                if not table.is_busy:
                    free_table = table
                    break
                if free_table:
                    customer_thread = Customer(customer_number, free_table)
                    customer_thread.start()
                    customer_number += 1
                else:
                    print(f'Посетитель №{customer_number} ожиадет свободный стол')
            self.queue.put(customer_number)
            customer_number += 1

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=Cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()

