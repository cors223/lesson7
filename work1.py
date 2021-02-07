class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for n in range(len(self.list_1)):
            for a in range(len(self.list_2[n])):
                matr[n][a] = self.list_1[n][a] + self.list_2[n][a]
        return str('\n'.join(['\t'.join([str(a) for a in n]) for n in matr]))
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for a in n]) for n in matr]))
my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])
print(my_matrix.__add__())
