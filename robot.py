from pyax12.connection import Connection
import time

#กำหนด ID ของมอเตอร์แต่ละตัว
motor_1 = 7
motor_2 = 11
motor_3 = 12
motor_4 = 13
motor_5 = 15
motor_6 = 18

#กำหนดความเร็วในการหมุนของ Motor (0 - 512)
speed = 100

try:
#ตั้งค่าการเชื่อต่อกับแขนกลผ่าน USB (Port ใช้ตาม DeviceManager, Baudrate = 1000000)
    serial_connection = Connection(port="COM4", baudrate=1000000)
    #หน่วงเวลาป้องกันระบบแฮ้ง
    time.sleep(0.5)
    print("\n\n********** ROBOT START **********\n\n")
except:
    print("Please connect USB or Power ! :( ")  

def connectDisable():
    #ปิดการเชื่อมต่อ USB
    serial_connection.close()    
    print("Dis-connected !!")

def grapOn(p6):
    serial_connection.goto(motor_6, p6, speed=speed, degrees=True)


#สแกนหา Motor ที่กำลังออนไลน์อยู่
def scanMotor():
    
    # Ping the dynamixel unit(s)
    ids_available = serial_connection.scan()

    for dynamixel_id in ids_available:
        print(dynamixel_id)

  
    
    

#สร้างฟังก์ชันในการกลับสู่ตำแหน่งเริ่มต้น
def gotoHome():
    
   
    

    serial_connection.goto(motor_5, 45, speed=speed+20, degrees=True)
    time.sleep(1.5)
    serial_connection.goto(motor_6,0, speed=speed, degrees=True)      
    serial_connection.goto(motor_3,-130, speed=speed, degrees=True)
    serial_connection.goto(motor_2,-90, speed=speed, degrees=True)
    time.sleep(3)
    serial_connection.goto(motor_1,-90, speed=speed, degrees=True)
    time.sleep(1)
    serial_connection.goto(motor_4, -90, speed=speed, degrees=True) 
    
    
    
  
    time.sleep(1)
    print("Go to home already !")
    
   
    

#สร้างฟังก์ชันในการเคลื่อนที่ของแขนตามข้อ(Joint)
def gotoJoint(p1,p2,p3,p4,p5):
    '''
    PARAMITER ของฟังก์ชั่น
        p1 = ตำแหน่งขององศาของ Motor ตัวที่ 1 (-150 ถึง 150)
        p2 = ตำแหน่งขององศาของ Motor ตัวที่ 2 (-150 ถึง 150)
        p3 = ตำแหน่งขององศาของ Motor ตัวที่ 3 (-150 ถึง 150)
        p4 = ตำแหน่งขององศาของ Motor ตัวที่ 4 (-150 ถึง 150)
        p5 = ตำแหน่งขององศาของ Motor ตัวที่ 5 (-150 ถึง 150)
         
    '''
    time.sleep(0.5)
    serial_connection.goto(motor_1,p1, speed=speed, degrees=True)
    serial_connection.goto(motor_2,p2, speed=speed, degrees=True)
    serial_connection.goto(motor_3,p3, speed=speed, degrees=True)
    serial_connection.goto(motor_4,p4, speed=speed, degrees=True)
    serial_connection.goto(motor_5,p5, speed=speed, degrees=True)
    time.sleep(1)
    print("Axis M1 = " +str(p1)+" , "+"Axis M2 = " +str(p2)+" , "+"Axis M3 = " +str(p3)+" , "+"Axis M4 = " +str(p4)+" , "+"Axis M5 = " +str(p5) )
    



def testMark_1():
    setReady()
    time.sleep(1.5)
    gotoJoint(-3,55,-45,20,45)
    grapOn(30)
    time.sleep(1.5)
    grapOn(-20)
    setReady()

def setReady():  
    gotoJoint(0,-60,-90,-90,45)  


