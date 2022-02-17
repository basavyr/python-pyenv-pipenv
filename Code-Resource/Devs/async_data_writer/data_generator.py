from random import randrange


class Data:
    def __init__(self):
        self.datasize = randrange(1, 10)
        self.arrsize = randrange(1, 100)

    def GenerateData(self):
        data = []
        for idx in range(self.datasize):
            current_data = [randrange(1, 100) for _ in range(self.arrsize)]
            data.append(current_data)

        try:
            assert len(data) > 0
        except AssertionError as err:
            return -1
        else:
            return data
