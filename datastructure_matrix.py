from numpy import *

a = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
           ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
           ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
           ['Sun', 13, 15, 19, 16]])

m = reshape(a, (7, 5))
print(m, '\n')

# Print data for Wednesday
print(m[2], '\n')

# Print data for friday evening
print(m[4][3], '\n')

# Update a row in in a Matrix
m[3] = ['Thu', 0, 0, 0, 0]
print(m, '\n')

# Adding a row
# 0 stands for row
m_r = append(m, [['Avg', 12, 15, 13, 11]], 0)
print(m_r, '\n')

# Adding a column
# 1 stands for column
m_c = insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)
print(m_c, '\n')

# Delete a row form a Matrix
m = delete(m, [2], 0)
print(m, '\n')

# Delete a column from a Matrix
m = delete(m, s_[2], 1)
print(m, '\n')

"""
    Matrix is a special case of two dimensional array where each data element is of strictly same size. 
    So every matrix is also a two dimensional array but not vice versa.
"""
