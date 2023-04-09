import numpy as np
from stl import mesh
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
window_name = "Detecting Objects "
original_image = cv2.imread(stream)
time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	stream = frame.array
	cv2.imshow("Frame", stream)
    cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow(window_name, 400, 400)
    cv2.waitKey(0)
    key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
    if key == ord("q"):
         break
    image_grey = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
    cascade_classifier = cv2.CascadeClassifier("phonecascade7tan9lb 3Lih.xml")
    detected_objects = cascade_classifier.detectMultiScale(image_grey, minSize=(50, 50))
    if len(detected_objects) != 0:
        for (x, y, width, height) in detected_objects:
            cv2.rectangle(original_image, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 2)




duty = angle / 18 + 2 

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(2.5)



GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    AVG=0
    for i in range(3):
     while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
     while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
     TimeElapsed = StopTime - StartTime
     distance = (TimeElapsed * 34300) / 2
     AVG=AVG+distance
    return AVG/3

R1=(36,3)
vertices=np.zeros(R1)
R2=(36,3)
faces=np.zeros(R2)
D=distance()
axe-x=[0,width/2,width/2,0,width/2,width/2]
max=height

for i in range(4):
   for j in range(4):
                 if D<=50:
                      vertices[i+j]=[axe-x[i],-(max/6)*j ,D]
                      p.ChangeDutyCycle(45 / 18 + 2)
                      time.sleep(0.5)
                 else:
                       time.sleep(0.5)


 p.ChangeDutyCycle(45 / 18 + 2)
 time.sleep(0.5)

for k in range(36):
 if vertices[k]==[0,0,0] :
     vertices.pop(k)


for l in range(0,len(vertices),2):
    faces[l] = np.array([l, l + 1, l + 6])
    faces[l + 1] = np.array([l + 1, l + 6, l + 7])
for l in range(1,len(vertices),2):
    faces[l] = np.array([l, l + 1, l + 6])
    faces[l + 1] = np.array([l + 1, l + 6, l + 7])




objet1 = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i,f in enumerate(faces):
    for j in range(3):
        objet1.vectors[i][j] = vertices[f[j],:]

objet1.save('objet1.stl')



Show_figure_in_matplotlib

from mpl_toolkits import mplot3d
from matplotlib import pyplot

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

your_mesh = mesh.Mesh.from_file('objet1.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()