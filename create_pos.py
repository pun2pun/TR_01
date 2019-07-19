import csv
import Arm

def create_data(x,y,z,q1,q2,q3,q4  ):
		
	row = [str(x), str(y),str(z),"   ",str(q1),str(q2),str(q3),str(q4)]

	with open('positions_2.csv', 'a') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(row)

	csvFile.close()


for x in range(23,38,1):
    for y in range(-21,21,1):
       for z in range(0,6,1):
   
                    hu = Arm.fw_kinemtic(x,y,z).findPositions()
                    create_data(x,y,z,hu[0],hu[1],hu[2],hu[3])
   
    print(x)



