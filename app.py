import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    # Get the "NAME" variable from the environment
    name = os.getenv("NAME", "World")  # Default to "World" if "NAME" is not set
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)