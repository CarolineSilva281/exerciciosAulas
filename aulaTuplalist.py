tupla = (1,2,3,4,5)
listanumero = list(tupla)
#converter tupla para lista
listanumero.append (5)
#inserir o objeto na ultima posição
listanumero.insert(0,0)
#inserir um objeto em qualquer posição sem remoção
listanumero.pop(1)
#remover um objeto da posição desejada
tupla = tuple(listanumero)
print(tupla)