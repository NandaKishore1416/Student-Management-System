from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config.from_pyfile("config.py")
db=SQLAlchemy(app)

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    roll=db.Column(db.String(20),unique=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(120))
    dept=db.Column(db.String(50))

@app.before_request
def init():
    db.create_all()

@app.route("/")
def home():
    return redirect("/students")

@app.route("/students")
def students():
    return render_template("students.html",students=Student.query.all())

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        s=Student(roll=request.form["roll"],name=request.form["name"],email=request.form["email"],dept=request.form["dept"])
        db.session.add(s);db.session.commit()
        return redirect(url_for("students"))
    return render_template("add_student.html")

@app.route("/delete/<int:id>")
def delete(id):
    s=Student.query.get_or_404(id)
    db.session.delete(s);db.session.commit()
    return redirect(url_for("students"))

@app.route("/edit/<int:id>",methods=["GET","POST"])
def edit(id):
    s=Student.query.get_or_404(id)
    if request.method=="POST":
        s.roll=request.form["roll"];s.name=request.form["name"];s.email=request.form["email"];s.dept=request.form["dept"]
        db.session.commit()
        return redirect(url_for("students"))
    return render_template("edit_student.html",s=s)

if __name__=="__main__":
    app.run(debug=True)
