import os
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from core.processor import Processor

CUR_PATH = os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1])
MODEL_SAVED_AS = 'Model.pickle'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return {'No file part'}
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return '{"error": "No selected file"}'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(os.getcwd())
            file_path = os.path.join(CUR_PATH, app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            model_path = os.path.join(CUR_PATH, 'core', MODEL_SAVED_AS)
            p = Processor(model_path, file_path)
            p.run()
            output_file_path = os.path.join(CUR_PATH, 'output', 'send.csv')
            return send_file(output_file_path, as_attachment=True)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
