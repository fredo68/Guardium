import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import datetime

def fred(str):
    if str=='Merge process - DONE':
        global int
        int = int + 1
        return(int)
    else:
        return(int)    

dir = "/home/fredo/"

data = pd.read_csv(dir+"AAL.csv", sep = ",")

print(data.head() )
datam=data.loc[data['Activity Type']=='Merge process' ]
datam2=datam.loc[datam['Status']=='Succeeded']


datam2['Start Time']=datam2['Start Time'].apply(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S.%f'))

#print(datam2[['Activity Type', 'Start Time','Status', 'Comment']])

int =0
datam2['Run Id']=datam2['Comment'].apply(lambda x: fred(x,))

print (datam2[['Run Id', 'Comment','Start Time']])

datat=pd.pivot_table(datam2, index=['Run Id'],values=['Start Time'],  columns=['Comment'] ,aggfunc=[np.min] , fill_value=0)
    
datat['Duration']=datat['amin','Start Time','Merge process - DONE'] - datat['amin','Start Time','Merge process - START']

print (datat)
