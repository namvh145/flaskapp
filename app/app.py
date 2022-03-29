from flask import *
import sqlite3
application = Flask(__name__, template_folder='templates')
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=9001, debug=True)

trusted_ips = ['42.42.42.42', '82.42.82.42', '127.0.0.1']

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
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            gender = request.form["gender"]
            contact = request.form["contact"]
            dob = request.form["dob"]
            address = request.form["address"]
            with sqlite3.connect("student_details.db") as connection:
                cursor = connection.cursor()
                cursor.execute("INSERT into Student_Info (name, email, gender, contact, dob, address) values (?,?,?,?,?,?)",(name, email, gender, contact, dob, address))
                connection.commit()
                msg = "Student details successfully Added"
        except:
            connection.rollback()
            msg = "We can not add Student details to the database"
        finally:
            return render_template("success_record.html",msg = msg)
            connection.close()



@application.route("/delete_student")
def delete_student():
    return render_template("delete_student.html")



@application.route("/student_info")
def student_info():
    connection = sqlite3.connect("student_details.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("select * from Student_Info")
    rows = cursor.fetchall()
    return render_template("student_info.html",rows = rows)



@application.route("/deleterecord",methods = ["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("student_details.db") as connection:

        cursor = connection.cursor()
        cursor.execute("select * from Student_Info where id=?", (id,))
        rows = cursor.fetchall()
        if not rows == []:

            cursor.execute("delete from Student_Info where id = ?",(id,))
            msg = "Student detail successfully deleted"
            return render_template("delete_record.html", msg=msg)

        else:
            msg = "can't be deleted"
            return render_template("delete_record.html", msg=msg)

# import os
# from flask import Flask, request, jsonify
# from flask_pymongo import PyMongo
#
# application = Flask(__name__)
# application.config["MONGO_URI"] = "mongodb://" + os.environ['MONGODB_USERNAME'] + ":" + os.environ['MONGODB_PASSWORD'] \
#                 + "@" + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
#
#
# @application.route('/')
# def index():
#     return jsonify(
#         status=True,
#         message='Welcome to the Dockerized Flask MongoDB app!'
#     )
# if __name__ == "__main__":
#     ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
#     ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
#     application.run(host="localhost", port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
