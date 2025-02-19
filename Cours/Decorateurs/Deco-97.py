import functools
from flask import Flask, request, abort

app = Flask(__name__)

# ...

@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return "success!"