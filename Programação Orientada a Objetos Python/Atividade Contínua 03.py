# Programação Orientada a Objetos
# AC03 ADS-EaD - Implementação de classes, herança, polimorfismo e lançamento de exceções.
#
# Email Impacta: ______________@aluno.faculdadeimpacta.com.br


class Produto:

	def __init__(self, nome, preco):
		self.__nome = nome
		self.__preco = preco


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


class ProdutoFisico:

	def __init__(self, nome, preco, peso):
		super().__init__(nome, preco)
		self.__peso = peso


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
		"""
		Método que calcula o peso do produto em quilogramas.
		Deve devolver (retornar) o valor do peso convertido em quilogramas.
		Exemplos:
			- Se o valor do atributo privado peso for 1000, este método retorna 1;
			- Se o valor do atributo privado peso for 7500, este método retorna 7.5;
			- Se o valor do atributo privado peso for 600, este método retorna 0.6;
		"""
		pass


	def calcular_preco_com_frete(self):
		"""
		Método que calcula o valor final do produto físico com o frete incluso.
		Para cada quilograma no peso do produto, acrescente R$5 ao seu valor final.

		Deve devolver (retornar) o valor final do produto acrescido do frete (que depende
		do peso do produto em quilogramas, conforme descrito acima).

		Dica: você pode (e deve) utilizar o método peso_em_kg para obter o peso
		do produto em kg.

		Exemplos:
			- Se o produto (preço) custa R$100 e seu peso é 1000 gramas, retorna R$105;
			- Se o produto (preço) custa R$50 e seu peso é 2500 gramas, retorna R$62.5;
			- Se o produto (preço) custa R$10 e seu peso é 100 gramas, retorna R$10.5;
			
		"""
		pass


class ProdutoEletronico:
	"""
	Classe ProdutoEletronico: deve representar os elementos básicos de um produto eletrônico.
	Esta classe herda da classe ProdutoFisico.
	"""

	def __init__(self, nome, preco, peso, tensao, tempo_garantia):
		"""
		Inicializa nome, preco e peso utilizando o construtor da superclasse ProdutoFisico, 
		(use a função super()), e também inicializa os atributos privados tensao e
		tempo_garantia da seguinte forma:
			- O atributo privado tensao não deve ser declarado diretamente no
			construtor.	Ao invés disso, utilize o setter "tensao" para inicializá-lo
			indiretamente, pois dessa forma ele será validado. 

			- O atributo privado tempo_garantia deve ser inicializado diretamente
			no construtor, sem necessidade de validação.
		"""
		pass

	
	@property
	def tensao(self):
		"""
		Property tensao: devolve (retorna) o valor do atributo privado tensao.
		"""
		pass


	@property
	def tempo_garantia(self):
		"""
		Property tempo_garantia: devolve (retorna) o valor do atributo privado tempo_garantia.
		"""
		pass

	
	@tensao.setter
	def tensao(self, nova_tensao):
		"""
		Setter tensao: recebe uma nova_tensao e atualiza o valor do atributo privado
		tensao com esse valor (que representa a tensão de um aparelho eletrônico, 
		com os seguintes valores possíveis: 0, indicando que o produto é bivolt,
		127 ou 220).

		Antes de modificar o valor do atributo privado tensao, verifique se seu valor
		é do tipo int (utilize a função isinstance para fazer essa verificação),
		caso contrário lance uma exceção do tipo TypeError.
		Caso nova_tensao seja do tipo int, verifique se seu valor é igual a 0, ou
		127 ou 220. Caso nova_tensao seja diferente desses valores, lance uma 
		exceção do tipo ValueError.
		"""
		pass


	def calcular_preco_com_frete(self):
		"""
		Método que calcula o valor final do produto eletrônico com o frete incluso.
		O cálculo é o mesmo que o produto físico, mas deverá ser acrescido 1% 
		ao valor final do frete.
		Dica: você pode reaproveitar o método calcular_preco_com_frete() da
		superclasse (a classe ProdutoFisico), através da função super(). Ou seja,
		obtenha o valor do frete do produto físico, depois acrescente 1% e devolva
		(retorne) esse valor.

		Deve devolver (retornar) o valor final do produto acrescido do frete (será
		o mesmo valor com frete do produto físico, com o acréscimo de 1%).

		Exemplos:
			- Se o produto (preço) custa R$100 e seu peso é 1000 gramas, retorna R$106.05;
			- Se o produto (preço) custa R$50 e seu peso é 2000 gramas, retorna R$60.6;
			- Se o produto (preço) custa R$10 e seu peso é 800 gramas, retorna R$14.14;
		"""
		pass


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



