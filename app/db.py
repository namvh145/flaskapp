import os

from pymongo import MongoClient

"""
This module is used to interact with the mongodb 
"""

class StudentMongoClient:
    def __init__(self, host=os.environ['MONGODB_HOSTNAME'],
                port=27017,
                username=os.environ['MONGODB_USERNAME'],
                password=os.environ['MONGODB_PASSWORD'],
                database=os.environ['MONGODB_DATABASE']
                 ):
        self.mongo = MongoClient(host=host, username=username,
                                 port=port, password=password)
        self.db = self.mongo[database]

    def insert_data(self, student_info):
        """
        This method inserts one or more students' info into the student database

        :param student_info: the dictionary or list of dictionary containing all the information of one student
        :return: msg: the message state which will show the status of insertion
        """
        self.db.insert(student_info)
        msg = "The student information has been added successfully!!"
        return msg

    def delete_data(self, name):
        """
        This method delete one or more students' info which has the same name
        as the request sent

        :param name:
        :return: msg: the message state which will show the status of deletion
        """
        q_names = self.db.student.find({"name": name})
        rows = []
        msg = ""
        for student_name in q_names:
            rows.append(student_name)
        if not rows == []:
            self.db.student.delete_many({"name": name})
            msg = "Student details successfully deleted"
        else:
            msg = "can't be deleted"
        return msg

    def get_all_data(self):
        """
        This method retrieves all the information of students available in the
        mongodb server

        :return: a list of students
        """
        rows = []
        all_students_data = self.db.student.find()
        for student_data in all_students_data:
            rows.append(student_data)
        return rows