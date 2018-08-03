# Create a file that uses takes the video and separates each it into the images
# TF 02/08/18

import cv2
import numpy as np
import os

# video_location = '../Documents/"SCANNER 2018 VIDEO"/"70093 WARWICKSHIRE"'

# Playing video from file:
video = cv2.VideoCapture('A38_NB_YR2_R09_180519132259.avi')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
frame_exists = True
while(frame_exists):
    # Capture frame-by-frame
    ret, frame = video.read()
    if ret == False:
        frame_exists = False
    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    # To stop duplicate images
    currentFrame += 1
    

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()
