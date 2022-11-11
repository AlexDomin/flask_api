# app.py
from flask import Flask, request, jsonify, make_response, abort
import sqlite3
from config import db
from models import Widget, widgets_schema, widget_schema
# conn = sqlite3.connect("widgets.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE widget(name, number_of_parts, created_date, updated_date)")

app = Flask(__name__)

# widgets = [
#     {"id": 1, "name": "Thailand", "number of parts": "Bangkok", "created date": "now", "updated date": "then"},
#     {"id": 2, "name": "Australia", "number of parts": "Canberra", "created date": "now", "updated date": "then"},
#     {"id": 3, "name": "Egypt", "number of parts": "Cairo", "created date": "now", "updated date": "then"},
# ]

def _find_next_id():
    return max(widget["id"] for widget in widgets) + 1

@app.get("/widgets")
def get_widgets():
    return jsonify(widgets)

@app.get("/widgets/<id>")
def get_widget(id):
    return jsonify(widgets[int(id)])

@app.post("/widgets")
def add_widget():
    if request.is_json:
        widget = request.get_json()
        widget["id"] = _find_next_id()
        widgets.append(widget)
        return widget, 201
    return {"error": "Request must be JSON"}, 415

@app.put("/widgets/<id>")
def update_widget(id):
    widget = widgets[int(id)]
    name = request.json['name']
    number_of_parts = request.json['number of parts']
    widget["name"] = name
    widget["number of parts"] = number_of_parts
    
# @app.patch("/widgets/<id>")
# def edit_widget(id):
#     widget = widgets[int(id)]

@app.delete("/widgets/<id>")
def delete_widget(id):
    del widgets[int(id)]
    return {"success": "Requested widget has been successfully deleted!"}, 204
