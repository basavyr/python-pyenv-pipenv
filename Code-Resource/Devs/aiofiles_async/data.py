from random import randrange


class Data:
    @staticmethod
    def GenerateData():
        data_size = randrange(1, 10)
        data = []
        for data_id in range(data_size):
            data.append([randrange(1, 100) for _ in range(randrange(1, 10))])

        return data
