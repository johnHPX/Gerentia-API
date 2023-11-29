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
INSERT INTO "tb_estoque" VALUES('12345','shampoo alterado','shampoo dourado alterado',15,7.95,15.4,'2023-11-15','03:57:13',0,1);
INSERT INTO "tb_estoque" VALUES('12345834923','produto aleatorio','qual quer coisa',15,7.95,15.4,'2023-11-15','21:54:22',0,1);
INSERT INTO "tb_estoque" VALUES('12345834923s55','produto aleatorio','qual quer coisa',15,7.95,15.4,'2023-11-15','00:13:01',0,1);
INSERT INTO "tb_estoque" VALUES('1234583492382155','produto aleatorio 333','qual quer coisa 333',15,7.95,15.4,'2023-11-15','08:34:02',0,1);
INSERT INTO "tb_estoque" VALUES('1234583','produto aleatorio 333','qual quer coisa 333',15,7.95,15.4,'2023-11-15','15:05:02',0,1);
INSERT INTO "tb_estoque" VALUES('12346579320','produto ivone','nâo existe mulher feia , existe mulher que não conhece os produtos ivones',15,7.95,15.4,'2023-11-15','21:54:53',0,1);
INSERT INTO "tb_estoque" VALUES('dcd7c180-a1a1-4e12-8c85-a5457e9b063f','JEQUITI','NÃO EXISTE MULHE FEIA, EXISTE MULHER QUE NÃO CONHECE OS PRODUTOS JEQUITI',10,125.0,250.0,'27/11/2023','00:36:34',0,1);
INSERT INTO "tb_estoque" VALUES('b4ce6249-29f0-4bdc-8b18-153fa55cc506','JEQUITI jonatas','alterado',40,120.0,250.0,'28/11/2023','19:22:21',1,1);
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
INSERT INTO "tb_funcionarios" VALUES('2','wallyson','dev','wall','w123','2023-11-15','12:30:00',0,0);
INSERT INTO "tb_funcionarios" VALUES('3','wallyson','dev','wall','w123','2023-11-15','12:30:00',0,1);
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
INSERT INTO "tb_vendas" VALUES(1,'venda 1',10,240.7,5.0,'2023-11-15','18:17:13',0,1);
INSERT INTO "tb_vendas" VALUES(2,'venda 1sxa',10,240.7,5.0,'2023-11-15','22:11:53',0,1);
INSERT INTO "tb_vendas" VALUES(3,'venda 1sxaekowqje',10,240.7,5.0,'2023-11-15','22:12:56',0,1);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('tb_vendas',3);
COMMIT;
