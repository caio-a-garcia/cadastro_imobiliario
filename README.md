# Cadastro Imobiliario

Esse projeto tem prop�sito primariamente did�tico. Seu objetivo � demonstrar pr�tica com Orienta��o a Objeto e outros conceitos b�sicos em Python. Por esse motivo a documenta��o pretende ser focada no processo de desenvolvimento, em contraste com o foco usual em usabilidade do c�digo.

## Premissas

O entreg�vel do projeto implementa um sistema de cadastro de im�veis e registro de contratos de aluguel. Um sistema de autentica��o � tambem parte das especifica��es. Enquanto a forma de autentica��o implementada aqui n�o tem preten��o de ser apropriada para produ��o (em termos de seguran�a e efici�ncia, por exemplo), ela busca manter uma boa experi�ncia de usu�rio, dentro dos limites da interface usada em cada fase.

## Processo
1) Definir como ser�o agrupadas as informa��es coletadas
    - Os itens a serem modelados s�o:
      * Im�vel: ID, logradouro, CEP, bairro, cidade
      * Inquilino/Proprietario: ID, nome, data de nascimento
      * Aluguel: ID, Imovel, Inquilino
    - A primeira tentativa de modelar esses dados foi feita com uma classe para cada um dos itens acima.

2) Definir quais formas de manipula��o desses dados podem ser usadas para implementar as funcionalidades desejadas
    - Dada a escolha de classes como forma de modelar os dados, um novo cadastro pode ser implementado como a cria��o de uma nova inst�ncia da classe apropriada.
    - Uma funcionalidade que consiga buscar os objetos criados de cada classe se faz necess�ria para trabalhar em cima dos dados registrados. Parece interessante separar essa funcionalidade da funcionalidade de cadastro, de forma a conseguir atribuir permiss�es para cada uma delas separadamente.

3) Implementar intera��es de usu�rio que acessem os m�todos definidos no passo 2
    - J� em sua vers�o mais b�sica, esse projeto se prop�e a criar uma interface de intera��o de forma que o usu�rio n�o chame fun��es diretamente, mas navegue no fluxo do programa.
    - Esse passo consiste me modelar e implementar dito fluxo, fazendo uso das funcionalidades desenvolvidas anteriormente.

4) Estruturar fluxo de login
    - Esse passo � entendido como independente dos passos anteriores e poderia ser implementado a qualquer momento, relativo aos outros passos.
    - Em sua primeira vers�o, o programa busca criar uma experi�ncia do fluxo de login para o usu�rio. Funcionalidades relativas a seguranca que seriam implementadas por autentica��o ficam como um exerc�cio futuro.