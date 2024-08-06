import pandas as pd
import numpy as np
from scipy.stats import t

car = np.array([15.078, 15.752, 15.549, 15.56, 16.098, 13.277, 15.462, 16.116, 15.214, 16.93, 14.118, 14.927,
15.382, 16.709, 16.804])
x_bar = car.mean()
s = car.std(ddof=1)

T = (car.mean() - 16.0) / (s/np.sqrt(15))

df = len(car) - 1
t.cdf(T, df)
x_bar + t.ppf(0.975, df) * (s/np.sqrt(15))
x_bar + t.ppf(0.025, df) * (s/np.sqrt(15)) # x_bar - t.ppf(0.975, df) * (s/np.sqrt(15)) 와 같음
