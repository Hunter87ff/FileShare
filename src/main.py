import flask, os
from flask import Flask, request, render_template

app = Flask("FileShare")


@app.route("/")
def upload():
    return render_template("form.html")
    return """
    <form action="/fsend" method="POST" enctype="multipart/form-data">
  <input type="file" name="file">
  <input type="submit" value="Upload">
</form>
    """



@app.route('/fsend', methods=['POST'])
def upload_file():
    data = request.form.to_dict()
    print(data)
    file = request.files.get('file').read()

    fn = str(request.files.get('file').filename)
    print(fn)
    with open(fn, "wb") as f:
        f.write(file)
    return "<script>alert('uploaded'); window.location.href='/'</script>"
    return "<script>alert('uploaded')</script>"

#os.system("start chrome http://localhost:8787")
app.run(host="0.0.0.0", port=8787)
