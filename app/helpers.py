"""
This class is build as helper class which contains all the business methods
"""

def extract_info(request):
    """
    This method is used to extract all information which has been
    posted from the request

    :param request: The request has been sent to the server
    :return: info: information has been extracted as a dictionary
    """
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
    return info

def extract_name(request):
    """
        This method is used to extract only name which has been
        posted from the request

        :param request: The request has been sent to the server
        :return: name: name has been extracted as a string
        """
    name = request.form['name']
    return name