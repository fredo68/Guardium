from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from jinja2 import Environment, FileSystemLoader


dir = "/home/fredo/"

data = pd.read_csv(dir+"LBUM_01.csv", sep = ",")



print(data.head() )

summary = data.describe()

summary = summary.transpose()

# print (summary.head())
print (summary)

hist=np.histogram(data['Analyzer Rate'],bins='fd')
print(hist)
# plt.hist(data['Analyzer Rate'],bins='fd')

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

  
# ----- Matplot ib
