'''
Random Number - Random number does not mean different number every time. random means something that can not be predicted logically.
'''
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Random number is:", random.randint(100))
print("Random Float is:", random.rand())
print("Random array:", random.randint(100, size=(5)))

'''
Random Data distribution - Data distribution is a list of all possible values and how often each value occurs
                           A random distribution is a set of numbers that follow a certain posibility density function

'''
print("Random data distribution is:", random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.5, 0.1], size=(10)))

'''
Random Permutation - a random permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
                    there are two methods to do the same - shuffule() and permutation()
'''
#shuffle - changing arrangement of elements inplace
arr = np.array([1, 2, 3, 4, 5])
arr1 = arr
#The shuffle() method makes changes to the original array.
print(random.shuffle(arr))

#the permutation() method returns a re-arranged array and leaves the original array un-changed
print(random.permutation(arr1))

'''
Seaborn is a library which uses a matpoltlib underneath to plot graps. It is used to visualize random distribution
'''
# sns.displot([0, 1, 2, 3, 4, 5])
# plt.show()

#plotting a displot without the histogram
sns.displot([0, 1, 2, 5, 4, 5], kind="kde")
plt.show()