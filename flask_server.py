from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_file():
    os.system('rm -rf DeepFake.mp4 filename.avi pic.jpg')
    file = request.files['DeepFake']
    print(request.files)
    file2 = request.files['pic']
    file.save('./' + 'DeepFake.mp4')
   
    file2.save('./' + f'pic{file2.filename[-4:]}')
    os.system("python3 main.py")
    return send_file('filename.avi', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)