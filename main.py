import cv2
import process
import recog
import numpy as np
# import model (not working)

#Google's tesseract works but not practical
#will probably have better results if threaded, but it cannot detect
#face cards or aces
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Video settings and output
# FRAME_WIDTH = 3200
# FRAME_HEIGHT = 480
# out = cv2.VideoWriter('output2.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (FRAME_WIDTH, FRAME_HEIGHT))

vid = cv2.VideoCapture(0)
for i in range(30):
        temp = vid.read()

while(True):
    ret, frame = vid.read()

    processedFrame = process.image_prep(frame) 
    ranks = recog.find_cards(processedFrame, frame)
    rankFrames = []
    try:
        #Iterate through all images of ranks to get prediction
        #and process image so it is able to be displayed next to 
        #original frame
        total = 0
        for r in ranks:
            cv2.imshow('a', r)
            #print(model.getPrediction(r))
            # merge = cv2.merge([r, r, r])
            # rankFrames.append(cv2.resize(merge, (640, 480)))
            # num = pytesseract.image_to_string(r, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            # if num != '':
                # total += int(num)
        # cv2.putText(frame, "total=" + str(total), (50,50), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 1, 2)

        cv2.addText()
    except Exception as error:
        print("An exception occurred:", error)
        pass

    #Combines all frames for display/video output
    # processedFrame = cv2.merge([processedFrame, processedFrame, processedFrame])
    # totalFrame = np.concatenate((frame, processedFrame), axis=1)
    # for rankFrame in rankFrames:
        # totalFrame = cv2.hconcat([totalFrame, rankFrame])
    cv2.imshow('final', frame) 

    #Uncomment to write to video file
    # out.write(totalFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()