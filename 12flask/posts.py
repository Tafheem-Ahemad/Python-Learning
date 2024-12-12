

from flask import Flask,render_template,request

# Create App
app=Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")


# Get method
@app.route("/success",methods=["GET","POST"])
def success():
	if(request.method=="POST"):
		name=request.form['Name']
		return f"Your name is {name}"
	return render_template("success.html")

@app.route("/result",methods=["GET","POST"])
def result():
	if(request.method=="POST"):
		mark=int(request.form['mark'])
		if(mark<50):
			return f"Your mark is {mark} and you are fail!!"
		else :
			return f"Your mark is {mark} and you are Pass!!"
		
	return render_template("mark_input.html")


if __name__ == "__main__" :
	app.run(debug=True)