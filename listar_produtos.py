import psycopg2

try:
    conexao = psycopg2.connect(
        dbname = "cadastro_produtos",
        user = "amanda",
        password = "amanda",
        host = "localhost",
        port = "5432"
    )

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    resultados = cursor.fetchall()

    print("\n 📦 Lista de produtos:")
    for produto in resultados:
        print(f"ID: {produto[0]} | Produto:{produto[1]} | Valor: R${produto[2]} | Estoque: {produto[3]}")
    
except Exception as erro:
    print("Ocorreu um erro:", erro)

finally:
    if conexao:
        cursor.close()
        conexao.close()
