CREATE TABLE IF NOT EXISTS tb_funcionarios(
    matricula varchar(32) not null,
    nome varchar(255) not null,
    cargo varchar(255) not null,
    nome_usuario varchar(255) not null,
    senha varchar(255) not null,
    data_atual DATE DEFAULT CURRENT_DATE, 
    hora_atual TIME DEFAULT CURRENT_TIME,
    PRIMARY KEY (matricula)
);

CREATE TABLE IF NOT EXISTS tb_estoque(
    cod NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL, 
    quantidade INTEGER NOT NULL, 
    preco_compra REAL NOT NULL, 
    preco_venda REAL NOT NULL, 
    data_atual DATE DEFAULT CURRENT_DATE, 
    hora_atual TIME DEFAULT CURRENT_TIME
);

CREATE TABLE IF NOT EXISTS tb_vendas(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL, 
    quantidade INTEGER NOT NULL, 
    valor REAL NOT NULL, 
    total REAL NOT NULL, 
    data DATE DEFAULT CURRENT_DATE, 
    hora TIME DEFAULT CURRENT_TIME
);

