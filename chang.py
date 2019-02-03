from pykinect import nui
import numpy 
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import imutils


def auto_canny(image, sigma=0.33):
        v = np.median(image)
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edgeds = cv2.Canny(image, lower, upper)

        return edgeds



def processImage_2():
    try:

        pic_raw = cv2.imread('data/FROM_kinect.jpg')

        pic = pic_raw[150:440,70:570]
        cv2.imwrite('data/crop.jpg',pic)

        img = cv2.imread('data/crop.jpg')

        x = []
        y = []
            
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        edges = auto_canny(gray)
        cv2.imwrite('data/rescale.jpg',edges)  

        x_pic_num = edges.shape[0]
        y_pic_num = edges.shape[1]

        print(x_pic_num,y_pic_num)


        for i in range(10,x_pic_num-5,1):
            for j in range(10,y_pic_num-5,1):
                if( edges[i][j] != 0):
                    x.append(i)
                    y.append(j) 
                
        codinate_x_1 = x[0]
        codinate_y_1 = y[0]

        codinate_x_2 = x[len(x)-1]
        codinate_y_2 = y[len(x)-1]

        

        position_x = ( codinate_x_1 + codinate_x_2 ) / 2 
        position_y = ( codinate_y_1 + codinate_y_2 ) / 2 

        delta_x = abs(codinate_x_2 - codinate_x_1)
        color_object = img[int(position_x)][int(position_y)]


        cv2.imwrite('data/crop_ob.jpg',pic)
        #print(codinate_x_1,codinate_x_2)
        #print(codinate_y_1,codinate_y_2)
        #print(position_x,position_y) 
        return position_x , position_y ,color_object[1],color_object[2],delta_x

    except:
        print(" In Chang ERROR function -- processImage_2")



# ฟังชั่นช่วยในการรับรูปของกล้อง KINECT
def video_handler_function(frame):
    try:

        kernel = np.ones((5,5),np.uint8)
        video = numpy.empty((480,640,4),numpy.uint8)
        frame.image.copy_bits(video.ctypes.data)

        image = video[150:400,85:570]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold( blurred,175,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]


        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        global pos 
        pos =  []
        text_color = ''

        for c in cnts:
        
            M = cv2.moments(c)
            
            cX = int(M["m10"] / (M["m00"]+0.0000000001))
            cY = int(M["m01"] / (M["m00"]+0.0000000001))
        
            color = image[cY][cX]
            
            if(color[2] > color[1]):
                text_color = 'Red'
            if(color[2] < color[1]):
                text_color = 'Green'

            pos.append((cX,cY,text_color))
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv2.circle(image, (cX, cY), 2, (255, 255, 255), -1)
            cv2.putText(image, text_color, (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
        
        cv2.imshow('KINECT Video Stream', video)
        cv2.imwrite('data/FROM_kinect.jpg',image)
        

    
    except:
        print('Get data from KINECT ERROR')
    

# ฟังก์ชั่นในการรับภาพของกล้อง KINECT
def getImage():
    try:
        kinect = nui.Runtime()
        kinect.video_frame_ready += video_handler_function
        kinect.video_stream.open(nui.ImageStreamType.Video, 2,nui.ImageResolution.Resolution640x480,nui.ImageType.color)
        cv2.namedWindow('KINECT Video Stream', cv2.WINDOW_AUTOSIZE)


        while True:
            key = cv2.waitKey(1)
            if key == ord(' '): 
                print(" Get Image -- Succesfully !!")
                print(pos)
                break

        kinect.close()
        cv2.destroyAllWindows()
        return pos

    except:
        print(" In Chang ERROR function -- getImage")




# ฟังก์ชั่ที่ใช้ปรับความละเอียดภาพ (ปกติใช้ 64x48 pixel)
def rescale(frames,percent = 75):

    width = 450
    hight = 340
    dim = (width,hight)

    return cv2.resize(frames,dim,interpolation = cv2.INTER_AREA)   


#-----------------------------------------------------------------------------------------------

# ฟังก์ชั่ที่ใช้ประมวลผลภาพที่ได้ 
def processImage():
    try:
        print("\n\n********** RESULT PROCESSIMAGE ********** \n\n")
        max= np.array([255,150,97])
        min= np.array([50,44,53])
        pic_raw = cv2.imread('data/FROM_kinect.jpg')
        pic_raw = cv2.inRange(pic_raw,min,max)

        pic = pic_raw[114:437,88:560]
        cv2.imwrite('data/crop.jpg',pic)
        pic1 = rescale(pic,percent=10)
        print(" Rescale -- Succesfully !!")

    

        cv2.imwrite('data/rescale.jpg',pic1)  
        
        img = cv2.imread('data/rescale.jpg')

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite('data/gray.jpg',gray)
        ret, thresh =cv2.threshold(gray,55,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        cv2.imwrite('data/thesho.jpg',thresh)
        print(" Convert and Fix theshold -- Succesfully !!")


        # noise removal
        kernel = np.ones((3,3),np.uint8)
        opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
        cv2.imwrite('data/noise_rm.jpg',opening)
        print(" Remove noise -- Succesfully !!")

        # sure background area
        sure_bg = cv2.dilate(opening,kernel,iterations=3)
        print(" Sure background area -- Succesfully !!")

        # Finding sure foreground area
        dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
        ret, sure_fg = cv2.threshold(dist_transform,0.05*dist_transform.max(),255,0)
        ret, sure_fg_pix = cv2.threshold(dist_transform,0.98*dist_transform.max(),255,0)
        print(" Finding sure foreground area -- Succesfully !!")

        # Finding unknown region
        sure_fg = np.uint8(sure_fg)
        unknown = cv2.subtract(sure_bg,sure_fg)
        cv2.imwrite('data/pi.jpg',sure_fg )
        cv2.imwrite('data/pixel.jpg',sure_fg_pix )
        print(" Finding unknown region -- Succesfully !!")

    except:
        print(" In Chang ERROR function -- processImage")    
    #----------------------------------------------------------------------------------------       
    




def calculateDistance():
    
    try:

        image = cv2.imread('data/pixel.jpg')

        print("********** POSITOINS OF PICTURE ********** \n\n")
        x=y=0
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                b, g, r = image[i, j]
                if(b == 255 and g == 255 and r == 255):
                # print(b, g, r) # 152 222 148	
                    #print(str(i)+'x'+str(j))
                    x = i /10
                    y = j /10
                    #print("\n")
        print(x,y)
        x= x-3
        y= (y-20) *-1           	
        return (x,y)

    except:
        print(" In Chang ERROR function -- calculateDistance")

def whatYouSee():
    try:
        pic = cv2.imread('data/Test.jpg')
        pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
        pic1 = cv2.imread('data/rescale.jpg')
        pic1 = cv2.cvtColor(pic1,cv2.COLOR_BGR2RGB)
        pic2 = cv2.imread('data/noise_rm.jpg')
        pic3 = cv2.imread('data/pixel.jpg')        
        plt.title("I am see")
        plt.subplot(221)
        plt.imshow(pic)
        plt.subplot(222)
        plt.imshow(pic1)
        plt.subplot(223)
        plt.imshow(pic2)
        plt.subplot(224)
        plt.imshow(pic3)
        plt.show()
    except:
        print(" In Chang ERROR function -- whatYouSee")



