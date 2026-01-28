from flask import Flask, request, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

# Variables de entorno para la base de datos
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Conexión a la base
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

# Crear tabla si no existe (espera a que la BD esté lista)
def create_table():
    while True:
        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id SERIAL PRIMARY KEY,
                    tipo VARCHAR(100),
                    descripcion TEXT,
                    fecha DATE
                );
            """)

            conn.commit()
            cur.close()
            conn.close()
            print("Tabla verificada/creada correctamente")
            break

        except Exception as e:
            print("Esperando base de datos...", e)
            time.sleep(3)

create_table()

# -------- ENDPOINTS --------

@app.route("/events", methods=["POST"])
def create_event():
    data = request.json

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO events (tipo, descripcion, fecha)
        VALUES (%s, %s, %s)
    """, (data["tipo"], data["descripcion"], data["fecha"]))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Evento guardado correctamente"}), 201


@app.route("/events", methods=["GET"])
def get_events():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, tipo, descripcion, fecha FROM events")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    events = []
    for row in rows:
        events.append({
            "id": row[0],
            "tipo": row[1],
            "descripcion": row[2],
            "fecha": str(row[3])
        })

    return jsonify(events)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
