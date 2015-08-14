import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
from skimage import io
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as 

UPLOAD_FOLDER = 'C:/Users/Django/classassign/app/uploads/'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
'''
# get the path to the script so we can use relative paths
full_path = os.path.realpath(__file__)
script_path, filename = os.path.split(full_path)

def circle(filename):
    #putting lines with in the image
    filename[10:13, 20:23]
    filename[100:120] = 255
    #this creates a circular shape with curved edge at y-axis and x-axis
    lx, ly = filename.shape
    X, Y = np.ogrid[0:lx, 0:ly]
    mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/4
    filename[mask] = 0
    #passing the and passing the line between an x-axis and y-axis
    #while measuring the width and height dimensions of the image
    filename[range(200), range(200)] = 255


    # Jpeg has values of 0-255 we need values normalized of 0.0 - 1.0
    filename =   filename/255

    #This resizes the image
    plt.figure(figsize=(3, 3))
    #this makes the middle grid pure white
    plt.axes([0, 0, 1, 1])
    #this makes the circular part grey
    plt.imshow(  filename, cmap=plt.cm.gray)

    #this removes the axis
    plt.axis('off')

    #displays the image
    plt.show()
'''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/show/<filename>')
def uploaded_file(filename):
    #filename.mask = Image.new('L',(200,200),0)
    #draw = ImageDraw.Draw(filename.mask)
    #draw.ecllipse((0,0)+filename.mask.size, fill=255)


    return render_template('template.html', filename=filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)  

if __name__ == '__main__':
    app.run(debug = True)