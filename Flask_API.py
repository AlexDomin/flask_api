Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # app.py
... from flask import Flask, request, jsonify
... 
... app = Flask(__name__)
... 
... countries = [
...     {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
...     {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
...     {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
... ]
... 
... def _find_next_id():
...     return max(country["id"] for country in countries) + 1
... 
... @app.get("/countries")
... def get_countries():
...     return jsonify(countries)
... 
... @app.post("/countries")
... def add_country():
...     if request.is_json:
...         country = request.get_json()
...         country["id"] = _find_next_id()
...         countries.append(country)
...         return country, 201
...     return {"error": "Request must be JSON"}, 415
SyntaxError: multiple statements found while compiling a single statement
