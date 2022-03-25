# Cadastro Imobiliario

Esse projeto tem propósito primariamente didático. Seu objetivo é demonstrar prática com Orientação a Objeto e outros conceitos básicos em Python. Por esse motivo a documentação pretende ser focada no processo de desenvolvimento, em contraste com o foco usual em usabilidade do código.

## Premissas

O entregável do projeto implementa um sistema de cadastro de imóveis e registro de contratos de aluguel. Um sistema de autenticação é tambem parte das especificações. Enquanto a forma de autenticação implementada aqui não tem pretenção de ser apropriada para produção (em termos de segurança e eficiência, por exemplo), ela busca manter uma boa experiência de usuário, dentro dos limites da interface usada em cada fase.

## Processo
1) Definir como serão agrupadas as informações coletadas
    - Os itens a serem modelados são:
      * Imóvel: ID, logradouro, CEP, bairro, cidade
      * Inquilino/Proprietario: ID, nome, data de nascimento
      * Aluguel: ID, Imovel, Inquilino
    - A primeira tentativa de modelar esses dados foi feita com uma classe para cada um dos itens acima.

2) Definir quais formas de manipulação desses dados podem ser usadas para implementar as funcionalidades desejadas
    - Dada a escolha de classes como forma de modelar os dados, um novo cadastro pode ser implementado como a criação de uma nova instância da classe apropriada.
    - Uma funcionalidade que consiga buscar os objetos criados de cada classe se faz necessária para trabalhar em cima dos dados registrados. Parece interessante separar essa funcionalidade da funcionalidade de cadastro, de forma a conseguir atribuir permissões para cada uma delas separadamente.

3) Implementar interações de usuário que acessem os métodos definidos no passo 2
    - Já em sua versão mais básica, esse projeto se propõe a criar uma interface de interação de forma que o usuário não chame funções diretamente, mas navegue no fluxo do programa.
    - Esse passo consiste me modelar e implementar dito fluxo, fazendo uso das funcionalidades desenvolvidas anteriormente.

4) Estruturar fluxo de login
    - Esse passo é entendido como independente dos passos anteriores e poderia ser implementado a qualquer momento, relativo aos outros passos.
    - Em sua primeira versão, o programa busca criar uma experiência do fluxo de login para o usuário. Funcionalidades relativas a seguranca que seriam implementadas por autenticação ficam como um exercício futuro.