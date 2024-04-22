import multiprocessing

class WarehouseManager(multiprocessing.Process):
    def __init__(self):
        super().__init__()
        self.data = {}

    def process_request(self, request):
        print('Получение данных')
        status, name, quantity = request
        if status == 'receipt':
            if name in self.data:
                print('Изменили данные')
                self.data[name] += quantity
                print(f"Добавлено {quantity} единиц товара {name}")
            else:
                self.data[name] = quantity
                print(f"Добавлен товар {name} в количестве {quantity}")
    def process_shipment(self, request):
        status, name, quantity = request
        print('Отгрузка товара')
        if status == 'shipment':
            if name in self.data and self.data[name] >= quantity:
                self.data[name] -= quantity
                print(f"Отгружено {quantity} единиц товара {name}")
            else:
                print(f"Невозможно отгрузить {quantity} единиц товара {name}")

    def run(self, requests):
        for request in requests:
            process = multiprocessing.Process(target=self.process_request, args=(request,))
            process.start()
            process.join()


if __name__ == '__main__':



    requests = [('receipt', 'Bounty', 5), ('receipt', 'Печенье', 5), ('shipment', 'Конфета', 5),
                    ('shipment', 'Яблоко', 8)]

    manager = WarehouseManager()
    manager.run(requests)
    print(manager.data)

    manager2 = WarehouseManager()
    manager2.run(requests)
    print(manager2.data)
