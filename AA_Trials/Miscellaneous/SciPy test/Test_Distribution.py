from scipy import stats
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# UNIFORM DISTRIBUTION
# =========================================================================

# uniform_data = stats.uniform.rvs(size=10000, loc=0, scale=10)   # generate 100 numbers from 0 to 10
# pd.DataFrame(uniform_data).plot(kind="density", figsize=(9, 9), xlim=(-1, 11))
# plt.show()

# uniform_sci = stats.uniform.rvs(loc=0, scale=10)
# uniform_random = random.uniform(0, 10)
# print(uniform_sci, uniform_random)


# =========================================================================
# NORMAL DISTRIBUTION
# =========================================================================

# normal_data = stats.norm.rvs(size=10000, loc=5, scale=2)
# pd.DataFrame(normal_data).plot(kind="density", figsize=(9, 9), xlim=(-1, 11))
# plt.show()
#
# norm_sci = stats.norm.rvs(loc=5, scale=1)


# =========================================================================
# GAMMA DISTRIBUTION
# =========================================================================

# gamma_data = stats.gamma.rvs(1.99, size=10000, loc=5, scale=2)
# pd.DataFrame(gamma_data).plot(kind="density", figsize=(9, 9), xlim=(-1, 11))
# plt.show()
#
# gamma_sci = stats.norm.rvs(1.99, loc=5, scale=1)

# =========================================================================
# RAYLEIGH DISTRIBUTION
# =========================================================================

# fig, ax = plt.subplots(1, 1)
# x = np.linspace(stats.rayleigh.ppf(0.01, loc=15.61, scale=0.57), stats.rayleigh.ppf(0.99, loc=15.61, scale=0.57), 100)
# ax.plot(x, stats.rayleigh.pdf(x), 'r-', lw=5, alpha=0.6, label='rayleigh pdf')
# plt.show()

# =========================================================================
# TRIANGULAR DISTRIBUTION
# =========================================================================

fig, ax = plt.subplots(1, 1)
# x = np.linspace(stats.triang.ppf(0.01, 0.65, loc=12.88, scale=3.22), stats.triang.ppf(0.99, 0.65, loc=12.88, scale=3.22), 100)
# ax.plot(x, stats.triang.pdf(x, 0.65), 'r-', lw=5, alpha=0.6, label='triang pdf')

r = stats.triang.rvs(0.65, loc=12.88, scale=3.22, size=1000)
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
