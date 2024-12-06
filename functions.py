def several_zeros():
    return [0] * 10
# print(several_zeros()) 

def several_zeros_custom(nb_zeros=10):
    return [0] * nb_zeros

# print(several_zeros_custom(5)) 
# print(several_zeros_custom(12)) 
# print(several_zeros_custom())   

def matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]

result = matrix(2, 3)

# print(result)         
# print(result[1][2])    
# print(result[0])      

class Matrix:
    def __init__(self, rows, cols):
        self.__matrix = [[0] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.__matrix[row][col]
        else:
            raise IndexError("Position hors limites de la matrice.")

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.__matrix == other.__matrix


# m1 = Matrix(2, 3)
# m2 = Matrix(2, 3)

# print(m1.get_value(1, 2)) 
# print(m1 == m2)          

# m2._Matrix__matrix[1][2] = 1
# print(m1 == m2)

def my_sort(my_list: [int]) -> [int]:

    sorted_list = my_list[:]

    n = len(sorted_list)
    for i in range(n):
        for j in range(n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    
    return sorted_list

# if __name__ == "__main__":
#     unsorted_list = [64, 34, 25, 12, 22, 11, 90]
#     sorted_list = my_sort(unsorted_list)
#     print("Liste originale :", unsorted_list)
#     print("Liste triée :", sorted_list)
