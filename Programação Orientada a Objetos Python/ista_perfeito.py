"""Função que lista os números ditos perfeitos até n

	Recebe um número natural n, com n >= 2, e retorna uma lista
	com todos os números perfeitos estritamente menores que n,
	em ordem crescente."""

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

def lista_perfeitos(n):
	lista = []
	cont = 0
	while cont <= n:
		if eh_perfeito(cont):
			lista.append(cont)
		cont += 1
	return lista