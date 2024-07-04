from flask import Flask, request, jsonify, send_from_directory
import mysql.connector
import os

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'host': 'localhost',
    'database': 'plataforma_educativa'
}

@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    data = request.json
    nombre = data['nombre']
    documento = data['documento']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios_basico (nombre, documento) VALUES (%s, %s)", (nombre, documento))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(success=True)

@app.route('/add_usuario_full', methods=['POST'])
def add_usuario_full():
    data = request.json
    nombre = data['nombre']
    documento = data['documento']
    fecha_nacimiento = data['fecha_nacimiento']
    localidad = data['localidad']
    email = data['email']
    cursos = data['cursos']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios_completo (nombre, documento, fecha_nacimiento, localidad, email, cursos) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, documento, fecha_nacimiento, localidad, email, cursos))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify(success=True)

@app.route('/get_usuarios', methods=['GET'])
def get_usuarios():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios_completo")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(usuarios=usuarios)

@app.route('/delete_usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios_completo WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(success=True)

@app.route('/')
def index():
    return send_from_directory(os.path.abspath(os.path.dirname(__file__)), 'usuarios.html')

if __name__ == '__main__':
    app.run(debug=True)
