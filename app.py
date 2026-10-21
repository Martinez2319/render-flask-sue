from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "API funcionando en Railway"


if __name__ == "__main__":
    app.run()
