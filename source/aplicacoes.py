from collections import deque

# (FIFO - First In, First Out)

#criando uma fila vazia usando a classe "deque"
fila = deque()

#adicionando elementos ao final da fila (FIFO)
fila.append(9)
fila.append(2)
fila.append(3)

#removendo o primeiro item da fila 
primeiro_elemento = fila.popleft()
print(f"O primeiro elemento da fila é: {primeiro_elemento}")

#(LIFO - O ult elemento add é o primeiro elemento a ser removido)
pilha = []

#adicionando elementos ao final da pilha LIFO
pilha.append(1)
pilha.append(2)
pilha.append(45)

ultimo_elemento = pilha.pop()
print(f"O utimo elemento foi {ultimo_elemento}")

import matplotlib.pyplot as plt
import numpy as np

imagem = [
    [120,50,200,30,80],
    [90,180,25,160,120],
    [40,220,75,100,60],
    [150,70,100,190,140],
    [20,130,170,10,220]
]

# a matriz imagem é convertida em um array numpy
imagem_array = np.array(imagem)

#Exibindo a imagem 
plt.imshow(imagem_array, cmap= 'Blues', vmin=0, vmax=255)
plt.colorbar()
plt.show()