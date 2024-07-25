import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1번
def my_pdf(x, mu, sigma):
    return ((sigma * math.sqrt(2*math.pi))**(-1)) * (math.exp((-1)*((x-mu)**2)/2*sigma**2))

x_values = np.linspace(0, 6, 100)
pdf_values = [my_pdf(x, 3, 2) for x in x_values]

plt.plot(x_values, pdf_values)
plt.show()
plt.clf()

#=================================
# 1번 다르게
# math는 값을 하나만 받음. np는 벡터 처리가 가능함.

def Norm(x, mu, sigma):
    return (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
k=np.linspace(-7,13,100)

my_n=Norm(k,3,2)

plt.plot(k,my_n)
plt.show()
plt.clf()

# 2번

norm.cdf(3, 2, 3)
norm.cdf(5, 2, 3) - norm.cdf(2, 2, 3)
norm.cdf(3, 2, 3) + (1 - norm.cdf(7, 2, 3))

#=================================

norm.ppf(0.95, 30, 2)
