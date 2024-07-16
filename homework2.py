import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mpg = pd.read_csv("C:/Doit_Python-main/Data/mpg.csv")
mpg_new = mpg.copy()
mpg_new

displ1 = mpg.query("displ <= 4")
displ1["hwy"].mean()
displ2 = mpg.query("displ >= 5")
displ2["hwy"].mean()

audi = mpg.query("manufacturer == 'audi'")
audi["cty"].mean()
toyota = mpg.query("manufacturer == 'toyota'")
toyota["cty"].mean()

cfh = mpg.query("manufacturer in ['chevrolet', 'ford', 'honda']")
cfh["hwy"].mean()

audi = mpg.query("manufacturer == 'audi'")
audi.sort_values("hwy", ascending = False).head()

mpg_new = mpg_new.assign(total = mpg_new["cty"] + mpg_new["hwy"])
mpg_new = mpg_new.assign(mean = (mpg_new["cty"] + mpg_new["hwy"])/2)
mpg.assign(total = mpg["cty"] + mpg["hwy"], 
           mean = (mpg["cty"] + mpg["hwy"])/2)\
          .sort_values("mean", ascending = False).head(3)
mpg_new.sort_values("mean", ascending = False).head(3)
