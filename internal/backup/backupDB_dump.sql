BEGIN TRANSACTION;
CREATE TABLE tb_estoque(
    cod varchar(32) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL, 
    quantidade INTEGER NOT NULL, 
    preco_compra REAL NOT NULL, 
    preco_venda REAL NOT NULL, 
    data_atual DATE DEFAULT CURRENT_DATE, 
    hora_atual TIME DEFAULT CURRENT_TIME,
    status numeric NOT NULL,
    sincronizado numeric NOT NULL
);
CREATE TABLE tb_funcionarios(
    matricula varchar(32) PRIMARY KEY,
    nome varchar(255) NOT NULL,
    cargo varchar(255) NOT NULL,
    nome_usuario varchar(255) NOT NULL,
    senha varchar(255) NOT NULL,
    data_atual DATE DEFAULT CURRENT_DATE, 
    hora_atual TIME DEFAULT CURRENT_TIME,
    status numeric NOT NULL,
    sincronizado numeric NOT NULL
);
CREATE TABLE tb_vendas(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL, 
    quantidade INTEGER NOT NULL, 
    valor REAL NOT NULL, 
    total REAL NOT NULL, 
    data DATE DEFAULT CURRENT_DATE, 
    hora TIME DEFAULT CURRENT_TIME,
    status numeric NOT NULL,
    sincronizado numeric NOT NULL
);
DELETE FROM "sqlite_sequence";
COMMIT;
