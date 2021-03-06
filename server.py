from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/dojo")
def dojo():
    return f"Dojo"

@app.route("/say/<name>")
def hi_name(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:num>/<word>")
def repeat_x(num, word):
    return f"{word * int(num)}" 


if __name__=="__main__":
    app.run(debug=True)