import csv

pos_all = []
with open('positions_2.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        pos_all.append(row)
csvFile.close()

round_find = int(len(pos_all))


def getPositons(x,y,z):
    for x_pos in range(1,round_find,1):  
        #print(x_pos)
        if( pos_all[x_pos][0] == str(x) and pos_all[x_pos][1] == str(y) and pos_all[x_pos][2] == str(z) ):
        
            val_angle_q0 = float(pos_all[x_pos][4])
            val_angle_q1 = float(pos_all[x_pos][5])
            val_angle_q2 = float(pos_all[x_pos][6])
            val_angle_q3 = float(pos_all[x_pos][7])
            
            break
    return val_angle_q0,val_angle_q1,val_angle_q2,val_angle_q3
    



