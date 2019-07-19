from math import sin , cos ,radians,atan,sqrt,degrees,atan2
from tqdm import tqdm
import csv

def create_data(x,y,z):
	q1,q2,q3,q4,q5,q6 = 1,2,5,4,7,5	
	row = [str(x), str(y),str(z),"   ",str(q1),str(q2),str(q3),str(q4),str(q5),str(q6)]

	with open('positions.csv', 'a') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(row)

	csvFile.close()


for i in range(20):
	create_data(i,2,3)

#/////////////////////////////////////////////////////////////////////////////
#    This moduel is  calculate 	FORWARD KINEMATIC for use control Robot
#
#	 Pattern of angle :
#    					Down <----( - )---- Q3 ----( + )----> Up
#   				    Down <----( - )---- Q2 ----( + )----> Up
#    					Down <----( + )---- Q1 ----( - )----> Up
#     
#    					Left <----( + )---- Q0 ----( - )----> Rigth
#
#
#/////////////////////////////////////////////////////////////////////////////


class fw_kinemtic:   

	def __init__(self,x_coor,y_coor,z_coor):					# Define valuese
		
		self.x0 = 0
		self.z0 = 3
		self.link_1 = 11
		self.link_2 = 11
		self.link_3 = 19
		self.position_x = x_coor + 0.000001
		self.position_y = y_coor + 0.000001
		self.position_z = z_coor + 0.000001


	def calculate(self,q0,q1,q2,q3):							# calculate coordinate(x,y,z) 
		q2 = q2 *-1
		q3 = q3 *-1
		dis_arm = (self.link_1)*(abs(sin(radians(q1)))) + (self.link_2)*(abs(sin(radians(q1+q2)))) + (self.link_3)*(abs(sin(radians(q1+q2+q3))))	
		#x = dis_arm * (sin(radians(q0)))
		#y = dis_arm * (cos(radians(q0)))
		z =  (self.z0) + (self.link_1)*(cos(radians(q1))) + (self.link_2)*(cos(radians(q1+q2))) + (self.link_3)*(cos(radians(q1+q2+q3)))
		#z = (self.z0) + (self.link_1)*(abs(cos(radians(q1)))) + (self.link_2)*(abs(cos(radians(q1+q2)))) + (self.link_3)*(abs(cos(radians(q1+q2+q3))))	
		
		return dis_arm,z  


	def findPositions(self):									# calculate angle from coordinate(x,y,z) 
		error = 10000
		count = 0 
				
		dis_d = sqrt((self.position_x ** 2) + (self.position_y ** 2))
		q0 = degrees(atan(self.position_y / self.position_x))
		
		for q1 in tqdm(range(-60,90,1)):		 
			for q2 in range(-135,10,1):
				for q3 in range(-90,10,1):		

						a = fw_kinemtic(self.position_x,self.position_y,self.position_z)
						dis,z = a.calculate(q0,q1,q2,q3)
						qt = degrees(atan2(z,dis))
						
						
						er = ((self.position_z - z ) **2)  + ((dis_d - dis)**2) 
						
						if(error >= er and self.position_z < 20 and z > 0 ):
							if( qt <= 90 and qt >= 0 ):
								
									error = er
									count += 1
									Q0 = q0
									Q1 = q1 
									Q2 = q2
									Q3 = q3

								
						'''
						if(self.position_x > 10):
							if( Q2 < 0) : Q2 * -1
							if( Q3 < 0) : Q3 * -1		 
						'''
			
		#print(" (%d , %d , %d)    Z = %d  dis = %d    Q0 = %d  Q1 = %d  Q2 = %d  Q3 = %d    ERROR = %d "%(self.position_x,self.position_y,self.position_z,zr,dr,Q0,Q1,Q2,Q3,error))						
		#print("Qt = %d     Enter loop  = %d" %(qt,count) )
		return	Q0,Q1,Q2,Q3	



	
	





