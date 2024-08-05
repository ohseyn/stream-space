import pandas as pd
import numpy as np
from scipy.stats import norm

car = np.array([15.078, 15.752, 15.549, 15.56, 16.098, 13.277, 15.462, 16.116, 15.214, 16.93, 14.118, 14.927,
15.382, 16.709, 16.804])
car.mean()
car.std(ddof=1)

t = (car.mean() - 16.0) / (car.std(ddof=1)/np.sqrt(15))
norm.cdf(t, loc=0, scale=1)
norm.ppf(0.975, loc=car.mean(), scale=car.std(ddof=1))
norm.ppf(0.025, loc=car.mean(), scale=car.std(ddof=1))
