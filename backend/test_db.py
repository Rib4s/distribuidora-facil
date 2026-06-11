from app.database.session import engine

try:
    connection = engine.connect()
    print("✅ Conexão realizada com sucesso!")

    connection.close()

except Exception as e:
    print("❌ Erro:", e)