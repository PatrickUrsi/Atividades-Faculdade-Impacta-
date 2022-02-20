"""Função que verifica se um número é primo

	Recebe um número natural n, com n >= 2, e retorna verdadeiro se
	n é um número primo e falso caso contrário.

	Exemplos
	--------
	Um número é dito primo se possuir apenas 2 divisores, isto é,
	não possuir nenhum divisor além do 1 e do próprio n.
	29 é primo:
		divisores de 29: 1, 29
	30 NÃO é primo:
		divisores de 30: 1, 2, 3, 5, 6, 10, 15, 30."""

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