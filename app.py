
import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename


# This is the path to the upload directory
UPLOAD_FOLDER = 'C:/Users/Django/classassign/app/uploads/'

# These are the extension that we are accepting to be uploaded and here we shall accept only image formats
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# For a given file, it returns whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# Route that will process the file upload
@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        file = request.files['file']
         # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
          # We Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            # Move the file form the temporal folder to the uploads
            # folder we setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index', filename=filename))

    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
        </form>
      <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))


#this enables us to run the server on the default server port
#http://127.0.0.1:5000/
if __name__ == "__main__":
    app.run(
    debug=True)
