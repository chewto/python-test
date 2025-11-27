from flask import Flask, request, jsonify, render_template_string, abort


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def helloWorld():
    if request.method == "POST":
      return "¡Hola, Mundo! POST"

    return "¡Hola, Mundo! GET"


# Manejo simple de errores
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "No encontrado"}), 404


if __name__ == "__main__":
    # En desarrollo: debug=True; en producción usar un servidor WSGI (gunicorn/uvicorn)
    app.run(host="0.0.0.0", port=5000, debug=True)