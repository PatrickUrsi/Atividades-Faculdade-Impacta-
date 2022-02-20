"""Função que lista os números e Armstrong até n

	Recebe um número natural n e retorna uma lista com todos o
	números de Armstrong estritamente menores que n, em ordem 
    crescente."""

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

def lista_armstrong(n):
	lista = []
	cont = 0
	while cont <= n:
		if eh_armstrong(cont):
			lista.append(cont)
		cont += 1
	return lista