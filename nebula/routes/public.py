# Copyright 2022 iiPython

# Modules
from nebula import app

# Routes
@app.route("/", methods = ["GET"])
def route_index() -> None:
    return "200 OK", 200
