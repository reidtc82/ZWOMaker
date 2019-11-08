import numpy as np
import pandas as pd

#ftp test
ftp = 195
target = ftp*1.3
factor = 0.9
mu = target*factor
sigma = mu*((1-factor)*1.5)
ride_a = abs(np.random.normal(mu, sigma, 50))
ride_a /= ftp
print(ride_a)

count, bins, ignored = plt.hist(ride_a, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()

plt.plot(ride_a)
plt.show()

print(np.mean(ride_a))
