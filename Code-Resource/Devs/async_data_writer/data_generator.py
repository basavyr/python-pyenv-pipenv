from random import randrange


class Data:
    def __init__(self, data_size, sub_array_size):
        self.datasize = data_size
        self.arrsize = sub_array_size

    def GenerateData(self):
        data = []
        for idx in range(self.datasize):
            current_data = [randrange(1, 10) for _ in range(self.arrsize)]
            data.append(current_data)

        try:
            assert len(data) > 0
        except AssertionError as err:
            return -1
        else:
            return data
