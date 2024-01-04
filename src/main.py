try:
    import flask, os
    from flask import Flask, request, render_template
except:
    os.system("pip install -r requirements.txt")

app = Flask("FileShare")
app.static_folder = "static"

@app.route("/")
def upload():
    return render_template("form.html")
    return """
    <form action="/fsend" method="POST" enctype="multipart/form-data">
  <input type="file" name="file">
  <input type="submit" value="Upload">
</form>
    """    #it'll run, if the above return isn't working properly



@app.route('/fsend', methods=['POST'])
def upload_file():
    # data = request.form.to_dict()
    # print(data)
    file = request.files['file']  #this is the file
    fn = os.path.join("D:/github/FileShare/src/files/", file.filename)  #change the file path to your file path
    try:
        with open(file.filename, "wb") as f:
            f.write(file.read())   #write and save the file
    except IOError as e:
        return "<script>alert('Unable to upload file, Try again!!'); window.location.href='/'</script>"  #error handelling for file saving
    return "<script>alert('uploaded'); window.location.href='/'</script>"  

#os.system("start chrome http://localhost:8080")  
app.run(host="0.0.0.0", port=8787, debug=False)  #disable the debugger if you want
