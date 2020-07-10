# Importando dependencias
from flask import Flask, render_template

# Definiendo el servidor
app = Flask(__name__)

# Definiendo Rutas
@app.route('/')
def index():
    return si sirve

# Iniciando el Servidor
if __name__ == "__main__":
    app.run(debug = True)