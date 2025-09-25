# Código python entrevista

O código relacionado a este repositório representa os desafios requisitados pela empresa byne durante a entrevista realizada em 25/09

## Como rodar

- Execute os comandos:
    ``pip install -r requirements.txt``
- Após isso, basta executar o o arquivo teste_estagio, pegando o host e a porta da api
- Crie um .env com o host e porta da api
- Execute o api_call

## Especificações de funções

### return_odd_number

    Gera um número aleatório entre 0 e 100 mil, percorrendo um loop até esse número ser impar. A verificação é feita verificando a divisão de módulo por 2 ser diferente de 0.

### return_even_number

    Gera um número aleatório entre 0 e 100 mil, percorrendo um loop até esse número ser par. A verificação é feita verificando a divisão de módulo por 2 ser igual a 0.

### return_text

    Retorna um texto fixo.

## Arquitetura cliente-servidor

Pensando em uma arquitetura envolvendo um website e um banco de dados hospedado em um servidor.

- Site faz a requisição através de chamadas de API para o servidor;
- Servidor web que está hospedado lá recebe a requisição;
- Servidor faz as devidas validações: Método da requisição, rota pedida, permissões, autenticação;
- Caso as validações sejam positivas: Busca os dados pedidos pela requisição e monta o padrão de resposta esperado pelo site;
- Caso as validações sejam negativas: Retorna uma mensagem e código de erro indicando o problema (rota inválida, usuário não autenticado, dados não existentes);
- Site recebe a o retorno da requisição e trata da forma que for necessária;
