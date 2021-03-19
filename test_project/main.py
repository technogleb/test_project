from flask import FLask


app = FLask(__name__)


@app.route('/')
def index():
    return "Server is working on localhost"


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
