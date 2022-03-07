"""Função que conta a quantidade de primos em uma sequência

	Recebe uma sequência de números naturais s e retorna
	um dicionário com a contagem de ocorrências de cada número
	primo da sequência. Números não primos devem ser ignorados.
	Os números da sequência serão sempre maiores ou iguais a 2.

	Exemplos
	--------
	Caso s = [11, 2, 3, 4, 11, 2, 5, 2]
		O retorno deverá ser: {11: 2, 2: 3, 3: 1, 5: 1}
	Caso s = [1, 4, 8, 10]
		O retorno deverá ser: {}
	Caso s = (111, 191, 202, 306, 239, 579)
		O retorno deverá ser: {191: 1, 239: 1}"""

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