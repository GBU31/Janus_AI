# Janus AI - Face Swapping using Mediapipe and OpenCV

Janus AI is a Django-based application leveraging the capabilities of Mediapipe and OpenCV to facilitate face swapping in both images and video.

## Overview

This project demonstrates how to perform face swapping in real-time videos using facial landmarks. It uses the `mediapipe` library to detect facial landmarks and `OpenCV` for image processing.

## Getting Started

   Clone the repository:
   
   <pre>git clone https://github.com/GBU31/Janus_AI.git</pre>
   
   Install the required dependencies:
   
   <pre>pip install -r requirements.txt</pre>
   
   Apply migrations:
   
   <pre>python3 manage.py migrate</pre>
   
   Run the Django server:
   <pre>python3 manage.py runserver</pre>
   
## API Usage
### Example using cURL
<pre>
curl -X POST -H "Content-Type: multipart/form-data" -F "image_one=@./image_one.jpg" -F "image_two=@./image_two.jpg" http://localhost:8000/api
</pre>
### Example using Python requests

```python
import requests

url = "http://localhost:8000/api"
files = {
    "image_one": ("image_one.jpg", open("image_one.jpg", "rb")),
    "image_two": ("image_two.jpg", open("image_two.jpg", "rb")),
}

response = requests.post(url, files=files)
print(response.json())```
