from flask import Flask, request, Response, send_file, abort

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 1024

FLAG = "cratectf{inte_för_stort_inte_för_litet}"
TARGET_LENGTH = 124 + 1

too_large_msg = """<!doctype html>
<html lang=en>
<title>413 Request Entity Too Large</title>
<h1>Request Entity Too Large</h1>
<p>The data value transmitted exceeds the capacity limit.</p>"""

too_small_msg = """<!doctype html>
<html lang=en>
<title>418 Request Entity Too Small</title>
<h1>Request Entity Too Small</h1>
<p>The data value transmitted does not exceed the capacity limit.</p>"""

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" in request.files:
        file = request.files["file"]
        file_length = file.seek(0, 2)
        if file_length < TARGET_LENGTH:
            return Response(too_small_msg, status=418)
        if file_length > TARGET_LENGTH:
            return Response(too_large_msg, status=413)
        else:
            return FLAG
    return abort(400)
