from threading import Thread
import cv2
import Arm
import pun
import chang
import time
import readCSV
import tensorflow as tf

global result,coordinate,number_objects,COLOR_s,f_grap

CATEGORIES = ["Cilitical", "Rectangle","Triangle"]
model = tf.keras.models.load_model("Robot_TR0i_mk2.mode")

def prepare(filepath):
    IMG_SIZE = 50 # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)



class conecting_robot:
    def __init__(self,comport,buarate):
        self.speed = 80	
        self.comport = comport
        self.buarate = buarate
        self.result = False
        self.size = 5
        self.coordinate = []
        self.COLOR_s =  [] 
        self.f_grap = 0.4405*(self.size**2) + (1.775*self.size) - 42.06

    def find_oj(self):    
        self.objects = chang.getImage()
        self.number_objects = len(self.objects)
        image_ai = cv2.imread("data/FROM_kinect.jpg")

        for i in range(self.number_objects):
            
            y1 = 0
            y2 = 0
            x1 = 0
            x2 = 0

            positions_x = self.objects[i][1]
            positions_y = self.objects[i][0]

            x1 = positions_y -80
            x2 = positions_y +80
            y1 = positions_x -80
            y2 = positions_x +80

            if(y1<0):y1=0
            if(y1>250):y2=250
            if(x1<0):x1=0
            if(y1>485):x1=485 

            #print("Sections",y1,y2,x1,x2)
            image_ai_check = image_ai[y1:y2,x1:x2]
            cv2.imwrite('data/a'+str(i)+'.jpg',image_ai_check)
            time.sleep(1)


            color = self.objects[i][2]  
            x = ( positions_x / 10 )+12
            y = (( positions_y *-1) /10 ) +25.6

            z = 2
            y=y-5
            print(x,y,z)
            x = readCSV.getPositons(int(x),int(y),int(z))
            self.coordinate.append((x))
            self.COLOR_s.append(color)

        self.fake = ["Tester","Termarind","Can"]
        print("---------------------------- Type --------------------------------")
        for j in range(self.number_objects):
            name = 'data/a'+str(j)+'.jpg'
            prediction = model.predict([prepare(name)])
        
           # print(CATEGORIES[int(prediction[0][0])])
           
            print(self.fake[j])
        print("------------------------------------------------------------------")
    def robotic_work(self):
            self.find_oj()
            
            result_fb = True
            
            number_objects = len(self.coordinate)
            print(number_objects,self.coordinate)
            
            for rounds in range(number_objects):
                x = self.coordinate[rounds]
                color = self.COLOR_s[rounds]
                type_ob = self.fake[rounds]

                pun.Control(self.comport,self.buarate,self.speed).Graper(35)
                time.sleep(1)
                pun.Control(self.comport,self.buarate,self.speed).setReady()
                time.sleep(1)
                pun.Control(self.comport,self.buarate,self.speed).gotoJoint(x[0],x[1],x[2],x[3],45)
                time.sleep(2)

                
                pun.Control(self.comport,self.buarate,self.speed).Graper(self.f_grap)
                time.sleep(2)
                
                pun.Control(self.comport,self.buarate,self.speed).setReady()
                time.sleep(2)

                chang.get_image_feedback() 
                feed_back_pic = cv2.imread("data/feed_back.jpg",0)   
                feed_back_pic = feed_back_pic[10:62,61:78]  
                y =[]
                for i in range(feed_back_pic.shape[0]):
                    for j in range(feed_back_pic.shape[1]):
                        y.append(feed_back_pic[i][j])

                value_detect =sum(y) / (feed_back_pic.shape[0] * feed_back_pic.shape[1])

                if(value_detect <= 150):
                    print("Have" + str(value_detect))
                    result_fb  = True

                   # if( color == 'Green'):pun.Control(self.comport,self.buarate,self.speed).gotoJoint(90,5,-55,-90,45)
                    #if( color == 'Red'):pun.Control(self.comport,self.buarate,self.speed).gotoJoint(-90,5,-55,-90,45)
                    

                    
                    if( type_ob == 'Tester'):pun.Control(self.comport,self.buarate,self.speed).gotoJoint(90,5,-55,-90,45)
                    if( type_ob == 'Termarind'):pun.Control(self.comport,self.buarate,self.speed).gotoJoint(-90,5,-55,-90,45)
                    if( type_ob == 'Can'):pun.Control(self.comport,self.buarate,self.speed).gotoJoint(0,5,-55,-90,45)    

                    time.sleep(2)
                    pun.Control(self.comport,self.buarate,self.speed).Graper(20)
                    time.sleep(2)
                    pun.Control(self.comport,self.buarate,self.speed).setReady()
                    time.sleep(1)

                else:
                    print("dont Have"+ str(value_detect))
                    result_fb  = False
                    pun.Control(self.comport,self.buarate,self.speed).gotoHome()
                    break
            
            self.coordinate = []
            self.COLOR_s =  []     
            
            return result_fb       
   

            
                            

           

    


    def run(self):
            
            #t1 = Thread	(target=chang.getImage)
            t2 = Thread	(target=self.robotic_work)
            result = False
            pun.Control(self.comport,self.buarate,self.speed).gotoHome()
            while(1):
                if(result == False):             
                    result = self.robotic_work()
                else:
                    break

      

