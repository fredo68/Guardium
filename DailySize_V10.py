#!/usr/bin/python

import csv
import datetime


# --- This script to process a AAL to extract the amount of data collected daily by each collector
# ---  and write it in the inventory Database

# Read file
# f_in = input("Enter AAL file name, with no extension. .csv is assumed: ");
f_in="Weekly_Data_import_Files"
f_in_t = f_in + ".csv"
f = open(f_in_t,'r')

csv_f = csv.reader(f)

# Write File
f_out = f_in + "_P.csv"
#fw = open(f_out,'wb')
fw = open(f_out,'w')
AALwriter = csv.writer(fw, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL);

# writing header
AALwriter.writerow(['Appliance', 'dayNbr', 'Day Of the Data' , 'Month', 'Week Nbr' , 'Daily Amount of Data in MB'])

# Fields
Activity=0		
Timestamp=1
Status=2
FileName=3
Comment=4

# Loop
for row in csv_f:
  # print(row[0])
  if row[Activity]=="Importing file":
    # Parse Unit of the compressed fileCNK01_Agg_AAL
    size_unit = row[Comment][len(row[Comment])-1:len(row[Comment])]
    # Parse Size of the File (compressed size)
    comp_size = float(row[Comment][6:len(row[Comment])-1])
    de_comp_size = comp_size * 9
    # Compute decompressed size in Megs
    if size_unit == 'K':
      actual_size = de_comp_size / 1024
    elif size_unit == 'G':
      actual_size = de_comp_size * 1024
    else: 
      actual_size = de_comp_size
    # Parse Day Nbr
    string = row[FileName]
    comment = string.split('-',)
    dayNbr = comment[0] 
    # Parse Day of Data
    dayOfData = comment[3][1:5] + "-" + comment[4] + "-" + comment[5][0:2]
    dODd=datetime.datetime.strptime(str(dayOfData),"%Y-%m-%d")
    #print wOData
    # Week day computation
    mo = dODd.month
    # print mo
    da = dODd.day
    # print da
    yea = dODd.year
    # print yea
    dddd=datetime.date(yea,mo,da)
    week_nbr=dddd.isocalendar()[1]
    # Parse appliance name
    applianceFQDN = comment[1].split('.',)
    appliance = applianceFQDN[0]
#   --- Writing in the csv file
    # -- AALwriter.writerow([appliance, dayNbr, dayOfData, mo ,week_nbr ,actual_size])
    data_Amount = (appliance, dayNbr, dayOfData, mo ,week_nbr ,actual_size)
    AALwriter.writerow([appliance, dayNbr, dayOfData, mo ,week_nbr ,actual_size])

# Closing Time
f.close()
fw.close()

# End of Process Message
print("Success !!!!  -- Please Check The DataBase ") ;
