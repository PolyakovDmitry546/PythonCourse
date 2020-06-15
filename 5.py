#1 задание
class car:
    def __init__(self, weight, engine_volume, power, cost):
        self.__weight = weight
        self.__engine_volume = engine_volume
        self.__power = power
        self.__cost = cost

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError

    @property
    def engine_volume(self):
        return self.__engine_volume

    @engine_volume.setter
    def engine_volume(self, engine_volume):
        if engine_volume > 0:
            self.__engine_volume = engine_volume
        else:
            raise ValueError

    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, power):
        if power > 0:
            self.__power = power
        else:
            raise ValueError

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    def bip(self):
        print('Bip!')

class truck(car):
    def __init__(self, weight, engine_volume, power, cost, trailer):
        super().__init__(weight, engine_volume, power, cost)
        self.__trailer = trailer

    @property
    def trailer(self):
        return self.__trailer

    @trailer.setter
    def trailer(self, trailer):
        self.__trailer = trailer

    def bip(self):
        print('Bip-Bip!')

    def unload(self):
        print("Truck unload")

car1 = car(1000, 3, 300, 3000)
truck1 = truck(5000, 5, 500, 8000, True)

print(car1.weight, car1.engine_volume, car1.power, car1.cost)
car1.bip()

print(truck1.weight, truck1.engine_volume, truck1.power, truck1.cost, truck1.trailer)
truck1.bip()

#2 задание

class mIterator:
    def __iter__(self):
        return self
    
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter * self.limit
        else:
            raise StopIteration

ite = mIterator(10)
for i in ite:
    print(i)

def mGenerator(value):
    while value > 2:
        value /= 2
        yield value

gen = mGenerator(7500)
for i in gen:
    print(i)

#3 задание

def f3(matrix):
    maxarea = 0
    if(matrix[0][0] == 1):
        maxarea = 1
    m1 = [[0] * len(matrix[i]) for i in range(len(matrix))]
    m2 = [[0] * len(matrix[i]) for i in range(len(matrix))]

    def issquare(i, j, level):
        if matrix[i][j] == 0:
            return False
        if level == 1:
            return matrix[i][j] == 1
        return m1[i][j] >= level and m2[i][j] >= level and issquare(i - 1, j - 1, level  - 1)
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                if j == 0:
                    m1[i][j] = matrix[i][j]
                else:
                    m1[i][j] = matrix[i][j] + m1[i][j-1]
                if i == 0:
                    m2[i][j] = matrix[i][j]
                else:
                    m2[i][j] = matrix[i][j] + m2[i-1][j]
                minarea = min(m1[i][j],m2[i][j])
                minarea *= minarea
                if maxarea < minarea and issquare(i,j,min(m1[i][j],m2[i][j])):
                    maxarea = minarea
    print(m1)
    print(m2)            
    return maxarea

print(f3([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]))
print(f3([[1]]))
print(f3([[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]]))
print(f3([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
print(f3([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))