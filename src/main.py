# Author : Hunter87
# Github : https://github.com/hunter87ff
# Insta  : https://instagram.com/im_hunter87
# Youtube: https://youtube.com/@hunter87
lgr='\033[1;32m' 
red='\033[0;31m' 
cyan='\033[36m' 
blue='\033[34m'
NC='\033[0m'



import flask, socket, os, qrcode, webview,threading
from flask import Flask, request, render_template, redirect


#cur_dir = os.path.dirname(__file__)
#os.chdir(cur_dir)


def local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        return local_ip
    except Exception as e:
        print(f"Error getting local IP address: {e}")
        return None

app = Flask("FileShare", static_folder = "static")

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/upload")
    return render_template('form.html'), 404

@app.route("/upload")
def upload():
    try:return render_template("form.html")
    except:return """
                    <form action="/fsend" method="POST" enctype="multipart/form-data">
                    <input type="file" name="file">
                    <input type="submit" value="Upload">
                    </form>
    """


@app.route("/")
def qrimg():
        return render_template("qrcode.html")



@app.route('/fsend', methods=['POST'])
def upload_file():
    file = request.files['file']
    fn = ""
    if "win" in os.sys.platform:
        fn = os.path.join(os.environ["USERPROFILE"]+r"\Downloads", file.filename)
    else: fn = file.filename
    try:
        with open(fn, "wb") as f:
            f.write(file.read())
            print(f"File saved as {fn}")
    except IOError as e:
        return "<script>alert('Unable to upload file, Try again!!'); window.location.href='/'</script>"  #error handelling
    return f"<script>alert('uploaded'); window.location.href='/'</script>"  

url = f"{lgr}URL to send file : {red}http://{local_ip()}:8787{NC}"
if "win" in os.sys.platform:
    url = f"URL to send file : http://{local_ip()}:8787"
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    data = f"{local_ip()}:8787/upload"
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(r"static/url_qr.png")
    #img.show()
    #os.system(r'del "static\url_qr.png"')


def loop1():
    app.run(host="0.0.0.0", port=8787)

thread1 = threading.Thread(target=loop1)
thread1.start()
webview.create_window('FileShare', app)
webview.start(debug=False)