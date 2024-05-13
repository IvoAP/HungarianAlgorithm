import matplotlib.pyplot as plt

instancias = ['K3xK3', 'K10xK10', 'K500xK500']
duracao = [0.002, 0.003, 27.0614]
matching = [5.0, 1633.0, 250500]

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(instancias, matching, color='skyblue')

# Adicionar rótulos e título
plt.xlabel('Instâncias')
plt.ylabel('Número de Correspondências (escala logarítmica)')
plt.title('Número de Correspondências em Diferentes Instâncias')
plt.yscale('log')  # Usar escala logarítmica no eixo y
plt.grid(axis='y')

# Mostrar o gráfico
plt.show()
