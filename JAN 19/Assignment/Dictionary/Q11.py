Q. Program to sort a dictionary by key.
Solution:

info = {'Name':'Nishesh Thakuri',
         'Address':'Gothatar',
          'Course name':'Python',}

for key in sorted(info):
    print("%s: %s" % (key, info[key]))
