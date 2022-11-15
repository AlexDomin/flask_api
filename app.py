# app.py
from flask import Flask, request, jsonify, make_response, abort, render_template
import sqlite3
from config import db
from models import Widget, widgets_schema, widget_schema
# conn = sqlite3.connect("widgets.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE widget(name, number_of_parts, created_date, updated_date)")

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('widgets.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# widgets = [
#     {"id": 1, "name": "Thailand", "number of parts": "Bangkok", "created date": "now", "updated date": "then"},
#     {"id": 2, "name": "Australia", "number of parts": "Canberra", "created date": "now", "updated date": "then"},
#     {"id": 3, "name": "Egypt", "number of parts": "Cairo", "created date": "now", "updated date": "then"},
# ]

def _find_next_id():
    return max(widget["id"] for widget in widgets) + 1

@app.get("/widgets")
def get_widgets():
    print("a")
    print(Widget)
    print(Widget.query)
    # wd = Widget()
    widgets = Widget.query.all()
    # for widget in widgets:
    #     print(dir(widget))
    return widgets_schema.dump(widgets)

@app.get("/widgets/<id>")
def get_widget(id):
    print("b")
    return jsonify(widgets[int(id)])

@app.post("/widgets")
def add_widget():
    print("c")
    new_widget = widget_schema.load(widget, session=db.session)
    db.session.add(new_widget)
    db.session.commit()
    return widget_schema.dump(new_widget), 201

@app.put("/widgets/<id>")
def update_widget(id):
    print("d")
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
    print("e")
    del widgets[int(id)]
    return {"success": "Requested widget has been successfully deleted!"}, 204
