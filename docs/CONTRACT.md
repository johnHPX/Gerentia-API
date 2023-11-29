# Documentação

## Introdução

Bem-vindo à documentação da API Gerentia. Esta API fornece funcionalidades específicas para a sicronização dos bancos de dados das aplicações estoque, vendas e administração. A documentação abaixo detalha os endpoints disponíveis, seus métodos associados e exemplos práticos de como usá-los.

## Base URL

A URL base para todos os endpoints é: `http://localhost:8000`

## 1. Obter todos os dados cadastrados em Estoque do servidor (GET)

### Endpoint

```
GET /api/stock/local HTTP/1.1
```

Essa funcionalidade permite retorna um lista de dicionarios contendo todos os dados cadastrados na tabela `Estoque`, de forma que a aplicação local posso utlizar essa lista para atualizar seu banco de dados.


#### Exemplo de Requisição

```bash
curl -X GET http://localhost:8000/api/stock/local
```

#### Exemplo de Resposta (200 OK)

```json
{
    "Content": [
        {
            "cod":"213980213",
            "nome":"produto 1",
            "descricao":"descrição 1",
            "quantidade":100,
            "preco_compra":14.60,
            "preco_venda":20.80,
            "data_atual":"02-01-2023",
            "status":0,
            "sincronizado":1
        },
    ],
    "MID": "OK!"
}
```

#### Respostas de Erro

- **404 Not Found**: Quando o endpointer está escrito incorretamente.

- **500 Internal Server Error**: Quando há um problema no servidor.


## 2. Sincronizar dados local de Estoque para o servidor (POST)

### Endpoint

```
POST /api/stock/sinc HTTP/1.1
```

Esta funcionalidade permite cadastrar, atulizar e deletar dados do banco de dados do servidor com base nas alterações do banco de dados local.

Os campos `status` e `sincronizado` servem como parâmentros para a tomada de decisão da API. 

`status` -> indica a ação que foi realizada para esse dados; Há 3 possíveis valores:

0 -> indica que o dado foi criado. <br>
1 -> indica que o dado foi atualizado. <br>
2 -> indica que o dado foi deletado.

`sincronizado` -> indica se o dado foi sincronizado com o servidor ou não; Há 2 possíveis valores:

0 -> False. <br>
1 -> True.

#### Parâmetros

- `cod` (obrigatório) (string): Codigo de barra. 
- `nome` (obrigatório) (string): Nome.
- `descricao` (obrigatório) (string): Descrição.
- `quantidade` (obrigatório) (int): Quantidade.
- `preco_compra` (obrigatório) (float): Preço de compra.
- `preco_venda` (obrigatório) (float): Preço de venda.
- `data_atual` (obrigatório) (string): Data atual.
- `hora_atual` (obrigatório) (string): Hora atual.
- `status` (obrigatório) (int): Status de verificação.
- `sincronizado` (obrigatório) (int): Sincronização feita.

#### Exemplo de Requisição

```bash
curl -X POST -H "Content-Type: application/json" -d '{"cod": "1234583492382155","nome": "produto aleatorio 333","descricao": "qual quer coisa 333","quantidade": 15,"preco_compra": 7.95,"preco_venda": 15.40,"data_atual": "2023-11-15","hora_atual": "12:30:00","status": 0,"sincronizado": 0}' http://localhost:8000/api/stock/sinc 
```

#### Exemplo de Resposta (200 OK)

```json
{
  "MID": "OK"
}
```

#### Respostas de Erro

- **400 Bad Request**: Quando os dados fornecidos não estão corretos ou incompletos.


- **404 Not Found**: Quando o endpointer está escrito incorretamente.


- **500 Internal Server Error**: Quando há um problema no servidor.


## 3. Obter todos os dados cadastrados em Vendas do servidor (GET)

### Endpoint

```
GET /api/sales/local HTTP/1.1
```

Essa funcionalidade permite retorna um lista de dicionarios contendo todos os dados cadastrados na tabela `Vendas`, de forma que a aplicação local posso utlizar essa lista para atualizar seu banco de dados.

#### Exemplo de Requisição

```bash
curl -X GET http://localhost:8000/api/sales/local
```

#### Exemplo de Resposta (200 OK)

```json
{
    "Content": [
        {
          "id": 1,
          "nome": "venda 1",
          "quantidade": 10,
          "valor": 240.70,
          "total": 5,
          "data_atual": "2023-11-15",
          "hora_atual": "12:30:00",
          "status": 0,
          "sincronizado": 1
        },
    ],
    "MID": "OK!"
}
```

#### Respostas de Erro

- **404 Not Found**: Quando o endpointer está escrito incorretamente.

- **500 Internal Server Error**: Quando há um problema no servidor.


## 4. Sincronizar dados local de Vendas para o servidor (POST)

### Endpoint

```
POST /api/sales/sinc HTTP/1.1
```

Esta funcionalidade permite cadastrar, atulizar e deletar dados do banco de dados do servidor com base nas alterações do banco de dados local.

Os campos `status` e `sincronizado` servem como parâmentros para a tomada de decisão da API.

`status` -> indica a ação que foi realizada para esse dados; Há 3 possíveis valores:

0 -> indica que o dado foi criado. <br>
1 -> indica que o dado foi atualizado. <br>
2 -> indica que o dado foi deletado.

`sincronizado` -> indica se o dado foi sincronizado com o servidor ou não; Há 2 possíveis valores:

0 -> False. <br>
1 -> True.

#### Parâmetros

- `id` (obrigatório) (int): Id.
- `nome` (obrigatório) (string): nome.
- `quantidade` (obrigatório) (int): quantidade.
- `valor` (obrigatório) (float): valor.
- `total` (obrigatório) (float): total.
- `data_atual` (obrigatório) (string): data.
- `hora_atual` (obrigatório) (string): hora.
- `status` (obrigatório) (int): Status de verificação.
- `sincronizado` (obrigatório) (int): Sincronização feita.

#### Exemplo de Requisição

```bash
curl -X POST -H "Content-Type: application/json" -d '{
 "id": 1,"nome": "venda 1","quantidade": 10,"valor": 240.70,"total": 5,"data": "2023-11-15","hora": "12:30:00","status": 0,"sincronizado": 0}' http://localhost:8000/api/stock/sinc 
```

#### Exemplo de Resposta (200 OK)

```json
{
  "MID": "OK"
}
```

#### Respostas de Erro

- **400 Bad Request**: Quando os dados fornecidos não estão corretos ou incompletos.


- **404 Not Found**: Quando o endpointer está escrito incorretamente.


- **500 Internal Server Error**: Quando há um problema no servidor.

## 5. Obter todos os dados cadastrados em Funcionarios do servidor (GET)

### Endpoint

```
GET /api/admin/local HTTP/1.1
```

Essa funcionalidade permite retorna um lista de dicionarios contendo todos os dados cadastrados na tabela `tb_funcionarios`, de forma que a aplicação local posso utlizar essa lista para atualizar seu banco de dados.

#### Exemplo de Requisição

```bash
curl -X GET http://localhost:8000/api/admin/local
```

#### Exemplo de Resposta (200 OK)

```json
{
    "Content": [
        {
          "matricula": 4, 
          "nome": "wallyson",
          "cargo": "dev",
          "nome_usuario": "wall",
          "senha": "w123",
          "data_atual": "2023-11-15",
          "hora_atual": "12:30:00",
          "status": 0,
          "sincronizado": 1
        },
    ],
    "MID": "OK!"
}
```

#### Respostas de Erro

- **404 Not Found**: Quando o endpointer está escrito incorretamente.

- **500 Internal Server Error**: Quando há um problema no servidor.

## 6. Sincronizar dados local de Funcionarios para o servidor (POST)

### Endpoint

```
POST /api/admin/sinc HTTP/1.1
```

Esta funcionalidade permite cadastrar, atulizar e deletar dados do banco de dados do servidor com base nas alterações do banco de dados local.

Os campos `status` e `sincronizado` servem como parâmentros para a tomada de decisão da API.

`status` -> indica a ação que foi realizada para esse dados; Há 3 possíveis valores:

0 -> indica que o dado foi criado. <br>
1 -> indica que o dado foi atualizado. <br>
2 -> indica que o dado foi deletado.

`sincronizado` -> indica se o dado foi sincronizado com o servidor ou não; Há 2 possíveis valores:

0 -> False. <br>
1 -> True.

#### Parâmetros

- `matricula` (obrigatório) (int): Id.
- `nome` (obrigatório) (string): nome.
- `cargo` (obrigatório) (string): quantidade.
- `nome_usuario` (obrigatório) (string): valor.
- `senha` (obrigatório) (string): total.
- `data_atual` (obrigatório) (string): data.
- `hora_atual` (obrigatório) (string): hora.
- `status` (obrigatório) (int): Status de verificação.
- `sincronizado` (obrigatório) (int): Sincronização feita.

#### Exemplo de Requisição

```bash
curl -X POST -H "Content-Type: application/json" -d '"matricula": 4, "nome": "wallyson","cargo": "dev","nome_usuario": "wall","senha": "w123","data_atual": "2023-11-15","hora_atual": "12:30:00","status": 0,"sincronizado": 0}' http://localhost:8000/api/stock/sinc 
```

#### Exemplo de Resposta (200 OK)

```json
{
  "MID": "OK"
}
```

#### Respostas de Erro

- **400 Bad Request**: Quando os dados fornecidos não estão corretos ou incompletos.

- **404 Not Found**: Quando o endpointer está escrito incorretamente.

- **500 Internal Server Error**: Quando há um problema no servidor.

## 7. Fazer backup geral do banco de dados.

### Endpoint

```
GET /api/admin/do/backup HTTP/1.1
```

Essa funcionalidade permite realizar um backup de todos os registros do banco de dados, armazenando em arquivos separadas para cada tabela e um também em um único arquivo.

#### Exemplo de Requisição

```bash
curl -X GET http://localhost:8000/api/admin/do/backup 
```

#### Exemplo de Resposta (200 OK)

```json
{
    "MID": "OK!"
}
```

#### Respostas de Erro

- **404 Not Found**: Quando o endpointer está escrito incorretamente.

- **500 Internal Server Error**: Quando há um problema no servidor.


## Conclusão

Essa documentação fornece uma visão geral dos endpoints disponíveis na API, seus parâmetros, exemplos de requisições e respostas esperadas. Certifique-se de fornecer os dados corretos e seguir as instruções para interagir efetivamente com a API.

Se precisar de mais detalhes ou tiver dúvidas específicas, não hesite em entrar em contato com a equipe de suporte.

**Equipe de Desenvolvimento**
Jonatas N. Freitas / Equipe Gerentia
