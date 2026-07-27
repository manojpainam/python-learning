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
Copy - Copy is a new array -  any modifcations done to the copied array will not effect the orginal array
View - view is just a view of original array - nay modifcations done to the existing array will affec the orginal array as well
'''
cp_arr = arr.copy()
cp_arr[0] = 69
print("Copied array after modification is :", cp_arr, "Original array even after modfications", arr)

view_arr = arr.view()
view_arr[0] = 56
print("Array after view applied :", view_arr, "Original array:", arr)

#print the base of the array
#Copy - None (as this is a new array created from the existing array) , View - arary that is got from as a view
print("Base array for copied array:", cp_arr.base, "base array for view array:", view_arr)


'''
Shape of the array - Shape of the array is number of dimensions in the array
'''
#It is represented in tuple
print("Shape of the array is:", array_4d.shape)

'''
Reshaping - add/delete dimensions of the array
            4 - dimensions and 3 - values in each
'''
arr_re = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Reshaped array is:", arr_re.reshape(4, 3))
print("Unknown dimensions:", arr_re.reshape(2, 2, -1))
print("Flattening arrays:", array_2d.reshape(-1))


'''
Iterating arrays
'''
#iterating single dimensional arrays
for element in arr_re:
    print(element)

#iteratng 2-d arrays
for elements in array_2d:
    print("Outer elements:", elements)
    for element in elements:
        print("inner element:", element)

#iterating using nditer function
for i in np.nditer(arr):
    print(i)

#change the data type of element during runtime
for i in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(i)

#Enumeration - Enumeration means mentioning sequence number of somethings one by one.
for idx, x in np.ndenumerate(arr):
    print(idx, x)

'''
Joining - Putting two or more arrays in a single array
'''
arr = np.concatenate((arr, arr_re))
print("Array after joining:", arr)

array_2d_1 = np.array([[10, 11, 12], [13, 14, 15]])
print(array_2d_1)

#using stack
arr_stack = np.stack((arr2, array_1d), axis=1)
print("Stack arrays:", arr_stack)

#Split
print("Split array:", np.array_split(arr_re, 3))

#Searching arrays - getting the elements of the array using search
print("element found at the indexes:", np.where(arr == 2), "element which are divisble 2:", np.where(arr % 2 == 0))

#searching element from the side using sorting
print("Searching the element from the sorted array using the side:", np.searchsorted(arr, 7, side="right"))

#Sorting
print("Sorted array is:", np.sort(arr))

#Filtering - getting some elements of the existing array and creating new array out of them is called filtering
#this can also be done using the conditions as well
x = [True, False, True, False,  True]
print("newly created array:", array_1d[x])
