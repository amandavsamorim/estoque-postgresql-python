# 📦 Controle de Estoque com Python + PostgreSQL

Projeto simples feito para fins de estudo, utilizando Python e PostgreSQL para simular um pequeno sistema de controle de estoque com inserção e listagem de produtos.

## 🛠️ Tecnologias utilizadas

- Python 3.10
- PostgreSQL
- Biblioteca `psycopg2`
- DBeaver (opcional, usado para visualizar o banco graficamente)

## 📋 Funcionalidades

- Inserção de produtos com nome, valor e quantidade
- Listagem dos produtos cadastrados no banco de dados

## 📁 Estrutura do banco de dados

O banco contém apenas uma tabela chamada `produtos` com a seguinte estrutura:

```sql
CREATE TABLE produtos (
	id SERIAL PRIMARY KEY,
	produto VARCHAR(100),
	valor DECIMAL(10,2),
	estoque INTEGER
);
