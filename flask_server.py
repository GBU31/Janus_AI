from flask import Flask, request, send_file
from flask_cors import CORS
from flask import render_template
import os
from core.deepfake import *

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html', title='Janus AI')


@app.route('/api', methods=['POST'])
def upload_file():
    os.system('rm -rf DeepFake.mp4 filename.avi pic.jpg')
    os.system('touch filename.avi')
    file = request.files['DeepFake']
    file2 = request.files['pic']
    file3 = request.files['filename.avi']
    file.save('./' + 'DeepFake.mp4')
    file2.save('./' + f'pic{file2.filename[-4:]}')
    file3.save('./' + 'filename.avi')

    DeepFake().run()
    
    try:
        return send_file('filename.avi', as_attachment=True)
    
    except:
       
       return os.popen("ls").read()


if __name__ == '__main__':
    app.run(debug=True)
