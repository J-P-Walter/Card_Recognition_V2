import cv2
import process
import recog
import numpy as np
# import model (not working)

#Video settings and output
# FRAME_WIDTH = 3200
# FRAME_HEIGHT = 480
# out = cv2.VideoWriter('output2.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (FRAME_WIDTH, FRAME_HEIGHT))

vid = cv2.VideoCapture(0)
for i in range(30):
        temp = vid.read()

while(True):
    ret, frame = vid.read()

    processedFrame = process.imagePrep(frame) 
    ranks = recog.findCards(processedFrame, frame)
    rankFrames = []
    try:
        #Iterate through all images of ranks to get prediction
        #and process image so it is able to be displayed next to 
        #original frame
        for r in ranks:
            #print(model.getPrediction(r))
            merge = cv2.merge([r, r, r])
            rankFrames.append(cv2.resize(merge, (640, 480)))
    except Exception as error:
        # print("An exception occurred:", error)
        pass

    #Combines all frames for display/video output
    processedFrame = cv2.merge([processedFrame, processedFrame, processedFrame])
    totalFrame = np.concatenate((frame, processedFrame), axis=1)
    for rankFrame in rankFrames:
        totalFrame = cv2.hconcat([totalFrame, rankFrame])
    cv2.imshow('final', totalFrame)

    #Uncomment to write to video file
    # out.write(totalFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()