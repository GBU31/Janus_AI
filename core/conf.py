class deepfakeconf:
    width = 640
    height = 480
    cap = cv2.VideoCapture("DeepFake.mp4")
    result1=cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 25, (640,480))
    cap.set(3, width)
    cap.set(4, height)

    image = cv2.imread("pic.jpg")

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_face_mesh = mp.solutions.face_mesh