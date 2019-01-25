Q. Python script to sort (ascending and descending) a dictionary by value
Solution:
    
import operator
d = {8: 9, 3: 4, 4: 3, 2: 1, 1: 0}
print('Original dictionary :',d)
sort_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sort_d)
sort_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sort_d)
