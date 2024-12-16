from flask import current_app as app, render_template, make_response, request, redirect, send_from_directory
import hashlib
import time
import os

allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_."
def checkAllowed(input):
    for c in input:
        if c not in allowedChars:
            return False
    return True

def compile(sessionid, filename):
    makeName = filename.split(".")[0]
    os.system("cd {} && make {} >> activity.log 2>&1".format("app/compiled/{}".format(sessionid), makeName))
    os.system("cd {} && rm {}".format("app/compiled/{}".format(sessionid), filename))

@app.route('/download/<filename>/') 
def download(filename):
    print(os.path.exists("app/compiled/{}/{}".format(request.cookies.get("sessionid"), filename)))
    if request.cookies.get("sessionid") and checkAllowed(filename) and filename != "activity.log" and os.path.exists("app/compiled/{}/{}".format(request.cookies.get("sessionid"), filename)) and checkAllowed(request.cookies.get("sessionid")):
        print("got here")
        return send_from_directory('compiled/{}'.format(request.cookies.get("sessionid")), filename)
    return redirect('/listing')
@app.route('/listing')
def listing():
    if request.cookies.get("sessionid") and os.path.exists("app/compiled/{}".format(request.cookies.get("sessionid"))) and checkAllowed(request.cookies.get("sessionid")):
        files = os.listdir("app/compiled/{}".format(request.cookies.get("sessionid")))
        if len(files) == 0:
            return redirect('/')
        if 'activity.log' in files:
            files.remove('activity.log')
        return render_template('listing.html', len=len(files), files=files)
    
    return redirect('/')
@app.route('/activity')
def activity():
    if os.path.exists("app/compiled/{}/activity.log".format(request.cookies.get("sessionid"))):
        with open("app/compiled/{}/activity.log".format(request.cookies.get("sessionid")), 'r') as file:
            content = file.read()
        return render_template('activity.html', content=content, filename="filename")
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.cookies.get("sessionid") and checkAllowed(request.cookies.get("sessionid")):
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '' or not checkAllowed(file.filename):
            return redirect(request.url)

        if file:
            filename = file.filename
            file.save(os.path.join("app/compiled/{}".format(request.cookies.get("sessionid")), filename))
            compile(request.cookies.get("sessionid"), filename)
            return redirect('/activity')
        
    
    resp = make_response()
    resp.set_data(render_template('index.html'))
    if not request.cookies.get("sessionid") or not os.path.exists("app/compiled/{}".format(request.cookies.get("sessionid"))):
        m = hashlib.sha256()
        m.update(str(time.time()).encode())
        resp.set_cookie('sessionid', m.hexdigest(), max_age=60*60*24*30)
        os.system("mkdir app/compiled/{}".format(m.hexdigest()))
    return resp
    
@app.route('/about')
def about():
    return "This is the about page."