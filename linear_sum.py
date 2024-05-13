import time

import numpy as np
from scipy.optimize import linear_sum_assignment


def input_case1 (): 
    n = 500
    cost_matrix = np.zeros((n, n), dtype=int)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                cost_matrix[i-1][j-1] = 10 * (i + j) + abs(i - j - 1)
            else:
                cost_matrix[i-1][j-1] = i + j

    return cost_matrix

def input_case2 () :
    file_path = r'C:\Users\IvoAg\OneDrive\Área de Trabalho\Repositorios\Hungarian_Algorithm\test_cases\K10x10.txt'
    n = 10  
    cost_matrix = np.full((n, n), np.inf)  


    with open(file_path, 'r') as file:
        for line in file:
            u, v, cost = map(int, line.split())
            if u % 2 == 1:  
                i = (u - 1) // 2
                j = (v - 2) // 2
                cost_matrix[i][j] = cost

    return cost_matrix


start_time = time.time()

# Inputs
# cost_matrix = input_case1()
cost_matrix = input_case2()



row_ind, col_ind = linear_sum_assignment(cost_matrix)
total_cost = cost_matrix[row_ind, col_ind].sum()

# print("Índices de linhas:", row_ind)
# print("Índices de colunas:", col_ind)
print("Custo total do emparelhamento ótimo:", total_cost)
end_time = time.time()
duration = end_time - start_time
print(f"Duração {duration:.4f}")






