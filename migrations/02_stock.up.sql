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

