"""Função que verifica se um número é dito perfeito

	Recebe um número natural n, com n >= 2, e retorna verdadeiro se
	n é dito um número perfeito e falso caso contrário

	Exemplos
	--------
	Um número é dito perfeito se a soma de todos os divisores próprios é
	igual a ele mesmo.
	6 é um número perfeito:
		divisores próprios de 6: 1, 2, 3
		1 + 2 + 3 = 6
	12 NÃO é um número perfeito:
		divisores próprios de 12: 1, 2, 3, 4, 6
		1 + 2 + 3 + 4 + 6 = 16"""

def eh_perfeito(n):
	if n <= 2:
		return False
	cont = 1
	acumulador = 0
	while cont <= n -1:
		if n % cont == 0:
			acumulador += cont
		cont += 1
	if acumulador == n:
		return True
	return False