from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def func1():
    return render_template("index.html")

@app.route('/success/<int:score>')
def success(score):
    return render_template("success.html", a = score)
@app.route('/fail/<int:score>')
def fail(score):
    return render_template("fail.html", a = score)

@app.route('/submit', methods = ['POST','GET'])
def submit():
    total_score = 0
    if (request.method=='POST'):
        sci = float(request.form['sci'])
        mat = float(request.form['mat'])
        eng = float(request.form['eng'])
        hin = float(request.form['hin'])
        cse = float(request.form['cs'])
        total_score = (sci + mat + eng + hin + cse)/5
    res = ""
    if total_score > 50:
        return redirect(url_for("success", score = total_score))
    else:
        return redirect(url_for("fail", score = total_score))

if __name__ == "__main__":
    app.run(debug = True)