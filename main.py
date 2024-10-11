from typing import List
import math

size = int(input("Size: "))

massive = list(map(float, input("Massive: ").split()))

matrix = []

def ten_to_fraction(num:float):
    return num
    str_num = str(num)
    zeros = 0
    if "." in str_num:
        num = round(num, 3)
        str_num = str(num)
        zeros = len(str_num.split(".")[1])
        if zeros == 1 and str_num.split(".")[1] == "0":
            return num
    else:
        return str(num)
    num = int(num * 10**zeros)
    
    delit = 10**zeros

    for i in reversed(range(abs(num))):
        if num % (i+1) == 0 and delit % (i+1) == 0:
            num = num // (i+1)
            delit = delit // (i+1)
    
    return f"{num}/{delit}"

def create_matrix(massive: list):
    index = 0
    for y in range(size):
        matrix.append([0 for i in range(size)])
        for x in range(size):
            matrix[y][x] = massive[index]
            index += 1
def create_matrix_from_matrix(matrix: List[list], ind_x: int, ind_y: int, minor:bool=True):
    if len(matrix) == 2 and minor:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    elif len(matrix) == 2:
        return matrix[-ind_y-1][-ind_x-1]
    new_matrix = []
    for y in range(0, len(matrix)):
        if y == ind_y:
            continue
        row = []
        for x in range(len(matrix)):
            if x == ind_x:
                continue
            row.append(matrix[y][x])
        new_matrix.append(row)
    if len(new_matrix) == 2 and minor:
        return new_matrix[0][0] * new_matrix[1][1] - new_matrix[1][0] * new_matrix[0][1]
    # elif len(new_matrix) == 2:
    #     return new_matrix[-ind_y-1][-ind_x-1]
    # print(sum([(-1)**i * new_matrix[0][i] * create_matrix_from_matrix(new_matrix, i, 0, minor) for i in range(len(new_matrix))]))
    return sum([(-1)**i * new_matrix[0][i] * create_matrix_from_matrix(new_matrix, i, 0, minor) for i in range(len(new_matrix))])
        
def transp(matrix: List[list]):
    new_matrix = []
    for y in range(len(matrix)):
        row = []
        for x in range(len(matrix)):
            row.append(matrix[x][y])
        new_matrix.append(row)
    return new_matrix

create_matrix(massive)

action = int(input("Det: 1;\nUnion: 2;\nT: 3;\nInverse: 4;\n-----------------\nAction: "))

def determinant(matrix):
    if len(matrix) != 2:
        return sum([matrix[0][i] * (-1)**i * create_matrix_from_matrix(matrix, i, 0) for i in range(size)])
    else:
        return create_matrix_from_matrix(matrix, 0, 0)

if action == 1:
    print(determinant(matrix))

elif action == 2:
    answer = []
    matrix = transp(matrix)
    for j in range(size):
        answer.append([(-1)**(i+j) * create_matrix_from_matrix(matrix, i, j, False) for i in range(size)])
    for y in range(size):
        for x in range(size):
            answer[y][x] = ten_to_fraction(answer[y][x])

    print("Matrix: ")
    print('\n'.join(['\t'.join(map(str, row)) for row in answer]))

elif action == 3:
    answer = transp(matrix)
    for y in range(size):
        for x in range(size):
            answer[y][x] = ten_to_fraction(answer[y][x])

    print("Matrix: ")
    print('\n'.join(['\t'.join(map(str, row)) for row in answer]))

elif action == 4:
    det = determinant(matrix)
    print("Determinant: ",det)
    answer = []
    matrix = transp(matrix)
    for j in range(size):
        answer.append([(-1)**(i+j) * create_matrix_from_matrix(matrix, i, j, False) for i in range(size)])

    for y in range(size):
        for x in range(size):
            answer[y][x] *= 1/det
            answer[y][x] = ten_to_fraction(answer[y][x])


    print("Matrix: ")
    print('\n'.join(['\t'.join(map(str, row)) for row in answer]))