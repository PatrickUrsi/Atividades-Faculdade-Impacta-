# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais

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




def conta_primos(s):
	dicionario_primos = {}
	cont = 0
	while cont <= len(s)-1:
		if eh_primo(s[cont]) == True:
			if s[cont] in dicionario_primos:
				dicionario_primos[s[cont]] += 1
			else:
				dicionario_primos[s[cont]] = 1
		cont += 1
	return dicionario_primos




def eh_armstrong(n):
	s = str(n)
	cont = 0
	acumulador = 0
	while cont <= len(s)-1:
		a = int(s[cont])
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




def lista_armstrong(n):
	lista = []
	cont = 0
	while cont <= n:
		if eh_armstrong(cont):
			lista.append(cont)
		cont += 1
	return lista




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