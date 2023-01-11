from application import app, db
from flask import render_template, request, json, Response
from application.models import vid # original
from urllib.request import urlopen
# from application.models import videos # clode

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
    url = "http://34.142.32.93/myflix/videos"
    response = urlopen(url)
    jdata = json.loads(response.read())   
    # print(jdata)
    for index in jdata:
        # print(index)
        for key in index:
            # print(key,index[key])
            if (key=="thumbnail"):
                thumbnail2 = index[key]
                print(thumbnail2)
            if (key=="title"):
                title2 = index[key]
                print(title2)
    
    videodata = vid.objects.all() # original
    # videodata = videos.objects.all() # cloud
    # return render_template("videocatalog.html", videodata=videodata, data2={"title2":title2, "thumbnail2":thumbnail2}, videocatalog=True)
    # return render_template("videocatalog.html", videodata=videodata, data2=jdata, videocatalog=True)
    return render_template("videocatalog.html", data2=jdata, videocatalog=True)

@app.route("/register") # 
def register():
    return render_template("register.html", register=True)

@app.route("/vid1", methods=["GET","POST"]) # 
def vid1():
    url = "http://34.142.32.93/myflix/videos"
    response = urlopen(url)
    jdata = json.loads(response.read())   
    # print(jdata)
    for index in jdata:
        # print(index)
        for key in index:
            # print(key,index[key])
            if (key=="thumbnail"):
                thumbnail2 = index[key]
                print(thumbnail2)
            if (key=="title"):
                title2 = index[key]
                print(title2)

    title = request.args.get('title')
    thumbnail = request.args.get('thumbnail')
    # return render_template("vid1.html", vid1=True, data={"title":title2, "thumbnail":thumbnail2})
    return render_template("vid1.html", vid1=True, data={"title":title, "thumbnail":thumbnail})

# @app.route("/api")
# @app.route("/api/<idx>")
# def api(idx=None):
#     if(idx == None):
#         jdata = videodata
#     else:
#         jdata = videodata[int(idx)]

#     return Response(json.dumps(jdata), mimetype="application/json")

# http://127.0.0.1:5000/api1
@app.route("/api1")
@app.route("/api/<idx>")
def api(idx=None):
    url = "http://34.142.32.93/myflix/videos"
    response = urlopen(url)
    if(idx == None):
        jdata = json.loads(response.read())
    else:
        jdata = videodata[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")

# # http://127.0.0.1:5000/api2
# @app.route("/api2")
# @app.route("/api/<idx>")
# def api(idx=None):
#     url = "http://34.142.32.93/myflix/videos"
#     response = urlopen(url)
#     if(idx == None):
#         jdata = json.loads(response.read())
#     else:
#         jdata = videodata[int(idx)]
    
#     # print(jdata)

#     for index in jdata:
#         # print(index)
#         for key in index:
#             # print(key,index[key])
#             if (key=="thumbnail"):
#                 thumbnail = index[key]
#                 print(thumbnail)
#             if (key=="title"):
#                 title = index[key]
#                 print(title)
#         #    if (key !="_id"):
#         #        print (index[key])
#             #    for key2 in index[key]:
#                 # print (key2,index[key][key2])
#                 #   print (key2,index[key][key2])
#                 #   if (key2=="Name"):
#                 #       video=index[key][key2]
#                 #   if (key2=="file"):
#                 #       videofile=index[key][key2]
#                 #   if (key2=="pic"):
#                 #       pic=index[key][key2]
            
#     return Response(json.dumps(jdata), mimetype="application/json")



