from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🔥 BARROCO ONLINE FUNCIONA 🔥"

if __name__ == "__main__":
    app.run()