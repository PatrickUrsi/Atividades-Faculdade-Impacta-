"""Função que retorna uma lista de primos até n

	Recebe um número natural n, com n >= 2, e retorna uma
	lista com todos o números primos estritamente menores
	que n, em ordem crescente.

	Parâmetros
	----------
	n : int
		Número natural que define o limite superior da lista.

	Retorno
	-------
	list
		itens : int
		descrição : Lista com todos os números primos menores
			que n, em ordem crescente.
	"""

def eh_primo(n):
	if n < 2:
		return False
	validador = 0
	cont = 1
	while cont <= n:
		if n % cont == 0:
			validador += 1
		cont += 1
	if validador == 2:
		return True
	return False

def lista_primos(n):
	if n < 2:
		return False
	lista = []
	for primo in range(2, n):
		if eh_primo(primo):
			lista.append(primo)
	return lista
