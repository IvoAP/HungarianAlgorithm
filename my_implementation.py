import time

import numpy as np


def input_case1():
    n = 500
    cost_matrix = np.zeros((n, n), dtype=int)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                cost_matrix[i-1][j-1] = 10 * (i + j) + abs(i - j - 1)
            else:
                cost_matrix[i-1][j-1] = i + j
    return cost_matrix

def input_case2():
    data = [
        [1, 2, 31], [1, 4, 683], [1, 6, 464], [1, 8, 958], [1, 10, 92], [1, 12, 496], [1, 14, 528], [1, 16, 167], [1, 18, 534], [1, 20, 540],
        [3, 2, 956], [3, 4, 625], [3, 6, 457], [3, 8, 63], [3, 10, 204], [3, 12, 799], [3, 14, 731], [3, 16, 88], [3, 18, 966], [3, 20, 198],
        [5, 2, 924], [5, 4, 842], [5, 6, 107], [5, 8, 390], [5, 10, 387], [5, 12, 714], [5, 14, 842], [5, 16, 77], [5, 18, 931], [5, 20, 793],
        [7, 2, 443], [7, 4, 954], [7, 6, 358], [7, 8, 722], [7, 10, 620], [7, 12, 918], [7, 14, 494], [7, 16, 684], [7, 18, 889], [7, 20, 896],
        [9, 2, 694], [9, 4, 471], [9, 6, 807], [9, 8, 238], [9, 10, 686], [9, 12, 481], [9, 14, 250], [9, 16, 319], [9, 18, 338], [9, 20, 462],
        [11, 2, 210], [11, 4, 566], [11, 6, 760], [11, 8, 393], [11, 10, 504], [11, 12, 322], [11, 14, 56], [11, 16, 245], [11, 18, 553], [11, 20, 719],
        [13, 2, 967], [13, 4, 434], [13, 6, 49], [13, 8, 571], [13, 10, 876], [13, 12, 786], [13, 14, 364], [13, 16, 389], [13, 18, 560], [13, 20, 872],
        [15, 2, 323], [15, 4, 33], [15, 6, 250], [15, 8, 386], [15, 10, 587], [15, 12, 825], [15, 14, 315], [15, 16, 298], [15, 18, 621], [15, 20, 416],
        [17, 2, 552], [17, 4, 54], [17, 6, 445], [17, 8, 161], [17, 10, 64], [17, 12, 721], [17, 14, 916], [17, 16, 68], [17, 18, 293], [17, 20, 185],
        [19, 2, 245], [19, 4, 140], [19, 6, 390], [19, 8, 722], [19, 10, 519], [19, 12, 407], [19, 14, 240], [19, 16, 44], [19, 18, 154], [19, 20, 408]
    ]

    num_vertices = 10
    cost_matrix = np.full((num_vertices, num_vertices), np.inf)
    for i, j, cost in data:
        i_index = (i - 1) // 2
        j_index = (j - 2) // 2
        cost_matrix[i_index, j_index] = min(cost_matrix[i_index, j_index], cost)  # Handle possible duplicate entries
    
    return cost_matrix

def input_case3():
    data = [
        [0, 0, 4],  # Elemento na linha 0, coluna 0, custo 4
        [1, 0, 2],  # Elemento na linha 1, coluna 0, custo 2
        [2, 0, 3],  # Elemento na linha 2, coluna 0, custo 3
        [0, 1, 1],  # Elemento na linha 0, coluna 1, custo 1
        [1, 1, 0],  # Elemento na linha 1, coluna 1, custo 0
        [2, 1, 2],  # Elemento na linha 2, coluna 1, custo 2
        [0, 2, 3],  # Elemento na linha 0, coluna 2, custo 3
        [1, 2, 5],  # Elemento na linha 1, coluna 2, custo 5
        [2, 2, 2]   # Elemento na linha 2, coluna 2, custo 2
    ]

    num_vertices = 3
    cost_matrix = np.full((num_vertices, num_vertices), np.inf)  # Inicia a matriz com infinito

    # Preenche a matriz de custos com os valores fornecidos
    for i, j, cost in data:
        cost_matrix[i, j] = min(cost_matrix[i, j], cost)  # Mantém o custo mínimo se houver entradas duplicadas
    
    return cost_matrix

def hungarian_algorithm_manual(cost_matrix):
    n = len(cost_matrix)
    u = [0] * n
    v = [0] * n
    ind = [-1] * n

    for i in range(n):
        links = [-1] * n
        mins = [float('inf')] * n
        done = [False] * n
        marked_i = i
        marked_j = -1
        j = 0
        while True:
            j = -1
            for j1 in range(n):
                if not done[j1]:
                    cur = cost_matrix[marked_i][j1] - u[marked_i] - v[j1]
                    if cur < mins[j1]:
                        mins[j1] = cur
                        links[j1] = marked_j
                    if j == -1 or mins[j1] < mins[j]:
                        j = j1
            delta = mins[j]
            for j1 in range(n):
                if done[j1]:
                    u[ind[j1]] += delta
                    v[j1] -= delta
                else:
                    mins[j1] -= delta
            u[i] += delta
            done[j] = True
            marked_j = j
            marked_i = ind[j]
            if marked_i == -1:
                break
        while True:
            if links[j] != -1:
                ind[j] = ind[links[j]]
                j = links[j]
            else:
                break
        ind[j] = i

    # Creating a detailed list of matches and their costs
    matches = [(ind[j], j, cost_matrix[ind[j]][j]) for j in range(n)]
    return matches, sum(cost_matrix[ind[j]][j] for j in range(n))

start_time = time.time()
# Inputs input case
# cost_matrix_case = input_case1()
cost_matrix_case = input_case2()
# cost_matrix_case = input_case3()

# Run the Hungarian algorithm manually
matches, total_cost_manual = hungarian_algorithm_manual(cost_matrix_case)

print("Total cost of optimal matching:", total_cost_manual)
# print("Matches and their costs:")
# for match in matches:
#     print(f"Vertex {match[0]+1} is matched to Vertex {match[1]+1} with cost {match[2]}")

end_time = time.time()
duration = end_time - start_time
print(f"Duração {duration:.4f}")
