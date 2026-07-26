'''
Numpy - It is a pythin librarory used to work with arrays
        it is also used for linear algbra, forier transform and matrics
        why - it is faster than the lists
        it stores the memory in continious manner so that it doesn't take much time to access the data
        installation - using command : pip install numpy
'''
#importing numpy alias to np
import numpy as np


arr = np.array([1, 2, 3, 4, 5])
print(arr)

#check numpy version
print(np.__version__)

#the array object in numppyis called as ndarray
print("type of array in numpy is:", type(arr))

#to create an array we can pass either as a list, typle or set as well
arr2 = np.array((1, 2, 3, 4, 5))
print(arr2)


'''
Dinemnsons in arrays - a dimension in array length is one level of array depth
'''
array_od = np.array(90)
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#using ndmin we can deine the number of dimensions
array_4d = np.array([1, 2, 3, 4], ndmin=4)
print("0D array:", array_od, "\n1D array:", array_1d, "\n2D array:", array_2d, "\n3D arrays:", array_3d)
print("Multi dimensional arrays:", array_4d.ndim)

'''
Array Indexing
'''
#Accessing array elements
print(arr[0])

#Accessing array elements - 2D
print(array_2d[0, 1])

#Accessing array elements - 3D
print(array_3d[0, 1, 2])

#negative indexing 
print(array_2d[1, -1])

'''
Slicing
'''
#slice array elements
print(arr[1:3])

#from third to end
print(arr[3:])

#negative indexing
print(arr[-3:-1])

#step in slicing by two
print(arr[0::2])

#print elements from the 2d arrays - array[row_selector, column_selector]
print(array_2d[1, 3])

#certain values from to
print(array_2d[1, 1:3])

#from both arrays
print(array_2d[0:2, 1:3])


'''
Data types in Numpy - In numpy we have the following data types
                      i - integer, b - boolean, u - unsigned integer, f - float, c - complex float, m - timedelta, M - datetime, O - object
                      S - string, U - unicode string, V - fixed chunck of memeory for other types (Void)
'''
#checking data type of the array object
print(arr.dtype)
str_arr = np.array(['banana', 'apple'])
print(str_arr.dtype)

#creating array with definite datatype
int_arr = np.array([1, 2, 3, 4, 5], dtype='i')

#change existing array object datatype
new_arr = arr.astype('i')

#change data type from one to the other
float_arr = np.array([1.1, 2.2, 3.6])
new_float_arr = float_arr.astype('i')
print(new_float_arr)


'''
Copy - Copy is a new array 
View - view is just a view of original array
'''