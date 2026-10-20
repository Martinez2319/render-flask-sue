from flask import Flask

# Actividad 5: verificacion del despliegue continuo con Render.
app = Flask(__name__)


@app.route("/")
def home():
    return "API funcionando en Render"


if __name__ == "__main__":
    app.run()
