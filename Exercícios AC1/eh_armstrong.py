"""Função que verifica se um número é de Armstrong

	Recebe um número natural n, com n >= 0, e retorna
	verdadeiro se n é um número de Armstrong e falso
	caso contrário.

	Exemplos
	--------
	Um número é dito número de Armstrong se a soma de seus digitos
	elevados ao número total de digitos é igual a ele próprio.
	153 é número de Armstrong:
		1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153
	4 é número de Armstrong:
		4 ** 1 = 4"""

def eh_armstrong(n):
	s = str(n)
	cont = 0
	acumulador = 0
	while cont <= len(s)-1:
		a = int(s[cont])  # Acessa posição de s com variável cont e converte para int.
		acumulador += a**len(s)
		cont += 1
	if acumulador == n:
		return True
	return False