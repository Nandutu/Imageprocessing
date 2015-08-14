# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 14:10:15 2015

@author: Django
NANDUTU IRENE 
JAN15/COMP/0573U
"""


import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

# This is the path to the upload directory
UPLOAD_FOLDER = 'C:/Users/Django/classassign/app/uploads/'
# These are the extension that we are accepting to be uploaded and here we shall accept only image formats
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'
])
# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Route that will process the file upload



# Route that will process the file upload
@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
            
                
    # do stuff                   
            
            
    return """
    <!doctype html>
    <title>Upload New File</title>
    <h1>Upload New File</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file>
        <input type=submit value=Upload>
        </form>
       
<body>

<script type='text/javascript'>

function main()
{
    var inputFileToLoad = document.createElement("input");
    inputFileToLoad.type = "file";
    inputFileToLoad.id = "inputFileToLoad";
    document.body.appendChild(inputFileToLoad);

    var buttonLoadFile = document.createElement("button");
    buttonLoadFile.onclick = loadImageFileAsURL;
    buttonLoadFile.textContent = "Load Selected File";
    document.body.appendChild(buttonLoadFile);
}

function loadImageFileAsURL()
{
    var filesSelected = document.getElementById("inputFileToLoad").files;
    if (filesSelected.length > 0)
    {
        var fileToLoad = filesSelected[0];

        if (fileToLoad.type.match("image.*"))
        {
            var fileReader = new FileReader();
            fileReader.onload = function(fileLoadedEvent) 
            {
                var imageLoaded = document.createElement("img");
                imageLoaded.src = fileLoadedEvent.target.result;
                document.body.appendChild(imageLoaded);
            };
            fileReader.readAsDataURL(fileToLoad);
        }
    }
}

main();

</script>

</body>
</form>
</html>
      <p>%s</p>
   """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))
   
 
#this enables us to run the server on the default server port
#http://127.0.0.1:5000/


# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload



if __name__ == "__main__":
    app.run(
    debug=True
  )
