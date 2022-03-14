# Programação Orientada a Objetos
# AC03 ADS-EaD - Implementação de classes, herança, polimorfismo e lançamento de exceções.
#
# Email Impacta: patrick.ursi@aluno.faculdadeimpacta.com.br


class Produto:

	def __init__(self, nome, preco):
		self.nome = nome
		self.preco = preco


	@property
	def nome(self):
		return self.__nome


	@property
	def preco(self):
		return self.__preco


	@nome.setter
	def nome(self, novo_nome):
		if len(novo_nome) == 0:
			raise ValueError
		else:
			self.__nome = novo_nome


	@preco.setter
	def preco(self, novo_preco):
		if isinstance(novo_preco, int) or isinstance(novo_preco, float):
			if novo_preco >= 0:
				self.__preco = novo_preco
			else: 
				raise ValueError
		else:
			raise TypeError


	def calcular_preco_com_frete(self):
		return self.__preco


class ProdutoFisico(Produto):

	def __init__(self, nome, preco, peso):
		super().__init__(nome, preco)
		self.peso = peso


	@property
	def peso(self):
		return self.__peso


	@peso.setter
	def peso(self, novo_peso):
		if isinstance(novo_peso, int):
			if novo_peso > 0:
				self.__peso = novo_peso
			else: 
				raise ValueError
		else: 
			raise TypeError


	def peso_em_kg(self):
		return self.peso / 1000


	def calcular_preco_com_frete(self):
		cal1 = self.peso_em_kg()
		cal2 = self.preco
		calcular_preco_com_frete = (cal1 * 5) + cal2
		return calcular_preco_com_frete


class ProdutoEletronico(ProdutoFisico):

	def __init__(self, nome, preco, peso, tensao, tempo_garantia):
		super().__init__(nome, preco, peso)
		self.tensao = tensao
		self.__tempo_garantia = tempo_garantia


	@property
	def tensao(self):
		return self.__tensao


	@property
	def tempo_garantia(self):
		return self.__tempo_garantia


	@tensao.setter
	def tensao(self, nova_tensao):
		if isinstance(nova_tensao, int):
			if nova_tensao == 0 or nova_tensao == 127 or nova_tensao == 220:
				self.__tensao = nova_tensao
			else:
				raise ValueError
		else:
			raise TypeError


	def calcular_preco_com_frete(self):
		cal1 = self.peso_em_kg()
		cal2 = self.preco
		calcular_preco_com_frete = (((cal1 * 5) + cal2) * 0.01) + ((cal1 * 5) + cal2)
		return calcular_preco_com_frete


class Ebook:
	"""
	Classe Ebook: deve representar os elementos básicos de um ebook (livro digital).
	Esta classe herda da classe Produto.
	"""

	def __init__(self, nome, preco, autor, numero_paginas):
		"""
		Inicializa nome e preco utilizando o construtor da superclasse Produto, 
		(use a função super()), e também inicializa os atributos privados autor e
		numero_paginas da seguinte forma:
			- O atributo privado autor deve ser inicializado diretamente
			no construtor, sem necessidade de validação.

			- O atributo privado numero_paginas não deve ser declarado diretamente no
			construtor.	Ao invés disso, utilize o setter "numero_paginas" para
			inicializá-lo indiretamente, pois dessa forma ele será validado.
		"""
		pass
	

	@property
	def nome_exibicao(self):
		"""
		Property nome_exibicao: devolve (retorna) uma string com o nome e autor
		do livro no seguinte formato (sem aspas): "Nome (Autor)".

		Exemplos:
			- Se nome é "Aprendendo Python" e autor é "Ana Maria", deve devolver (retornar)
			 uma string com: "Aprendendo Python (Ana Maria)";

			- Se nome é "O senhor dos anéis" e autor é "J. R. R. Tolkien", deve
			devolver (retornar) uma string com: "O senhor dos anéis (J. R. R. Tolkien)";
		"""
		pass


	@property
	def numero_paginas(self):
		"""
		Property numero_paginas: devolve (retorna) o valor do atributo 
		privado numero_paginas.
		"""
		pass
	

	@numero_paginas.setter
	def numero_paginas(self, valor):
		"""
		Setter numero_paginas: recebe um valor e atualiza o atributo privado
		numero_paginas com esse valor.

		Antes de modificar o valor do atributo privado numero_paginas, verifique
		se o valor é maior que zero. Caso contrário (se valor for menor ou igual
		a zero), lance um erro do tipo ValueError.
		"""
		pass