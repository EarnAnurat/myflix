from application import app, db
from flask import render_template, request, json, Response
from application.models import videopop

videodata = [{"courseID":"1","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}, {"courseID":"6","title":"66","description":"666","credits":6666,"term":"66666"}]

@app.route("/") # root directory

@app.route("/index") #
@app.route("/home") # 
def index():
    return render_template("index.html", index=True)

@app.route("/login") # 
def login():
    return render_template("login.html", login=True)

@app.route("/videocatalog") #
# @app.route("/videocatalog/<vid>") #
def videocatalog():
    videodata = videopop.objects.all()
    return render_template("videocatalog.html", videodata=videodata,videocatalog=True)

@app.route("/register") # 
def register():
    return render_template("register.html", register=True)

@app.route("/vid1", methods=["GET","POST"]) # 
def vid1():
    title = request.args.get('title')
    return render_template("vid1.html", vid1=True, data={"title":title})

@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = videodata
    else:
        jdata = videodata[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")



