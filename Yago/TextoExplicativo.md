___
#Implementação de uma Tabela de Hash com Tentativa Quadrática

##Trabalho da Disciplina Estrutura de Dados

####Professor:
*Saulo Pereira Ribeiro*

####Grupo: 
*Yago Crystian, Eduardo Soares, Lucas Cesar*
___

**Objetivo do Trabalho:**

- Desenvolver uma tabela de hash para armazenar nomes de pessoas. A tabela de hash será
representada por uma matriz com duas colunas: a primeira para o estado (L para livre, O para
ocupado e R para deletado) e a segunda para armazenar o elemento (neste caso, o nome da
pessoa). A função de hash utilizará o método de tentativa quadrática para resolver colisões.
___

**Descrição da Função de Hash:**

*A função de hash principal usa o método do resto da divisão. Dada uma chave (nome, neste
caso), a função calcula o valor do hash como o resto da divisão da soma dos valores ASCII dos
caracteres da chave pelo tamanho da tabela.*

**Tentativa Quadrática:**

- Em caso de colisões (quando uma posição calculada já está ocupada), a tentativa quadrática é
usada. Isso significa que, se a posição h(k) estiver ocupada, o programa tentará h(k) + 1^2, h(k)
+ 2^2, h(k) + 3^2, e assim por diante, até encontrar uma posição livre ou deletada.
___

**O que deve ser feito:**

*1. Implementar a função de hash que converte o nome em um índice da tabela.*

*2. Implementar a lógica de tentativa quadrática para lidar com colisões.*

*3. Criar a tabela de hash com um tamanho fixo e predefinido.*

*4. Implementar funções para inserir, buscar e deletar nomes da tabela de hash.*

*5. Ler nomes de um arquivo e inseri-los na tabela de hash usando as funções criadas.*

*6. Garantir que a inserção só aconteça em posições com estado L (livre) ou R (deletado), e
alterar o estado para O (ocupado) após a inserção.*
___

**Funções a Serem Implementadas e as demais de leitura de arquivo:**

funcao_hash(nome, tamanho_tabela): Calcula o índice para um dado nome.
inserir(tabela, nome): Insere um nome na tabela de hash.
buscar(tabela, nome): Busca um nome na tabela de hash.
deletar(tabela, nome): Deleta um nome da tabela de hash.
Testar todas as funcionalidades devem ser implementadas em python e comentadas linha a
linha.
___

**Resultados:**
Nomes lidos de 'Entradas.txt' e inseridos na tabela.
Posição 0: ('O', 'Eva')
Posição 1: ('L', None)
Posição 2: ('O', 'Jack')
Posição 3: ('O', 'aaaa')
Posição 4: ('O', 'abcd')
Posição 5: ('O', 'Bob')
Posição 6: ('O', 'Charlie')
Posição 7: ('O', 'Charlie')
Posição 8: ('O', 'David')
Posição 9: ('O', 'dcba')
Posição 10: ('O', 'bcdb')
Posição 11: ('L', None)
Posição 12: ('O', 'Alice')
Posição 13: ('O', 'Alice')
Posição 14: ('O', 'Eva')
Charlie encontrado na posição 6
Bob encontrado na posição 5
Eva removido da tabela
Eva não encontrado na tabela
___

**- Observacoes:**
1. A tabela hash é impressa, mostrando os elementos em cada posição.
2. A busca pelo nome "Charlie" encontrou uma ocorrência na posição 6.
3. A busca pelo nome "Bob" encontrou uma ocorrência na posição 5.
4. A deleção do nome "Eva" foi bem-sucedida, marcando-o como removido ('R') na posição 7.
5. A busca pelo nome "Eva" após a deleção mostra que ele não está mais na tabela.
6. Se você estava esperando colisões, elas ocorreram em posições como 7 (duas ocorrências de "Charlie") e 13 (duas ocorrências de "Alice"). Isso é uma demonstração de como a tabela trata colisões usando tentativa quadrática para encontrar uma posição adequada.

