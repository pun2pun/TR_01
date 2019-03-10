from tkinter import *
import pun
import Arm


root = Tk()
root.title("Control Robot :) - TR_01")
root.geometry('1080x350')


comPort_label        = Label(root, text = "   Com port : ").grid(row = 1, column = 1)
bps_label            = Label(root, text = "   Buadrate :").grid(row = 2, column = 1)
speed_label          = Label(root, text = "   Speed    : ").grid(row = 3, column = 1)
theta    = Label(root,text = str(0) +"\t"+str(0)+ "\t"+str(0)+"\t"+ str(0)+"             ").grid(row = 2, column = 4  ) 

info_1 = Label(root,text = "A study and development of artificial intelligence system for industrial robot arm").grid(row = 1, column = 6)
info_2 = Label(root,text = "by").grid(row = 2, column = 6)
info_3 = Label(root,text = "PUNPUN - LEKTA - SELF").grid(row = 3, column = 6)
info_4 = Label(root,text = "Consultants").grid(row = 4,column = 6)
info_4 = Label(root,text = "Dr.Thummaros Rugthum").grid(row = 7, column = 6)



space   = Label(root, text = " ").grid(row = 5, column = 1)
X       = Label(root, text = "Position X :").grid(row = 6, column = 1)
Y       = Label(root, text = "Position Y :").grid(row = 7, column = 1)
Z       = Label(root, text = "Position Z :").grid(row = 8, column = 1)


entry_port      = Entry(root)
entry_port.grid(row = 1, column = 2)
entry_bps       = Entry(root)
entry_bps.grid(row = 2, column = 2)
entry_speed     = Entry(root)
entry_speed.grid(row = 3, column = 2)


entry_x         = Entry(root)
entry_x.grid     (row = 6, column = 2 )
entry_y         = Entry(root)
entry_y.grid     (row = 7, column = 2 )
entry_z         = Entry(root)
entry_z.grid     (row = 8, column = 2 )
#------------------------------------------------------------FUNCTION FOR BUTTON---------------------------------------------
def grapOn(event):
    try:
        port  = entry_port.get()
        bps   = int(entry_bps.get())
        speed = int(entry_speed.get())
        
        pun.Control(port,bps,speed).Graper(0)
    except:
        print("  ")
def grapOff(event):
    try:
        port  = entry_port.get()
        bps   = int(entry_bps.get())
        speed = int(entry_speed.get())
        
        pun.Control(port,bps,speed).Graper(30)
    except:
        print("  ")        

def readyPosition(event):
    try:
        port  = entry_port.get()
        bps   = int(entry_bps.get())
        speed = int(entry_speed.get())
        
        pun.Control(port,bps,speed).setReady()
    except:
        print("  ")


def gotoHome(event):
    try:
        port  = entry_port.get()
        bps   = int(entry_bps.get())
        speed = int(entry_speed.get())
        
        pun.Control(port,bps,speed).gotoHome()
    except:
        print("  ")
def gotoPoint(event):
    try:
        port  = entry_port.get()
        bps   = int(entry_bps.get())
        speed = int(entry_speed.get())
        x_cor = int(entry_x.get())
        y_cor = int(entry_y.get())
        z_cor = int(entry_z.get())

   
        q0,q1,q2,q3 = Arm.fw_kinematic(x_cor,y_cor,z_cor).findPositions()

        theta    = Label(root,text = str(q0) +"\t"+str(q1)+ "\t"+str(q2)+"\t"+ str(q3)+"             ").grid(row = 2, column = 4  )     
        pun.Control(port,bps,speed).gotoJoint(q0,q1,q2,q3,45)

    
    except:
        theta    = Label(root,text = "Try agian ! I's out more range          ").grid(row = 2, column = 4)


#------------------------------------------------------------------BUTTON----------------------------------------------------

button_robo_set_ready = Button(root,text=" Set Ready ")
button_robo_set_ready.bind("<Button-1>", readyPosition)
button_robo_set_ready.grid(row = 6, column = 3)

button_robo_set_ready = Button(root,text="GO to Home ")
button_robo_set_ready.bind("<Button-1>", gotoHome)
button_robo_set_ready.grid(row = 7, column = 3)

button_robo_set_ready = Button(root,text=" Go to Point ")
button_robo_set_ready.bind("<Button-1>", gotoPoint)
button_robo_set_ready.grid(row = 8, column = 3)


button_robo_set_ready = Button(root,text=" Grap ON ")
button_robo_set_ready.bind("<Button-1>", grapOn)
button_robo_set_ready.grid(row = 9, column = 3)


button_robo_set_ready = Button(root,text=" Grap OFF ")
button_robo_set_ready.bind("<Button-1>", grapOff)
button_robo_set_ready.grid(row = 10, column = 3)
#-----------------------------------------------------------------------------------------------------------------------





root.mainloop()

