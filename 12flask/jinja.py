
from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
	return "I am Tafheem and CF handle is Kalix1110"

@app.route("/content")
def content():
	return "I am Tafheem and CF handle is Kalix1110 and I am Expert"

@app.route("/result/<int:mark>")
def result(mark):
	return render_template("result.html",mark=mark)

@app.route("/scoreboard",methods=["GET","POST"])
def scoreboard():
	if(request.method=="POST"):
		total_sum=0;
		total_sum+=int(request.form['math'])
		total_sum+=int(request.form['physics'])
		total_sum+=int(request.form['chemistry'])
		total_sum+=int(request.form['SSC'])

		return redirect(url_for("result",mark=total_sum))
	else :
		return render_template("all_mark_input.html")

if __name__ == "__main__":
	app.run(debug=True)