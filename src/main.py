try:
    import flask, os
    from flask import Flask, request, render_template
except:
    os.system("pip install -r requirements.txt")

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
    """    #it'll run, if the above return isn't working properly



@app.route('/fsend', methods=['POST'])
def upload_file():
    # data = request.form.to_dict()
    # print(data)
    file = request.files['file']  
    fn = os.path.join(os.environ["USERPROFILE"]+r"\Downloads", file.filename)  #change the file path to your file path
    try:
        with open(fn, "wb") as f:
            f.write(file.read())   #write and save the file
    except IOError as e:
        return "<script>alert('Unable to upload file, Try again!!'); window.location.href='/'</script>"  #error handelling for file saving
    return f"<script>alert('uploaded'); window.location.href='/'</script>"  


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
