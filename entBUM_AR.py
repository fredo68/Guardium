import pandas as pd
import matplotlib.pyplot as plt
import sys
dir = "/home/fredo/"

data = pd.read_csv(dir+"fredoBUM.csv", sep = ",",parse_dates=True)

data['TIMESTAMP2']=pd.to_datetime(data['TIMESTAMP'],format='%Y-%m-%d')

data['TIMESTAMP3']=data['TIMESTAMP2'].dt.strftime('%Y-%m-%d %H:%M')

itemList=['Datasource Name','TIMESTAMP3','PID','MEMORY','ANALYZE_RATE', 'ANALYZER_QUEUE','LOG_RATE', 'LOGGER_QUEUE','SYSTEM_CPU_LOAD','MYSQL_DISK_USAGE','ETH0_RECEIVED']
datas=data[itemList].sort_values(by=['TIMESTAMP3','Datasource Name'])

datas2=datas.loc[(datas['PID'] != 0)]

#ds_list2=datas2['Datasource Name'].unique()
ds_list2=pd.Series(datas2['Datasource Name'].unique())

print ("ds_list2" + ds_list2)


for ll in range (len(ds_list2)):
    for ll2 in range (3, len(itemList)):
        datas3=datas.loc[(datas['Datasource Name']==ds_list2[ll]) ]
        datas4=datas3[['TIMESTAMP3',itemList[ll2]]]
        datas4.plot()
        plt.show()
        plt.hist(datas4[itemList[ll2]])
        plt.show()


# ---- Exit the Script
sys.exit()


## --- Collector 1
datas3=datas.loc[(datas['Datasource Name']==ds_list2[0]) & (datas["ANALYZE_RATE"] != 0)]
datas4=datas3[['TIMESTAMP3','ANALYZE_RATE']]
print(datas4)
datas4.plot()
plt.show()
plt.hist(datas4['ANALYZE_RATE'])
plt.show()

datas4=datas3[['TIMESTAMP3','MEMORY']]
print(datas4)
datas4.plot()
plt.show()

plt.hist(datas4['MEMORY'])
plt.show()

## ---- Collector 2
datas5=datas.loc[(datas['Datasource Name']==ds_list2[1]) & (datas["ANALYZE_RATE"] != 0)]
datas6=datas5[['TIMESTAMP3','ANALYZE_RATE']]
print(datas6)
datas6.plot()
plt.show()

plt.hist(datas6['ANALYZE_RATE'])
plt.show()
