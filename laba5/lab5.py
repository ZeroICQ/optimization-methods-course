

class Simplex:
    table = []
    m, n = 0, 0
    basis = []

    def __init__(self, source):
        self.m = len(source)
        self.n = len(source[0])
        self.table = [[.0 for __ in range(self.n + self.m - 1)] for _ in range(self.m)]
        self.basis = []
        for i in range(self.m):
            for j in range(len(self.table[0])):
                if j < self.n:
                    self.table[i][j] = source[i][j]
                else:
                    self.table[i][j] = 0
            if self.n + i < len(self.table[0]):
                self.table[i][self.n + i] = 1
                self.basis.append(self.n + i)
        self.n = len(self.table[0])

    def Calculate(self, result):
        while not self.IsItEnd():
            mainCol = self.findMainCol()
            mainRow = self.findMainRow(mainCol)
            self.basis[mainRow] = mainCol
            new_table = [[.0 for __ in range(self.n)] for _ in range(self.m)]
            for j in range(self.n):
                new_table[mainRow][j] = self.table[mainRow][j] / self.table[mainRow][mainCol]
            for i in range(self.m):
                if i == mainRow:
                    continue
                for j in range(self.n):
                    new_table[i][j] = self.table[i][j] - self.table[i][mainCol] * new_table[mainRow][j]
            self.table = new_table
        for i in range(len(result)):
            k = self.basis.index(i + 1)
            if k != -1:
                result[i] = self.table[k][0]
            else:
                result[i] = 0
        return self.table

    def IsItEnd(self):
        flag = True
        for j in range(self.n):
            if self.table[self.m - 1][j] < 0:
                flag = False
                break
        return flag


    def findMainCol(self):
        mainCol = 1
        for j in range(2, self.n):
            if self.table[self.m - 1][j] < self.table[self.m - 1][mainCol]:
                mainCol = j
        return mainCol

    def findMainRow(self, mainCol):
        mainRow = 0
        for i in range(self.m - 1):
            if self.table[i][mainCol] > 0:
                mainRow = i
                break
        for i in range(mainRow + 1, self.m - 1):
            if self.table[i][mainCol] > 0 and ((self.table[i][0] / self.table[i][mainCol]) < (self.table[mainRow][0] / self.table[mainRow][mainCol])):
                mainRow = i
        return mainRow


table = [[25, -3, 5],
         [30, -2, 5],
         [10, 1, 0],
         [6, 3, -8],
         [0, -6, -5]]


result = [.0, .0]
S = Simplex(table)
table_result = S.Calculate(result)

print("Решенная симплекс-таблица:")
print(table_result)

print("Решение:")
print("X[1] = " + str(result[0]))
print("X[2] = " + str(result[1]))