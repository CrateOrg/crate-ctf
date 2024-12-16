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

def pack(sessionid, filename):
    notExtension = filename.split('.')[0]
   
    base = 0x50
    currentChar = ''
    lastChar = []

    def findDistance(target):
        # this code is spaghetti because im having a brainfreeze figuring out how to do this with clean math, without mixing up 0xff and 0x00
        count = 0
        current = base
        for i in range(0,256):
            if current == target:
                return count
            current += 1
            count += 1
            if current == 256:
                current = 0

    with open(os.path.join("app/compiled/{}".format(request.cookies.get("sessionid")), filename), 'rb') as f1:
        with open(os.path.join("app/compiled/{}".format(request.cookies.get("sessionid")), notExtension + ".packed"), 'wb') as f2:
            try:
                while True:
                    currentByte = ord(f1.read(1))

                    currentChar = findDistance(currentByte).to_bytes(1, 'big')
                    
                    print(currentChar)
                    if len(lastChar) == 0:
                        lastChar = [currentChar, 1]

                    elif currentChar == lastChar[0]:
                        lastChar[1] = lastChar[1] + 1
                    else:

                        f2.write(lastChar[0])
                        f2.write((lastChar[1]).to_bytes(2, 'big'))
                        lastChar[0] = currentChar
                        lastChar[1] = 1
                    #print("going to next round")
            except:
                try:
                    f2.write(lastChar[0])
                    f2.write((lastChar[1]).to_bytes(2, 'big'))
                except:
                    pass

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
        return render_template('listing.html', len=len(files), files=files)
    
    return redirect('/')

@app.route('/unpack')
def unpack():
    return render_template('unpack.html')


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
            pack(request.cookies.get("sessionid"), filename)
            return redirect('/listing')
        
    
    resp = make_response()
    resp.set_data(render_template('index.html'))
    if not request.cookies.get("sessionid") or not os.path.exists("app/compiled/{}".format(request.cookies.get("sessionid"))):
        m = hashlib.sha256()
        m.update(str(time.time()).encode())
        resp.set_cookie('sessionid', m.hexdigest(), max_age=60*60*24*30)
        os.system("mkdir app/compiled/{}".format(m.hexdigest()))
        os.system("cp flag.packed app/compiled/{}".format(m.hexdigest()))
    return resp
