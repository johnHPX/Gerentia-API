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
INSERT INTO "tb_estoque" VALUES('232423342','sabonete 2','sabonete Dove 2',10,3.95,15.4,'2023-11-15','20:17:05',0,1);
INSERT INTO "tb_estoque" VALUES('23242334322','sabonete 3','sabonete Dove 3',10,3.95,15.4,'2023-11-15','20:20:05',0,1);
INSERT INTO "tb_estoque" VALUES('12345','shampoo','shampoo dourado',15,7.95,15.4,'2023-11-15','02:43:59',0,1);
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
INSERT INTO "tb_funcionarios" VALUES('20222082121231253','jonatas','Dev','johnHPX','jonatas123','2023-11-15','05:29:16',0,1);
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
