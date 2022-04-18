# Cadastro Imobili�rio

## Como rodar
   - Clone o projeto
   - Com o prompt de commando aberto fora da pasta do projeto de o comando 'python cadastro_imobiliario'
   - Faca o login com as seguintes credenciais
     * usu�rio: caio.crud
     * senha: senhasegura

## Projeto

Esse projeto implementa um sistema de cadastro imobili�rio em linha de comando.

O projeto � estruturado ao redor de seis classes que constituem as entidades descritas no diagrama l�gico (./diagrama_logico.png). Para essa implementa��o foi utilizada a classe Individuo no lugar das classes filhas Inquilino e Proprietario, pois as caracteristicas comuns entre as classes se mostraram suficientes.

O dados s�o mantidos em mem�ria em listas de dicion�rios e n�o s�o persistidos. � esperado que as estruturas de dados utilizadas se prestem facilmente aa persist�ncia em arquivos de texto ou banco SQLite.

As listas de dados utilizam id auto-incremental. A implementa��o desse id � compativel com listas iniciais, de forma que o auto-incremento de id n�o precisa ser modificado para se adicionar dados iniciais em uma execu��o do programa. O auto-incremento depende de a lista inicial estar sortida em ordem crescente de id, e � fr�gil em n�o apresentar redund�ncia na checagem de ids repetidos.