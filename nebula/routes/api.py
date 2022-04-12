# Copyright 2022 iiPython

# Modules
from nebula import app
from flask import jsonify

# Routes
@app.route("/api/status", methods = ["GET"])
def route_api_status() -> None:
    return jsonify(
        data = app.reader.get_current(),
        status = app.reader.get_overall_status()
    ), 200

@app.route("/api/day/<string:date>", methods = ["GET"])
@app.route("/api/day/<string:date>/<string:service>", methods = ["GET"])
def route_api_day(date: str, service: str = None) -> None:
    data = app.reader.get_date(date)
    if data is None:
        return jsonify(code = 404, message = "Not found"), 404

    elif not service:
        return jsonify(data = data, status = app.reader.get_overall_status(date)), 200

    data = {time: services.get(service, {}) for time, services in data.items()}
    if not any([k for k in data.values() if k]):
        return jsonify(code = 400, message = "Invalid or unknown service"), 400

    return jsonify(data = data), 200
