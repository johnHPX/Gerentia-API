#!/bin/bash

# Caminho para o arquivo do banco de dados SQLite
DATABASE_PATH="../internal/db/gerentia.db"

# Array contendo nomes das tabelas a serem removidas
TABLES=("tb_funcionarios" "tb_estoque" "tb_vendas")

# Itera sobre as tabelas e executa a query DROP TABLE
for TABLE in "${TABLES[@]}"
do
    sqlite3 $DATABASE_PATH "DROP TABLE IF EXISTS $TABLE;"
    echo "Tabela $TABLE removida."
done

echo "Operação concluída: Todas as tabelas foram removidas do banco de dados."
