import numpy as np
import cv2

class TakePhoto:    
    imgName = ""
    
    def __init__(self, nameOfPicture):
        self.imgName = nameOfPicture
        
        
    def vid(self):
        cap = cv2.VideoCapture( 0 )

        while( True ):
            ret, frame = cap.read()
    
            cv2.imshow( 'Press T to take photo!', frame )
            if cv2.waitKey( 1 ) & 0xFF == ord( 't' ):
                cv2.imwrite(self.imgName+".jpeg",frame)
                break
        
        cap.release()
        cv2.destroyAllWindows()
    