import numpy as np
import matplotlib.pyplot as plt

x = np.array([6.1, 12.6, 34.7, 1.6, 18.8, 2.2, 3, 2.2, 5.6, 3.8, 2.2, 3.1, 1.3, 1.1, 14.1, 4, 21, 6.1, 1.3, 20.4, 7.5, 3.9, 10.1, 8.1, 19.5, 5.2, 12, 15.8, 10.4, 5.2, 6.4, 10.8, 83.1, 3.6, 6.2, 6.3, 16.3, 12.7, 1.3, 0.8, 8.8, 5.1, 3.7, 26.3, 6, 48, 8.2, 11.7, 7.2, 3.9, 15.3, 16.6, 8.8, 12, 4.7, 14.7, 6.4, 17, 2.5, 16.2])

num_bins = 10

plt.hist(x, num_bins, range=[0, 100], normed=0, facecolor='green', alpha=0.5)
ymin, ymax = plt.ylim()
plt.yticks ( np.arange(ymin, ymax+10, 10) )
plt.xlabel('FundRsng')
plt.ylabel('Frequency')
plt.show()

