
from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

items=[
	{"id":1,"description":"This is item 1","task":"Task 1"},
	{"id":2,"description":"This is item 2","task":"Task 2"}
]

@app.route("/")
def home():
	return "This is a API"

@app.route("/items",methods=["GET"])
def get_items():
	return jsonify(items)

@app.route("/items/<int:id>",methods=["GET"])
def get_item(id):
	item=next((item for item in items if item['id']==id),None)
	if(item is None): 
		return jsonify({"error":"Not Found"})
	return jsonify(item)


# Add new task
@app.route("/items",methods=["POST"])
def add_new():
	if(not request.json or not "task" in request.json):
		return jsonify({"error":"Not Found"})
	
	item={
		"id":items[-1]["id"]+1 if items else 1,
		"task":request.json['task'],
		"description" : request.json['description']
	}

	items.append(item)
	return jsonify(items)

# Update the tasks
@app.route("/items",methods=["PUT"])
def update_item():
	if(not request.json or not "id" in request.json):
		return jsonify({"error":"Not Found"})
	
	id=request.json["id"]
	item=next((item for item in items if item['id']==id),None)

	if(item is None): return jsonify({"error":"Not Found ID"})

	item['task']=request.json.get('task',item['task'])
	item['description']=request.json.get('description',item['description'])

	return jsonify(items)

# Delete the task
@app.route("/items/<int:id>",methods=["DELETE"])
def delte_iten(id):
	global items
	items[:]=[item for item in items if item['id'] != id]
	return jsonify(items)


if __name__ == "__main__":
	app.run(debug=True)