import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dir = "/home/fredo/"

data = pd.read_csv(dir+"AAL_P.csv", sep = ",")

print(data.head() )

summary = data.describe()

summary = summary.transpose()

#print (summary.head())

pivTab=pd.pivot_table(data,index=["Appliance"],values=["Daily Amount of Data in MB"],
aggfunc=[np.mean, np.std],  fill_value=0)
pivTab2=pd.DataFrame(pd.pivot_table(data,index=["Appliance"],values=["Daily Amount of Data in MB"],
aggfunc=[np.mean, np.std],  fill_value=0))

print (pivTab.info())
print (pivTab2.info())
print(pivTab2)
print(pivTab2[('mean','Daily Amount of Data in MB' )])
print(pivTab2[('std','Daily Amount of Data in MB' )])

pivTab2['RSTD']=(pivTab2[('std','Daily Amount of Data in MB' )])/(pivTab2[('mean','Daily Amount of Data in MB' )])
print ('pivTab2')
print (pivTab2)
pivTab3=pivTab2.sort_values(('mean','Daily Amount of Data in MB'),axis=0,  ascending=False)
print('pivTab3')
print(pivTab3)
print (type(pivTab3.info))

Appliance_Mean=(pivTab2[('mean','Daily Amount of Data in MB' )]).mean()
print(Appliance_Mean)

pivTab3.columns = ['Appl_Mean',  'Appl_Std',  'RSTD']
print (pivTab3)

pivTab3['Relative Load'] = pivTab3['Appl_Mean']  / Appliance_Mean
pivTab3.columns = ['Appl_Mean',  'Appl_Std',  'RSTD', 'Relative Load']
print (pivTab3)

print ('Overloaded' + str(pivTab3['Relative Load']>=1.2))

# ----- Matplot ib
