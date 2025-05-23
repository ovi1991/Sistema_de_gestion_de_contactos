from flask import Flask, jsonify, request
from flask_cors import CORS
from contactos import GestionContactos
import os

app = Flask(__name__)
CORS(app)
gestion = GestionContactos()

@app.route('/api/contactos', methods=['GET'])
def obtener_contactos():
    return jsonify(gestion.obtener_contactos())



# Agregar un nuevo contacto
@app.route("/api/contactos", methods=["POST"])
def agregar_contacto():
    data = request.get_json()
    try:
        nuevo = gestion.agregar_contacto(
            data["nombre"],
            data["telefono"],
            data["email"]
        )
        return jsonify(nuevo), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Buscar un contacto por nombre
@app.route("/api/contactos/<nombre>", methods=["GET"])
def buscar_contacto(nombre):
    contacto = gestion.buscar_contacto(nombre)
    if contacto:
        return jsonify(contacto)
    else:
        return jsonify({"error": "Contacto no encontrado"}), 404

# Eliminar un contacto por nombre
@app.route("/api/contactos/<nombre>", methods=["DELETE"])
def eliminar_contacto(nombre):
    eliminado = gestion.eliminar_contacto(nombre)
    if eliminado:
        return jsonify(eliminado)
    else:
        return jsonify({"error": "Contacto no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "True") == "True", port=int(os.getenv("PORT", 5000)))