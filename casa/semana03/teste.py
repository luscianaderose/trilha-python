# Listas de exemplo
lista1 = [1, 2, 3, 4]
lista2 = [5, 6]
print("Lista1:", lista1)
print("Lista2:", lista2)  

posicao = int(input('Qual a posicao do numero q quer mover? '))
# Move o item da posição 2 (o número 3) de lista1 para lista2
item = lista1.pop(posicao)  # Remove o item da lista1 e o retorna
lista2.append(item)   # Adiciona o item em lista2

print("Lista1:", lista1)  # Saída: Lista1: [1, 2, 4]
print("Lista2:", lista2)  # Saída: Lista2: [5, 6, 3]
