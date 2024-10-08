import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_welfare = pd.read_spss("C:/Data/Koweps_hpwc14_2019_beta2.sav")
welfare = raw_welfare.copy()

welfare = welfare.rename(
    columns = {"h14_g3" :"sex",
                "h14_g4" : "birth",
                "h14_g10" : "marriage_type",
                "h14_g11" : "religion",
                "p1402_8aq1" : "income",
                "h14_eco9" : "code_job",
                "h14_reg7" : "code_region"})
welfare = welfare[["sex", "birth", "marriage_type", "religion", "income", "code_job", "code_region"]]

welfare["sex"].dtypes
welfare["sex"].value_counts()
welfare["sex"].isna().sum() 
welfare["sex"]=np.where(welfare["sex"]==1, "male", "female") 
sns.countplot(data = welfare, x = "sex")
plt.show()
plt.clf()

welfare["income"].describe() 
welfare["income"].isna().sum() 
welfare["income"]=np.where(welfare["income"] == 9999, np.nan, welfare["income"])

sex_income = welfare.dropna(subset = "income")\
            .groupby("sex", as_index=False)\
            .agg(mean_income=("income", "mean"))
sns.barplot(data = sex_income, x = "sex", y ="mean_income") 
plt.show()
plt.clf()

from scipy.stats import norm

my_df = welfare.dropna(subset = "income")\
            .groupby("sex", as_index = False)\
            .agg(mean = ("income","mean"),
             std = ("income","std"),
             n = ("sex","count"))

my_df["bottom_ci"] = my_df["mean"] - 1.96*my_df["std"]/np.sqrt(my_df["n"])
my_df["upper_ci"] = my_df["mean"] + 1.96*my_df["std"]/np.sqrt(my_df["n"])
plt.errorbar(my_df["sex"], my_df["mean"], yerr=1.96 * my_df["std"] / np.sqrt(my_df["n"]), 
            fmt='none', c='black', capsize=5)
sns.barplot(data = my_df, x = "sex", y ="mean") 
plt.show()
plt.clf()
