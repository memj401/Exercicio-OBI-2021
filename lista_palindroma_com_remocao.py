class Lista_Palindroma(object):
	def __init__(self,tam,lista):
		self.tam = int(tam)
		self.lista = [int(x) for x in lista.split()[:self.tam]]
		
		if self.tam != len(self.lista):
			self.tam = len(self.lista)

	def tornar_lista_palindroma(self):
		numero_de_contracoes = 0
		inicio = 0
		fim = self.tam - 1
		lista = self.lista
		while inicio < fim:
			if lista[inicio] < lista[fim]:
				lista[inicio] += lista[inicio+1]
				lista.pop(inicio + 1)
				numero_de_contracoes += 1
				fim -= 1
			elif self.lista[fim] < self.lista[inicio]:
				lista[fim] += lista[fim-1]
				lista.pop(fim-1)
				numero_de_contracoes += 1
				fim -= 1
			else:
				inicio += 1
				fim -= 1
		return numero_de_contracoes

entrada_tam = input()
entrada_lista = input()

lista_palindroma = Lista_Palindroma(entrada_tam,entrada_lista)
print(lista_palindroma.tornar_lista_palindroma())
