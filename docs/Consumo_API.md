# Guia Didático de Consumo de APIs em Python

Bem-vindo ao Guia Didático de Consumo de APIs em Python! Este documento destina-se a proporcionar uma compreensão prática e teórica sobre APIs e como consumi-las usando a linguagem de programação Python.

## Introdução

### O que é uma API?

Uma API (Interface de Programação de Aplicações) é um conjunto de regras e definições que permite que um software se comunique com outro. Ela define as maneiras pelas quais os componentes de software devem interagir. APIs são cruciais para a integração de sistemas e serviços.

### Como as APIs Funcionam?

As APIs possibilitam a comunicação entre diferentes sistemas por meio de requisições HTTP (Hypertext Transfer Protocol). Geralmente, essas requisições são feitas utilizando os métodos HTTP: GET, POST, PUT e DELETE.

- **GET**: Solicita a recuperação de dados de um recurso específico.
- **POST**: Envia dados para o servidor para criar um novo recurso.
- **PUT**: Atualiza dados de um recurso existente no servidor.
- **DELETE**: Remove um recurso do servidor.

## Requisitos Prévios

Antes de começar, certifique-se de ter o Python instalado em sua máquina e um editor de código configurado, como o Visual Studio Code.

## Instalação de Dependências

Vamos usar a biblioteca `requests` para realizar solicitações HTTP em Python. Instale-a utilizando o seguinte comando:

```bash
pip install requests
```

## Realizando Requisições GET

Vamos começar com o método GET, que é utilizado para obter dados de um recurso no servidor.

```python
import requests

url = 'https://api.exemplo.com/dados'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Erro {response.status_code}: {response.text}')
```

Neste exemplo, fazemos uma requisição GET para a URL fornecida e verificamos se a resposta foi bem-sucedida (código 200). Se for, convertemos a resposta para JSON e a exibimos.

## Enviando Dados com Requisições POST

O método POST é utilizado para enviar dados ao servidor e criar um novo recurso.

```python
import requests

url = 'https://api.exemplo.com/enviar_dados'
data = {'chave': 'valor'}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Dados enviados com sucesso!')
else:
    print(f'Erro {response.status_code}: {response.text}')
```

Aqui, enviamos dados na forma de um dicionário JSON para a URL especificada usando o método POST.

## Realizando Requisições PUT e DELETE

Os métodos PUT e DELETE são utilizados para atualizar e excluir recursos, respectivamente.

```python
import requests

# Método PUT
url_put = 'https://api.exemplo.com/atualizar_dados/1'
data_put = {'campo': 'novo_valor'}

response_put = requests.put(url_put, json=data_put)

if response_put.status_code == 200:
    print('Dados atualizados com sucesso!')
else:
    print(f'Erro {response_put.status_code}: {response_put.text}')

# Método DELETE
url_delete = 'https://api.exemplo.com/excluir_dados/1'

response_delete = requests.delete(url_delete)

if response_delete.status_code == 200:
    print('Dados excluídos com sucesso!')
else:
    print(f'Erro {response_delete.status_code}: {response_delete.text}')
```

Aqui, utilizamos o método PUT para atualizar dados e o método DELETE para excluir dados do servidor.

## Manipulação de Respostas JSON

Frequentemente, as APIs retornam dados no formato JSON (JavaScript Object Notation). Veja como manipular essas respostas em Python:

```python
import requests

url = 'https://api.exemplo.com/dados'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Acesse os dados como um dicionário
    print('Nome:', data['nome'])
    print('Idade:', data['idade'])
else:
    print(f'Erro {response.status_code}: {response.text}')
```

Ao receber uma resposta, podemos converter o conteúdo JSON para um dicionário Python para facilitar a manipulação.

## Tratamento de Erros

Ao realizar solicitações HTTP, é importante lidar com possíveis erros. Utilize um bloco `try...except` para tratar exceções.

```python
import requests

url = 'https://api.exemplo.com/dados'

try:
    response = requests.get(url)
    response.raise_for_status()  # Lança uma exceção para códigos de erro HTTP
    data = response.json()
    print(data)
except requests.exceptions.RequestException as err:
    print(f'Erro: {err}')
```

Este bloco `try...except` captura erros durante a solicitação, incluindo erros HTTP, e exibe uma mensagem apropriada.

## Conclusão

Parabéns! Você agora possui uma compreensão básica e prática de como consumir APIs em Python. Continue explorando diferentes APIs e ajuste os exemplos conforme necessário para suas próprias necessidades.

## Referências

- [Documentação do módulo `requests`](https://docs.python-requests.org/en/latest/)
- [HTTP Methods: PUT and DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT)
- [HTTP Methods: DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)
