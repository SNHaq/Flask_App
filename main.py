from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {
    "id": 1, 
    "title": "Buying Groceries", 
    "description": "Milk, Cheese, Pizza"
    }, 
    {
    "id": 2, 
    "title": "Learning Parts of Speech", 
    "description": "Noun, Verb, Adjective"
    }
]

@app.route("/")
def helloWorld():
    return "Hi, I'm Shifa."

@app.route("/get-data")
def getTask():
    return jsonify({
        "data": tasks
    })

@app.route("/add-data", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status": "error", 
            "message": "Please provide the data."
        }, 400)
    task = {
        "id": tasks[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description", ""), 
        "done": False
    }

    tasks.append(task)
    return jsonify({
        "status": "success", 
        "message": "Task added successfully!"
    })

if(__name__ == "__main__"):
    app.run(debug=True)

#The GET Method - GET is used to request data from a specified resource. When you access a website’s 
#page, your browser makes a get request to your API and your API is returning the front-end that is 
#displayed in the browser

#The POST Method - POST is used to send data to the server to create/update a resource

#The PUT Method - PUT is used to send data to a server to create / update a resource. The basic 
#difference between PUT and POST is that a POST request is when you can create multiple copies of the 
#same resource

#The DELETE Method - DELETE is used to delete a resource. The default method used by flask is GET.