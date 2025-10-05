from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Configuración DB (usa las mismas credenciales del contenedor Postgres)
DB_CONFIG = {
    "dbname": "analytics_db",
    "user": "admin",
    "password": "admin123",
    "host": "postgres_db",  # nombre del servicio en docker-compose
    "port": "5432"
}

@app.route("/")
def home():
    return jsonify({"status": "API Flask funcionando correctamente"})

@app.route("/data", methods=["GET"])
def get_data():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT * FROM noticias LIMIT 10;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
