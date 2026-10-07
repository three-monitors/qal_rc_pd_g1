import psycopg

# Параметри підключення (з Render)
DSN = "postgresql://dbsmsadmin:OIY1C6HqPfFVEn6ujG2CdDmrpEdkMuix@dpg-db343b49v7es73at0tsg-a.oregon-postgres.render.com/dbsms_0axi"

try:
    # Підключитися до БД
    with psycopg.connect(DSN) as conn:
        print("✅ Успішно підключені до PostgreSQL!")

        # Отримати інформацію про БД
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            version = cur.fetchone()[0]
            print(f"\n📊 PostgreSQL версія:\n{version}\n")

            # Отримати інформацію про поточного користувача
            cur.execute("SELECT current_user;")
            user = cur.fetchone()[0]
            print(f"👤 Користувач: {user}")

            # Отримати поточну БД
            cur.execute("SELECT current_database();")
            database = cur.fetchone()[0]
            print(f"📁 Поточна БД: {database}")

except psycopg.Error as e:
    print(f"❌ Помилка підключення: {e}")
