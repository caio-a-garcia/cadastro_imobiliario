# Cadastro Imobiliário

## Como rodar
   - Clone o projeto
   - Com o prompt de commando aberto fora da pasta do projeto de o comando 'python cadastro_imobiliario'
   - Faca o login com as seguintes credenciais
     * usuário: caio.crud
     * senha: senhasegura

## Projeto

Esse projeto implementa um sistema de cadastro imobiliário em linha de comando.

O projeto é estruturado ao redor de seis classes que constituem as entidades descritas no diagrama lógico (./diagrama_logico.png). Para essa implementação foi utilizada a classe Individuo no lugar das classes filhas Inquilino e Proprietario, pois as caracteristicas comuns entre as classes se mostraram suficientes.

O dados são mantidos em memória em listas de dicionários e não são persistidos. É esperado que as estruturas de dados utilizadas se prestem facilmente aa persistência em arquivos de texto ou banco SQLite.

As listas de dados utilizam id auto-incremental. A implementação desse id é compativel com listas iniciais, de forma que o auto-incremento de id não precisa ser modificado para se adicionar dados iniciais em uma execução do programa. O auto-incremento depende de a lista inicial estar sortida em ordem crescente de id, e é frágil em não apresentar redundância na checagem de ids repetidos.