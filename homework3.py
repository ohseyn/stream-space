import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

mpg = pd.read_csv("C:/Data/mpg.csv")
sns.scatterplot(data = mpg, x = "cty", y = "hwy")
plt.show()
plt.clf()

midwest = pd.read_csv("C:/Data/midwest.csv")
sns.scatterplot(data = midwest, x = "poptotal", y = "popasian").set(xlim=[0,500000], ylim=[0,10000])
plt.show()
plt.clf()

mpg = pd.read_csv("C:/Data/mpg.csv")
suv = mpg.query("category == 'suv'").groupby("manufacturer", as_index = False)\
                                    .agg(mean_cty = ("cty", "mean"))\
                                    .sort_values("mean_cty", ascending = False)\
                                    .head(5)
sns.barplot(data = suv, x = "manufacturer", y = "mean_cty", hue = "manufacturer")
plt.show()
plt.clf()

df_category = mpg.groupby("category", as_index = False)\
                .agg(category_count = ("category", "count"))\
                .sort_values("category_count", ascending = False)
sns.barplot(data = df_category, x = "category", y = "category_count", hue = "category")
plt.show()
plt.clf()
