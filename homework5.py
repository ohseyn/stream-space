import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import uniform

x = uniform.rvs(loc=3, scale=7, size=20*10000).reshape(-1, 20)

s_2 = x.var(axis=1, ddof=1) 
sns.histplot(s_2, stat="density", color="red")
plt.axvline(x=np.var(x), color='green', linestyle='-', linewidth=2)
k_2 = x.var(axis=1, ddof=0)
sns.histplot(k_2, stat="density")
plt.axvline(x=np.var(x), color='green', linestyle='-', linewidth=2)
plt.show()
plt.clf()
