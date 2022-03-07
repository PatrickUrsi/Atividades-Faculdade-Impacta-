"""Função que verifica se um número é quase de Armstrong

	Recebe um número natural n, com n >= 0, e retorna
	verdadeiro se n atende aos seguintes critérios:

	1) não ser um número de Armstrong;
	2) o resultado da soma de seus digitos elevados ao número total
	   de digitos é igual a ele próprio somado ou subtraído de 1.

	Exemplos
	--------
	35 é quase um número de Armstrong:
		3**2 + 5**2 = 9 + 25 = 34
	75 é quase um número de Armstrong:
		7**2 + 5**2 = 49 + 25 = 74"""

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

def eh_quase_armstrong(n):
	if eh_armstrong(n) == True:
		return False
	s = str(n)
	cont = 0
	acumulador = 0
	while cont <= len(s)-1:
		a = int(s[cont])
		acumulador += a**len(s)
		cont += 1
	if acumulador +1 == n:
		return True
	return False