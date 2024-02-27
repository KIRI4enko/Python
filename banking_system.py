'''
Банковская система(OOП)
Banking system(OOP)
'''


class Client:
    unique_id = 1
    client_base = []

    def __init__(self, full_name: str, data_vk, size_vk: int, percent_vk: int):
        self._id = Client.unique_id
        self._full_name = full_name
        self._data_vk = data_vk
        self._size_vk = size_vk
        self._percent_vk = percent_vk
        Client.unique_id += 1
        Client.client_base.append(self)

    def __str__(self):
        return f'{self._id}\t{self._full_name}\t{self._data_vk}\t{self._size_vk}\t{self._percent_vk}'


class Bank:
    def __init__(self):
        self._client_base = Client.client_base

    def __str__(self):
        return '\n'.join([Client.__str__(client) for client in self._client_base])

    def showByMoney(self, money):
        for client in self._client_base:
            if client._size_vk > money:
                print(client)

    def showByProc(self, proc):
        for client in self._client_base:
            if client._percent_vk > proc:
                print(client)

    def showByCode(self, id):
        for client in self._client_base:
            if client._id == id:
                print(client)
                return


bank = Bank()
c1 = Client('Zoya', '123', 20000, 15)
c2 = Client('Ivan', '777', 50000, 13)
c3 = Client('Joes', '076', 1337, 1)
print(bank)
bank.showByMoney(10000)
print('=' * 100)
bank.showByCode(3)
print('=' * 100)
bank.showByProc(14)
