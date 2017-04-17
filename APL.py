# Needed Imports
import pandas as pd
import numpy as np
import datetime

# Upload the file to process
dir = "/home/fredo/"
data = pd.read_csv(dir+"Appliance_1_Agg_APL.csv", sep = ",",parse_dates=True)

# Conversion of the Timestamp column into a DateTime Object. This is actually the crucialpart
data['Timestamp'] = data['Timestamp'].apply(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d %H:%M:%S.%f'))

# Pivot Table to get Start and End times of processes
datat=pd.pivot_table(data.loc[data['Run Id'] > 0],index=['Audit Process Id','Run Id','Audit Task Id'],values=['Timestamp'], aggfunc=[np.min,np.max],  fill_value=0)

# Adding the column with the duration of the process
datat['Diff']=datat[('amax', 'Timestamp')]-datat[('amin', 'Timestamp')]

# Printing the gorgeous Pivot table
print (datat)
