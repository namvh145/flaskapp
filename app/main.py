import os
from flask import Flask, request, jsonify, render_template
from pymongo.mongo_client import MongoClient

from db import StudentMongoClient
from helpers import extract_info, extract_name

application = Flask(__name__, template_folder='templates')
db_client = StudentMongoClient()

#
# trusted_ips = ['42.42.42.42', '82.42.82.42', '127.0.0.1']
#
# @app.before_request
# def limit_remote_addr():
#     if request.remote_addr not in trusted_ips:
#         abort(404)  # Not Found


@application.route("/")
def index():
    return render_template("index.html")

@application.route("/add_student")
def add_student():
    return render_template("add_student.html")

@application.route("/saverecord",methods = ["POST","GET"])
def saveRecord():
    if request.method == "POST":
        info = extract_info(request)
        msg = db_client.insert_data(info)
        return render_template("success_record.html", msg=msg)


@application.route("/delete_student")
def delete_student():
    return render_template("delete_student.html")

@application.route("/student_info")
def student_info():
    rows = db_client.get_all_data()
    return render_template("student_info.html", rows=rows)

@application.route("/deleterecord",methods = ["POST"])
def deleterecord():
    name = extract_name(request)
    msg = delete_student(name)
    return render_template("delete_record.html", msg=msg)

if __name__ == "__main__":
    application.run(debug=False)

