import psycopg2

# Cria a conexão com o banco
def conectar():
    return psycopg2.connect(
        dbname = "cadastro_produtos",
        user = "amanda",
        password = "amanda",
        host = "localhost",
        port = "5432"
    )

#Inserir os dados na tabela
def inserir_produto(conn, produto, valor, estoque):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO produtos (produto, valor, estoque) VALUES (%s, %s, %s)",
        (produto, valor, estoque)
    )
    conn.commit()
    print(f"Produto '{produto}' inserido com sucesso!")
    cur.close()

def recebe_dados():
    produto = input("Nome do produto: ")
    valor = float(input("Valor do produto: "))
    estoque = int(input("Quantidade em estoque: "))
    return produto, valor, estoque

#Função principal
def main():
    try:
        conn = conectar()
        produto, valor, estoque = recebe_dados()
        inserir_produto(conn, produto, valor, estoque)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conn.close()
    
if __name__ == "__main__":
    main()