# face detection with mtcnn on a photograph
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import time
from picamera import PiCamera
 
# draw an image with detected objects
def draw_image_with_boxes(filename, result_list):
	# load the image
	data = pyplot.imread(filename)
	# plot the image
	pyplot.imshow(data)
	# get the context for drawing boxes
	ax = pyplot.gca()
	# plot each box
	for result in result_list:
		# get coordinates
		x, y, width, height = result['box']
		# create the shape
		rect = Rectangle((x, y), width, height, fill=False, color='red')
		# draw the box
		ax.add_patch(rect)
		# draw the dots
		for key, value in result['keypoints'].items():
			# create and draw dot
			dot = Circle(value, radius=2, color='red')
			ax.add_patch(dot)
	# show the plot
	pyplot.show()

camera = PiCamera();
camera.resolution = (640, 480)
 
filename = 'testjeluc.jpg'
# load image from file
pixels = pyplot.imread(filename)
# create the detector, using default weights
detector = MTCNN()

while True:
    # start timer
    print("start")
    # take snapshot
    camera.capture(filename)
    # load image from file
    pixels = pyplot.imread(filename)
    #start timer
    print("start timer")
    start = int(round(time.time() * 1000))
    # detect faces in the image
    faces = detector.detect_faces(pixels)
    # print detect face time
    print(str(int(round(time.time() * 1000)) - start))
    # display faces on the original image
    draw_image_with_boxes(filename, faces)
