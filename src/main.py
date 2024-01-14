# Author : Hunter87
# Github : https://github.com/hunter87ff
# Insta  : https://instagram.com/im_hunter87
# Youtube: https://youtube.com/@hunter87

try:
    import flask, socket, os, qrcode
    from flask import Flask, request, render_template
except:
    os.system("pip install -r requirements.txt")
lgr='\033[1;32m' 
red='\033[0;31m' 
cyan='\033[36m' 
blue='\033[34m'
NC='\033[0m'

def local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        return local_ip
    except Exception as e:
        print(f"Error getting local IP address: {e}")
        return None

app = Flask("FileShare")
app.static_folder = "static"

@app.route("/")
def upload():
    try:return render_template("form.html")
    except:return """
    <form action="/fsend" method="POST" enctype="multipart/form-data">
  <input type="file" name="file">
  <input type="submit" value="Upload">
</form>
    """    #it'll run, if the form template isn't working properly



@app.route('/fsend', methods=['POST'])
def upload_file():
    # data = request.form.to_dict()
    file = request.files['file']
    fn = ""
    if "win" in os.sys.platform:
        fn = os.path.join(os.environ["USERPROFILE"]+r"\Downloads", file.filename)  #file path config is configured for windows. change it based on your os.
    else: fn = file.filename
    try:
        with open(fn, "wb") as f:
            f.write(file.read())   #write and save the file
    except IOError as e:
        return "<script>alert('Unable to upload file, Try again!!'); window.location.href='/'</script>"  #error handelling
    return f"<script>alert('uploaded'); window.location.href='/'</script>"  

url = f"{lgr}URL to send file : {red}http://{local_ip()}:8787{NC}"
if "win" in os.sys.platform:
    url = f"URL to send file : http://{local_ip()}:8787"
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    data = f"{local_ip()}:8787"
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("url_qr.png")
    img.show()
    os.system("del url_qr.png")


print(url)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8787)