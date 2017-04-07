#!/usr/bin/python

import csv
import datetime

# --- This script to process a AAL to extract the amount of data collected daily by each collector

# Read file
f_in = raw_input("Enter AAL file name, with no extension. .csv is assumed: ");
f_in_t = f_in + ".csv"
f = open(f_in_t,'r')

csv_f = csv.reader(f)

# Write file
#f_out = raw_input("Enter your outputfile, with no extension. .csv is assumed:");
f_out = f_in + "_P.csv"
fw = open(f_out,'wb')
AALwriter = csv.writer(fw, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# writing header
AALwriter.writerow(['Appliance', 'dayNbr', 'Day Of the Data' , 'Month', 'Week Nbr' , 'Daily Amount of Data in MB'])

# Loop
for row in csv_f:
  # print row[0]
  if row[0]=="Importing file":
    # Parse Unit of the compressed fileCNK01_Agg_AAL
    size_unit = row[4][len(row[4])-1:len(row[4])]
    # Parse Size of the File (compressed size)
    comp_size = float(row[4][6:len(row[4])-1])
    de_comp_size = comp_size * 9
    # Compute decompressed size in Megs
    if size_unit == 'K':
      actual_size = de_comp_size / 1024
    elif size_unit == 'G':
      actual_size = de_comp_size * 1024
    else: 
      actual_size = de_comp_size
    # Parse Day Nbr
    string = row[2]
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
    #print dayNbr + " -- " + appliance +  " -- " + str(comp_size) +  " -- " + size_unit +  " -- " + str(actual_size)+  " -- " + dayOfData
    AALwriter.writerow([appliance, dayNbr, dayOfData, mo ,week_nbr ,actual_size])

# Closing Time
f.close()
fw.close()

# End of Process Message
print "Success !!!!  -- Please review the output file: " + f_out
