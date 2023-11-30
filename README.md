# Gerentia - Application Programming Interface

A API(Application Programming Inteface) do software Gerentia tem como único objetivo ser um meio de comunicação entre os setores de estoque, vendas e administração. É responsável por sincronizar o banco de dados local presente em ambas as aplicações, de forma que todos no final possam ter as mesmas informações. É destinando exclusivamente aos desenvolvedores do software Gerentia: Estoque, Gerentia: Vendas e Gerentia: admin.

## Avisos

<p> Para usar o serviço, o desenvolvedor precisa conectar a sua aplicação local com a API, utilizando uma URL correspondente ao domínio a qual a API está localizada.
Um exemplo: em ambiente de desenvolvimento local, o serviço da API estará escutando na sua máquina. Portanto, a URL seria “http://localhost:PORT/”, onde a palavra-chave “PORT” referencia a porta do seu computador, na qual a API está rodando. </p>

<p><b>Está API por padrão escuta na porta 8000.</b></p>

<p style="font-size: 20px; ">A documentação completa da API Gerentia está localizada na pasta Docs deste repositório. Mas é muito importante conferir o básico sobre consumo de APIs para que o desenvolvedor tenha menos problemas na hora de integrar o serviço com sua aplicação local.</p>

<hr>

# Como iniciar a API:

## Linux e Mac

```

// Para iniciar o ambiente virtual:

- source venv/bin/activate 

// E para executar a API basta rodar o comando:

- python3 main.py 

```

## Windows

```

// Para iniciar o ambiente virtual:

- venv\Scripts\activate

// E para executar a API basta rodar o comando:

- python3 main.py 

```
