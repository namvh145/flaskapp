import os
from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient


application = Flask(__name__, template_folder='templates')
# application.config["MONGO_URI"] = "mongodb://" + os.environ['MONGODB_USERNAME'] + ":" + os.environ['MONGODB_PASSWORD'] \
#                 + "@" + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = MongoClient(host=os.environ['MONGODB_HOSTNAME'],
                    port=27017,
                    username=os.environ['MONGODB_USERNAME'],
                    password=os.environ['MONGODB_PASSWORD']
                    )
db = mongo[os.environ['MONGODB_DATABASE']]

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
        name = request.form["name"]
        email = request.form["email"]
        gender = request.form["gender"]
        contact = request.form["contact"]
        dob = request.form["dob"]
        address = request.form["address"]
        info = {
            "name": name,
            "email": email,
            "gender": gender,
            "contact": contact,
            "dob": dob,
            "address": address
        }
        db.student.insert_one(info)
        msg = "The student information has been added successfully!!"
        return render_template("success_record.html", msg=msg)


@application.route("/delete_student")
def delete_student():
    return render_template("delete_student.html")



@application.route("/student_info")
def student_info():
    rows = []
    all_students_data = db.student.find()
    for student_data in all_students_data:
        rows.append(student_data)
    return render_template("student_info.html", rows=rows)



@application.route("/deleterecord",methods = ["POST"])
def deleterecord():
    name = request.form["name"]
    results = db.student.find({"name": name})
    rows = []
    for student in results:
        rows.append(student)
    if not rows == []:
        db.student.delete_one({"name": name})
        msg = "Student detail successfully deleted"
        return render_template("delete_record.html", msg=msg)

    else:
        msg = "can't be deleted"
        return render_template("delete_record.html", msg=msg)

if __name__ == "__main__":
    application.run(debug=False)

