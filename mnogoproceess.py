import multiprocessing

class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        print('Получение данных')
        status, name, quantity = request
        if status == 'receipt':
            if name in self.data:
                print('Изменили данные')
    def process_shipment(self, request):
        status, name, quantity = request
        print('Отгрузка товара')
        if status == 'shipment':
            if name in self.data and self.data[name] > 0:
                self.data[name] -= quantity
                print('Товар отгружается')


    if __name__ == '__main__':
        req = multiprocessing.Process(target=process_request)

        requests = [('receipt', 'Bounty', 5), ('receipt', 'Печенье', 5), ('shipment', 'Конфета', 5),
                    ('shipment', 'Яблоко', 8)]

        print(req)
        req2 = multiprocessing.Process(target=process_shipment)
        print(req2)

