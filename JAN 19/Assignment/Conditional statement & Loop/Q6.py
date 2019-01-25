Q.Program which takes two digits m (row) and n (column) as input and
generates a two-dimensional array. The element value in the i-th row and j-th column of the
array should be i*j.
Solution:

row_m = int(input("Input number of rows: "))
col_n = int(input("Input number of columns: "))
_list = [[0 for col in range(col_n)] for row in range(row_m)]

for row in range(row_m):
    for col in range(col_n):
        _list[row][col]= row*col

print(_list)
