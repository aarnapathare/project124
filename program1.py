from distutils.log import debug
from flask import Flask, jsonify, request
app = Flask(__name__)
contacts = [
    {
        "id":1,
        "Name":"name",
        "Contact":"",
        "done":""
    }
]
@app.route("/adddata", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "please provide the data needed"
        }, 400)

    contact = {
        "id":contacts[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact": request.json.get('Contact', ""),
        "done": False
        }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "task added successfully"
    })
@app.route("/getdata")
def gettask():
    return jsonify({
        "data":contacts
    })
if(__name__=="__main__"):
    app.run(debug=True)