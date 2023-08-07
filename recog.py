import cv2
import numpy as np
import math

#Finds contours, isolates "adult" contours which out the outermost ones
#i.e. the card edges, finds and orients the corners and returns
#rank from corner of card
def find_cards(processedImage, image):
    adultContours = []
    cardCorners = []

    contours, hierarchy = cv2.findContours(processedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    try:
        for c, h in zip(contours, hierarchy[0]):
            if h[3] == -1:
                adultContours.append(c)
 
        for c in adultContours:
            perimeter = cv2.arcLength(c, True)
            corners = cv2.approxPolyDP(c, 0.1 * perimeter, True)
            if cv2.contourArea(corners) > 1000:
                cardCorners.append(corners)

        ranks = []
        for c in cardCorners:
            #Pretty confident this does not do anything,
            #but it might help performance
            if len(c) != 4:
                continue
            c = orient_cards(c)

            #Visual markers and numbers
            for idx, corners in enumerate(c):
                cv2.circle(image, corners[0], 2, (255,0,0), 2)
                cv2.putText(image, str(idx), (corners[0][0], corners[0][1]), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 2, 2)
                
            ortho = np.float32([[0,0], [0,900], [650,900], [650,0]])
            H1, _ = cv2.findHomography(srcPoints=c, dstPoints=ortho)
            warp = cv2.warpPerspective(processedImage, H1, (650,900))
            ranks.append(warp[:140, :140])
        return ranks
    except Exception as error:
    # handle the exception
        # print("An exception occurred:", error)
        pass

def orient_cards(corners):
    dist0to1 = math.dist(corners[0][0], corners[1][0])
    dist1to2 = math.dist(corners[1][0], corners[2][0])
    if (dist0to1 < dist1to2):
        return rotate(corners)
    return corners

def rotate(corners):
    res = np.zeros((4,1,2), dtype=int)
    res[0] = corners[1]
    res[1] = corners[2]
    res[2] = corners[3]
    res[3] = corners[0]
    return res

