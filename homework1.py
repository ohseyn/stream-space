import pandas as pd
mpg = pd.read_csv("C:/Doit_Python-main/Data/mpg.csv")
mpg_new = mpg.copy()
mpg_new

mpg_new = mpg_new.rename(columns = {"cty" : "city", "hwy" : "highway"})
mpg_new

mpg_new[0:5]

import pandas as pd
midwest = pd.read_csv("C:/Doit_Python-main/Data/midwest.csv")
midwest
midwest.head()
midwest.tail()
midwest.shape
midwest.info()
midwest.describe()

midwest = midwest.rename(columns = {"poptotal" : "total", "popasian" : "asian"})
midwest
midwest.info()

midwest["asian_percentage"] = ((midwest["asian"] / midwest["total"])*100)
midwest
midwest.info()

import matplotlib.pyplot as plot
midwest["asian_percentage"].plot.hist()
plot.show()
plot.clf()

import numpy as np
asian_mean = np.mean(midwest["asian_percentage"])
midwest["asian_mean"] = np.where(midwest["asian_percentage"] > asian_mean, "large", "small")
midwest.tail()

midwest["asian_mean"].value_counts()
count_mean = midwest["asian_mean"].value_counts()
count_mean.plot.bar(rot = 0)
plot.show()
