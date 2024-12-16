from flask import Flask, request, render_template
from lxml import etree

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 1024 * 10

parser = etree.XMLParser(resolve_entities=True, no_network=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/xml", methods=["POST"])
def xml():
    exception = None
    xml_output = None
    xml_input = request.form["xml"]
    if xml_input == "lite XML":
        return "Haha, nej inte så där! Men du kan få en liten bit av flaggan i alla fall: <code>cratectf{xml_</code>"
    try:
        tree = etree.fromstring(xml_input, parser)
        xml_output = etree.tostring(tree).decode("utf-8", errors="replace")
    except Exception as e:
        exception = e
    return render_template("xml.html", xml=xml_output, exception=exception)
