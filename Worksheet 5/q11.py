import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
years = np.array([2000, 2005, 2010, 2015, 2020])
pop = np.array([50, 55, 70, 80, 90])
pearson_corr = np.corrcoef(years, pop)[0, 1]
f = interp1d(years, pop)
pop_2008 = f(2008)
plt.plot(years, pop, 'o-', label='Population')
plt.plot(2008, pop_2008, 'ro', label='2008 estimate')
plt.legend()
plt.show()
print(pearson_corr)
print(pop_2008)