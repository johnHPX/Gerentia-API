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