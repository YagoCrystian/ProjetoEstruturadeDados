class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [('L', None)] * tamanho

    def funcaoHash(self, chave):
        # Função usando resto da divisão
        soma_ascii = sum(ord(char) for char in chave)
        return soma_ascii % self.tamanho

    def inserir(self, nome):
        indice = self.funcaoHash(nome)

        # Inicializa tentativa quadrática
        i = 0
        while self.tabela[indice][0] in ['O', 'R']:
            i += 1
            indice = (indice + i**2) % self.tamanho

        # Insere o nome e altera para 'O'
        self.tabela[indice] = ('O', nome)

    def buscar(self, nome):
        indice = self.funcaoHash(nome)

        # Procura pelo nome
        i = 0
        while self.tabela[indice][0] == 'O':
            if self.tabela[indice][1] == nome:
                return f"{nome} encontrado na posição {indice}"
            i += 1
            indice = (indice + i**2) % self.tamanho

        return f"{nome} não encontrado na tabela"

    def deletar(self, nome):
        indice = self.funcaoHash(nome)

        # Procura pelo nome
        i = 0
        while self.tabela[indice][0] == 'O':
            if self.tabela[indice][1] == nome:
                # Marca como 'R' (deletado)
                self.tabela[indice] = ('R', None)
                return f"{nome} removido da tabela"
            i += 1
            indice = (indice + i**2) % self.tamanho

        return f"{nome} não encontrado na tabela"

#Funcao de Imprimir a tabela inteira
    def imprimirTabela(self):
        for i, item in enumerate(self.tabela):
            print(f"Posição {i}: {item}")

# Função de ler arquivo com os dados
def lerArquivo(Entradas="Entradas.txt"):
        try:
            # Abre o arquivo no modo de leitura ('r')
            with open(Entradas, 'r') as file:
                # Lê todas as linhas do arquivo e remove qualquer caractere de nova linha
                nomes = file.read().splitlines()

                # Para cada nome na lista de nomes lidos do arquivo
                for nome in nomes:
                    # Insere o nome na tabela hash usando o método inserir
                    tabela.inserir(nome)  # Note que agora estou usando "tabela" em vez de "self"

                # Imprime uma mensagem indicando que os nomes foram lidos e inseridos
                print(f"Nomes lidos de '{Entradas}' e inseridos na tabela.")

        except FileNotFoundError:
            # Se o arquivo não for encontrado, imprime uma mensagem de erro
            print(f"Arquivo '{Entradas}' não encontrado.")



# Função principal
if __name__ == "__main__":
    # Inicializa a tabela com um tamanho maior para facilitar a visualização das colisões
    tabela = TabelaHash(15)

    # Lê o arquivo
    lerArquivo("Entradas.txt")

    # Insere mais alguns nomes para criar colisões intencionais
    tabela.inserir("Charlie")
    tabela.inserir("Eva")
    tabela.inserir("Alice")

    # Imprime a tabela para visualizar as colisões
    tabela.imprimirTabela()

    # Busca por nomes
    print(tabela.buscar("Charlie"))
    print(tabela.buscar("Bob"))

    # Deleta um nome
    print(tabela.deletar("Eva"))

    # Busca novamente após a deleção
    print(tabela.buscar("Eva"))
