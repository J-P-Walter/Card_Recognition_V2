import cv2

#Standard cv image processing
#Can tweak by chaning the numbers but these seem to work
#well for this project
def image_prep(image):
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurImg = cv2.GaussianBlur(grayImg, (1, 1), 0)
    retval, threshImg = cv2.threshold(blurImg, 127, 255, cv2.THRESH_BINARY)
    return threshImg