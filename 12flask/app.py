

from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
	return "I am Tafheem and CF handle is Kalix1110"

@app.route("/content")
def content():
	return "I am Tafheem and CF handle is Kalix1110 and I am Expert"

if __name__ == "__main__":
	app.run(debug=True)