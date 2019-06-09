import requests
import pandas as pd

def to_position(pred):
        i=0
        x = pred
        Y = [0,1]
        if x==1:
            Y[i]="RF"
        elif x==2:
            Y[i]="ST"
        elif x==3:
            Y[i]="LW"
        elif x==4:
            Y[i]="GK"
        elif x==5:
            Y[i]="RCM"
        elif x==6:
            Y[i]="LF"
        elif x==7:
            Y[i]="RS"
        elif x==8:
            Y[i]="RCB"
        elif x==9:
            Y[i]="LCM"
        elif x==10:
            Y[i]="CB"
        elif x==11:
            Y[i]="LDM"
        elif x==12:
            Y[i]="CAM"
        elif x==13:
            Y[i]="CDM"
        elif x==14:
            Y[i]="LS"
        elif x==15:
            Y[i]="LCB"
        elif x==16:
            Y[i]="RM"
        elif x==17:
            Y[i]="LAM"
        elif x==18:
            Y[i]="LM"
        elif x==19:
            Y[i]="LB"
        elif x==20:
            Y[i]="RDM"
        elif x==21:
            Y[i]="RW"
        elif x==22:
            Y[i]="CM"
        elif x==23:
            Y[i]="RB"
        elif x==24:
            Y[i]="RAM"
        elif x==25:
            Y[i]="CF"
        elif x==26:
            Y[i]="RWB"
        elif x==27:
            Y[i]="LWB"
        i = i+1
        return Y[0]

new_arr = [72,20,70,60,55,65,60,70,65,60,60,65,70,70,70,50,70,60,55,55,60,65,50,35,40,59,60,65,36,30,28,4]
new_vals = pd.DataFrame(columns=['Index'])
new_vals = new_vals.append([new_arr])

url = 'http://localhost:5000/api'
print(new_arr)
r = requests.post(url,json={'exp':new_arr,})

pred = to_position(r.json())
print(pred)

#Decode position variable
