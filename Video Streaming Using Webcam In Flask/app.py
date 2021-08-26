# https://jdhao.github.io/2019/07/06/python_opencv_pil_image_to_bytes/
# https://github.com/krishnaik06/Flask-Web-Framework/blob/main/Tutorial%207/app.py
# https://stackoverflow.com/questions/63362371/how-to-stop-a-flask-video-streamer


from flask import Flask , render_template , request , redirect , url_for , Response
import cv2

app = Flask(__name__)

face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')



# Create a VideoCapture object and read
cap = cv2.VideoCapture(0)
# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video stream or file")


# The function yields frame formatted as a response chunk with a content type of image/jpeg
def generate_frames():

    while True:
        res , frame = cap.read()
        if res == False:
            print("Stream Ended Unexpectedly")
            break

        else:
            # OpenCV Face And Eye Detection In Flask Web Framework
            gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray , 1.1 , 3)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame , (x, y) , (x+w, y+h) , (255, 0, 0) , 2)

                roi_gray = gray[y:y+h , x:x+w]
                roi_frame = frame[y:y+h , x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray , 1.1 , 3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_frame , (ex, ey) , (ex+ew, ey+eh) , (0, 255, 0) , 2)

                
            # Encodes an image into a memory buffer - encodes image in a one-dimension Numpy array in specified format
            # compress image data format to facilitate network transmission
            ret , buffer = cv2.imencode('.jpg' , frame)
            # converts to binary format on disk
            frame = buffer.tobytes()


        # keep generating frames
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def display():
    return render_template('index.html')



# #Video streaming route. Put this in the src attribute of an img tag
@app.route('/video')
def video():
    return Response(generate_frames() , mimetype = 'multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(debug = True)