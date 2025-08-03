from flask import Flask, request, jsonify, redirect, abort
from app.utils import is_valid_url
from app.storage import save_url, get_url_data, increment_clicks

app = Flask(__name__)

@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    url = data.get("url")

    if not url or not is_valid_url(url):
        return jsonify({"error": "Invalid or missing URL"}), 400

    short_code, short_url = save_url(url)
    return jsonify({"short_code": short_code, "short_url": short_url}), 201

@app.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    data = get_url_data(short_code)
    if not data:
        abort(404)
    
    increment_clicks(short_code)
    return redirect(data["url"], code=302)

@app.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    data = get_url_data(short_code)
    if not data:
        abort(404)

    return jsonify({
        "url": data["url"],
        "clicks": data["clicks"],
        "created_at": data["created_at"]
    })
